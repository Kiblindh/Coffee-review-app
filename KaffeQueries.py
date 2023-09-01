import sqlite3
from prettytable import PrettyTable

 

def kaffequery2():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute(""" SELECT bruker.navn as Brukerens_Fulle_Navn,
    COUNT(DISTINCT kaffesmaking.kaffeID) AS Antall_Smaksnotater
    FROM kaffesmaking
    INNER JOIN bruker
    ON bruker.epostadresse = kaffesmaking.epostadresse
    Where kaffesmaking.smaksDato LIKE '%2022%'
    GROUP BY bruker.navn
    ORDER BY Antall_Smaksnotater DESC

        """)

    
    tuppels = cursor.fetchall()
    print("\nTabellen nedenfor er en oversikt over hvem som har smakt på flest unike kaffer i 2022. Sortert i avtagende rekkefølge fra toppen.")
    print("Tabellen er på formen (Fulle navn, Antall smaksnotater):\n")
    
    myTable = PrettyTable(['Fulle navn', 'Antall smaksnotater'])
    
    for item in tuppels:
        myTable.add_row(item)
    
    print(myTable)
        
    con.commit()
    con.close()


def kaffequery3():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute(""" SELECT kaffe.brennerinavn as Brennerinavn, kaffe.navn AS Kaffenavn, ROUND(kaffe.kilopris, 1) AS Kilopris, 
    ROUND(AVG(poengscore),1) AS Gjennomsnittsscore
    FROM kaffe
    INNER JOIN kaffesmaking ON kaffesmaking.kaffeID = kaffe.kaffeID
    GROUP BY kaffesmaking.kaffeID
    ORDER BY kaffe.kilopris/Gjennomsnittsscore ASC

        """)

    tuppels = cursor.fetchall()
    print("\nTabellen nedenfor er rangert fra den kaffen som gir mest smak for pengene øverst, og den som gir minst nederst.")
    print("Tabellen er på formen (Brennerinavn, Kaffenavn, KiloprisNOK, Gjennomsnitlig score fra brukere):\n")
    
    myTable = PrettyTable(['Brennerinavn', 'Kaffenavn', 'KiloprisNOK', 'Gjennomsnitlig score fra brukere'])
    
    for item in tuppels:
        myTable.add_row(item)
    
    print(myTable)
    
    con.commit()    
    con.close()


def kaffequery4():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute("""SELECT DISTINCT kaffe.navn AS Kaffenavn, kaffe.brennerinavn as Brennerinavn
    FROM kaffe
    INNER JOIN kaffesmaking ON kaffesmaking.kaffeID = kaffe.kaffeID
    WHERE kaffesmaking.smaksNotater LIKE '%floral%' OR kaffe.beskrivelse LIKE '%floral%'



            """)

    tuppels = cursor.fetchall()
    print("\nTabellen nedenfor innholder kun kaffer er beskrevet med ordet floral av en bruker eller et brenneri.")
    print("Tabellen er på formen (Kaffenavn, Brennerinavn, ):\n") 

    myTable = PrettyTable(['Kaffenavn', 'Brennerinavn'])
    
    for item in tuppels:
        myTable.add_row(item)
    
    print(myTable)   
    
    
    con.commit()
    con.close()


def kaffequery5():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute("""SELECT kaffe.navn AS Kaffenavn, kaffe.brennerinavn AS Brennerinavn
    FROM kaffe
    INNER JOIN kaffebønneParti ON kaffebønneParti.partiID = kaffe.partiID
    INNER JOIN gård ON kaffebønneParti.gårdID = gård.gårdID
    WHERE (gård.land = 'Rwanda' OR gård.land = 'Colombia') 
    AND kaffebønneParti.foredlingsmetode NOT LIKE '%Vasket%'



        """)

    tuppels = cursor.fetchall()
    print("\nTabellen nedenfor innholder kun kaffer som er uvasket og fra Rwanda eller Colombia.")
    print("Tabellen er på formen (Kaffenavn, Brennerinavn):\n")   


    myTable = PrettyTable(['Kaffenavn', 'Brennerinavn'])    
    for item in tuppels:
        myTable.add_row(item)
    
    print(myTable)
    
    con.commit()
    con.close()





    
