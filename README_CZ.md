# Elections Scraper

### Popis projektu
Skrip slouží ke stahování výsledků českých parlamentních voleb 2017 ze stránky [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Vstupní odkaz je na úrovni seznamu obcí územního celku jako například [Prostějov](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103), [Praha](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100), [Ostava-město](https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=14&xnumnuts=8106). Projekt vznikl jako třetí zadání [Engeto](https://engeto.cz/) Python Akademie.

### Instalace knihoven
Seznam použitých knihoven třetích stran je uveden v souboru requirments.txt

### Spuštění projektu
Program je spuštěn v příkazovém řádku se dvěma argumenty, URL pro výběr obce na úrovni územního celku a název CSV souboru do kterého bude výstup uložen.

### Ukázka využití projektu

Výsledky hlasování pro okres Hradec Králové:

1.argument: "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201"

2.argument: "hradec_kralove.csv"

Spuštění skriptu:

```
python projekt_3.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=8&xnumnuts=5201" "hradec_kralove.csv"
```

Ukázka části výstupu:

```
code,location,registered,envelopes,valid,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
569828,Babice,165,109,108,7,1,0,4,0,7,19,3,0,0,1,0,6,0,9,36,0,0,2,1,0,0,12,0
569836,Barchov,227,141,140,21,0,0,9,0,5,16,2,0,2,0,0,19,1,4,46,1,0,3,2,1,1,6,1
569852,Běleč nad Orlicí,269,207,206,38,0,0,8,0,9,1,3,0,7,0,0,16,0,12,76,0,0,10,1,0,0,25,0
569861,Benátky,93,67,67,9,0,0,2,0,9,1,0,0,2,0,0,7,0,5,19,0,0,5,0,0,2,6,0
```




