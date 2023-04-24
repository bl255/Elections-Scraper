# Elections Scraper

### Project Description
The script is used to download the results of the 2017 Czech parliamentary elections from the [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). The input link is at the level of a list of municipalities within a territorial unit, such as [Prostějov](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103), [Praha](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100), [Ostava-město](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106). The project was created as the third assignment for the [Engeto](https://engeto.cz/) Python Academy.

### Library Installation
The list of third-party libraries used is included in the requirements.txt file.

### Running the Project
The program is run on the command line with two arguments: the URL for selecting the municipality at the territorial unit level and the name of the CSV file where the output will be stored.

### Example of the Project Use
Voting results for the Hradec Králové district:

1st argument: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201"

2nd argument: "hradec_kralove.csv"

Running the script:

```
python projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201" "hradec_kralove.csv"
```

Example of part of the output:

```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
569828,Babice,165,109,108,7,1,0,4,0,7,19,3,0,0,1,0,6,0,9,36,0,0,2,1,0,0,12,0
569836,Barchov,227,141,140,21,0,0,9,0,5,16,2,0,2,0,0,19,1,4,46,1,0,3,2,1,1,6,1
569852,Běleč nad Orlicí,269,207,206,38,0,0,8,0,9,1,3,0,7,0,0,16,0,12,76,0,0,10,1,0,0,25,0
569861,Benátky,93,67,67,9,0,0,2,0,9,1,0,0,2,0,0,7,0,5,19,0,0,5,0,0,2,6,0
```