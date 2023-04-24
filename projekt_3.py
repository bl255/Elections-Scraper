import requests
import bs4
import sys
import re
import csv

HEADER_START = ["code", "location", "registered", "envelopes", "valid"]
URL_CORE = "https://www.volby.cz/pls/ps2017nss/"

# ASSIGNING AND CHECKING COMMAND LINE ARGUMENTS
url = sys.argv[1]
csv_file = sys.argv[2]

if csv_file[-3:] != "csv":
    print("Wrong file format.")
    sys.exit()

if "https://www.volby.cz/pls/ps2017nss/" not in url:
    print("Wrong input url.")
    sys.exit()

# CREATING BEAUTIFULSOUP FOR THE INPUT WEBPAGE
area_site_html = requests.get(url)
if area_site_html.status_code != 200:
    print("The connection to the area page was not successful.")
    sys.exit()

area_site_txt = area_site_html.text
area_soup = bs4.BeautifulSoup(area_site_txt, 'html.parser')


# SCRAPING VILLAGES/TOWNS CODES
previous_political_parties_names = None
for village_town in area_soup.find_all(class_="cislo"):
    village_town_code = village_town.find('a').text
    if not village_town_code.isdigit():
        print("Error in the municipality number, the result is not a number.")
        sys.exit()

    # GETTING URL, CONNECTING AND CREATING BEAUTIFULSOUP FOR EACH VILLAGE/TOWN WEBPAGE
    village_town_select = village_town.find('a').get('href')
    village_town_link = f"{URL_CORE}{village_town_select}"

    village_town_html = requests.get(village_town_link)
    if village_town_html.status_code != 200:
        print(f"The connection to the municipality page was not successful.")
        sys.exit()

    village_town_txt = village_town_html.text
    village_town_soup = bs4.BeautifulSoup(village_town_txt, 'html.parser')

    # SCRAPING VILLAGE/TOWN NAME
    village_town_name = [re.search(r": (.*?)\n", h3.text).group(1) for h3 in village_town_soup.find_all("h3")
                         if "Obec:" in h3.text][0]

    # SCRAPING AND CHECKING NUMBER OF VOTERS, NUMBER OF ENVELOPES, NUMBER OF LEGIT VOTES AND NAMES OF POLITICAL PARTIES
    # FOR EACH VILLAGE/TOWN
    voters = [item.text.replace("\xa0", "") for item in village_town_soup.find(attrs={"headers": "sa2"})][0]
    if not voters.isdigit():
        print(f"Error in the number of voters for {village_town_name}, the result is not a number.")
        sys.exit()

    envelopes = [item.text.replace("\xa0", "") for item in village_town_soup.find(attrs={"headers": "sa3"})][0]
    if not envelopes.isdigit():
        print(f"Error in the number of envelopes for {village_town_name}, the result is not a number.")
        sys.exit()

    votes = [item.text.replace("\xa0", "") for item in village_town_soup.find(attrs={"headers": "sa6"})][0]
    if not votes.isdigit():
        print(f"Error in the number of valid votes for {village_town_name}, the result is not a number.")
        sys.exit()

    political_parties_names = [item.text for item in village_town_soup.find_all(class_="overflow_name")]

    # CHECKING CONSISTENCY OF POLITICAL PARTIES NAMES AND CREATING AND WRITING CSV HEADER
    if previous_political_parties_names is None:
        previous_political_parties_names = political_parties_names
        with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADER_START + political_parties_names)

    if previous_political_parties_names != political_parties_names:
        print(f"Discord in political parties list for {village_town_name}")
        sys.exit()
    previous_political_parties_names = political_parties_names

    # SCRAPING, CLEANING AND CHECKING NUMBER OF VOTES FOR EACH POLITICAL PARTY
    raw_votes = [item.text for item in village_town_soup.find_all(attrs={"headers": "t1sa2 t1sb3"})] + \
                [item.text for item in village_town_soup.find_all(attrs={"headers": "t2sa2 t2sb3"})]
    cleaned_votes = [item.replace("\xa0", "") for item in raw_votes if item.replace("\xa0", "").isdigit()]

    if len(political_parties_names) != len(cleaned_votes):
        print(f"Discord in length votes/parties list for {village_town_name}")
        print(f"votes:{len(cleaned_votes)} vs. {len(political_parties_names)}, {cleaned_votes}")
        sys.exit()

    # CREATING AND WRITING DATA ROW FOR EACH VILLAGE/TOWN
    data_row = [village_town_code, village_town_name, voters, envelopes, votes] + cleaned_votes

    with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data_row)

print(f"{csv_file} was created")
