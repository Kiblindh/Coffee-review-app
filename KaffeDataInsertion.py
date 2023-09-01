import sqlite3
import SqlScrip



def kaffeData1():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art2, art3 = "coffea arabica", "coffea robusta", "coffea liberica"
    

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 1

    #partiInhold(partiID, art | attributter: 2)
    partiID = 10
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'joel123@gmail.com', 'joel123', 'Joel Constantinos'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 100, 'Brenneri A', 'mørk', '15.12.2020', 'Julekaffe 2020', 'En digg og lett kaffe for jula', 500
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 1000, 7, '23.12.2020', 'Wow, et eventyr for smaksløkene: lime, aprikos!'
    
    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 10, 'Bunngård', 'Vestlandet', 'Norge'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Bærtørket', 'Hele kaffebønnen tørkes'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 20, 2020
    


    #Innseter data slik at databasen representerer brukerhistorien:
    cursor.execute('''INSERT INTO kaffebønne VALUES (?)''', (art1,))
    cursor.execute('''INSERT INTO kaffebønne VALUES (?)''', (art2,))
    cursor.execute('''INSERT INTO kaffebønne VALUES (?)''', (art3,))

    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art2))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art3))

    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art2))
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art3))

    cursor.execute('''INSERT INTO bruker VALUES (?,?,?)''', (epostadresse, passord, navn))

    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))
       
    cursor.execute('''INSERT INTO foredlingsmetode VALUES (?,?)''', (foredlingsNavn, metodeBeskrivelse))

    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
        
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData2():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art2 = "coffea arabica", "coffea robusta"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 2 

    #partiInhold(partiID, art | attributter: 2)
    partiID = 20
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'julius123@gmail.com', 'julius123', 'Julius Schjetne'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 200, 'Brenneri B', 'middels', '02.01.2019', 'Nyår kaffe 2021', 'En fin start på året', 300
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 2000, 9, '07.01.2019', 'Fantastisk! Rogaland leverer varene som alltid.'
    
    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 200, 'Rogalandsgården', 'Rogaland', 'Norge'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Vasket', 'Vasket kaffe kjennetegnes ved en frisk og ren smak med markant syre.'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 15, 2018
    


    #Innseter data slik at databasen representerer brukerhistorien:
      
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art2))
    
    
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art2))
   

    cursor.execute('''INSERT INTO bruker VALUES (?,?,?)''', (epostadresse, passord, navn))

    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))
       
    cursor.execute('''INSERT INTO foredlingsmetode VALUES (?,?)''', (foredlingsNavn, metodeBeskrivelse))

    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
        
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData3():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1 = "coffea arabica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 3 

    #partiInhold(partiID, art | attributter: 2)
    partiID = 30
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'kim123@gmail.com', 'kim123', 'Kim-Iver Blindheimsvik'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 300, 'Brenneri C', 'lys', '28.07.2021', 'Sommerkaffe 2021', 'En digg og lett kaffe for en solskinndag', 900
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 3000, 6, '21.06.2022', 'Ganske god, men passer ikke beskrivelsen på pakken!'
    
    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 700, 'Brasilanskgård', 'Rio de Janeiro', 'Brasil'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Vasket', 'Vasket kaffe kjennetegnes ved en frisk og ren smak med markant syre.'

   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 15 , 2021
    


    #Innseter data slik at databasen representerer brukerhistorien: 
    

    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))
   

    cursor.execute('''INSERT INTO bruker VALUES (?,?,?)''', (epostadresse, passord, navn))

    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))
       
    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
        
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData4():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1 = "coffea arabica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 3 

    #partiInhold(partiID, art | attributter: 2)
    partiID = 30
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'julius123@gmail.com', 'julius123', 'Julius Schjetne'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 300, 'Brenneri C', 'lys', '28.07.2021', 'Sommerkaffe 2021', 'En digg og lett kaffe for en solskinndag', 900
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 4000, 4, '21.11.2022', 'Den var helt grei.'
    
    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 700, 'Brasilanskgård', 'Rio de Janeiro', 'Brasil'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Vasket', 'Vasket kaffe kjennetegnes ved en frisk og ren smak med markant syre.'

   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 15 , 2021
    


    #Innseter data slik at databasen representerer brukerhistorien: 

    
   
       
    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    
       
    
    
        
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData5():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art2 = "coffea arabica", "coffea robusta"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 5

    #partiInhold(partiID, art | attributter: 2)
    partiID = 50
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'torleif123@gmail.com', 'torleif123', 'Torleif Brandtzæg'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 500 , 'Jacobsens & Svart', 'lys', '20.01.2022', 'Vinterkaffe 2022', 'En velsmakende og kompleks kaffe for mørketiden', 600
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 5000, 10, '21.02.2022', 'Wow – en odyssé for smaksløkene: sitrusskall, melkesjokolade, aprikos!'

    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 700, 'Nombre De Dios', 'Santa Ana', 'El Salvador'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Bærtørket', 'Hele kaffebønnen tørkes'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 8, 2021
    


    #Innseter data slik at databasen representerer brukerhistorien:

    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art2))
   
      

    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))
    

    cursor.execute('''INSERT INTO bruker VALUES (?,?,?)''', (epostadresse, passord, navn))

    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))
       
    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData6():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art3 = "coffea arabica", "coffea liberica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 6

    #partiInhold(partiID, art | attributter: 2)
    partiID = 60
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'torleif123@gmail.com', 'torleif123', 'Torleif Brandtzæg'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 600 , 'Brenneri D', 'lys', '20.02.2018', 'Sommerkaffe 2018', 'En velsmakende floral kaffe for våren', 900
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 6000, 8, '19.04.2018', 'Kaffen etterlater en floral smak i munnen!'

    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 300, 'Kigali', 'RWD Farm', 'Rwanda'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Bærtørket', 'Hele kaffebønnen tørkes'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 14, 2018
    


    #Innseter data slik at databasen representerer brukerhistorien:

    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art3))
      

    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))    


    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))
       
    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData7():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art3 = "coffea arabica", "coffea liberica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 7

    #partiInhold(partiID, art | attributter: 2)
    partiID = 70
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'torleif123@gmail.com', 'torleif123', 'Torleif Brandtzæg'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 700 , 'Brenneri E', 'lys', '17.05.2017', 'Sommerkaffe 2017', 'En velsmakende floral kaffe for våren', 1000
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 7000, 6, '12.04.2017', 'Ganske god!'

    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 400, 'Bogota', 'Cool Farm', 'Colombia'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Vasket', 'Vasket kaffe kjennetegnes ved en frisk og ren smak med markant syre.'

   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 15, 2017
    


    #Innseter data slik at databasen representerer brukerhistorien:

    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art1))
    cursor.execute('''INSERT INTO dyrkesAv VALUES (?,?)''', (gårdID,art3))
      

    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art1))
    cursor.execute('''INSERT INTO partiInnhold VALUES (?,?)''', (partiID,art3))

    cursor.execute('''INSERT INTO kaffe VALUES (?,?,?,?,?,?,?,?)''', (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID))

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    cursor.execute('''INSERT INTO gård VALUES (?,?,?,?,?)''', (gårdID, moh, gårdsNavn, region, land))

    cursor.execute('''INSERT INTO kaffebønneParti VALUES (?,?,?,?,?)''', (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID))
    
    
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData8():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1 = "coffea arabica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 3 

    #partiInhold(partiID, art | attributter: 2)
    partiID = 30

    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'julius123@gmail.com', 'julius123', 'Julius Schjetne'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 300, 'Brenneri C', 'lys', '28.07.2021', 'Sommerkaffe 2021', 'En digg og lett kaffe for en solskinndag', 900
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 8000, 7, '23.12.2022', 'Smaker betydelig bedre enn sist gang jeg prøvde den. Har fått sansen for kaffer med floral smak. '
    
    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 700, 'Brasilanskgård', 'Rio de Janeiro', 'Brasil'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Vasket', 'Vasket kaffe kjennetegnes ved en frisk og ren smak med markant syre.'

    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 15 , 2021
    


    #Innseter data slik at databasen representerer brukerhistorien:

    
    
    
    

    

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

   
       
   

   
    
        
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData9():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art3 = "coffea arabica", "coffea liberica"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 6

    #partiInhold(partiID, art | attributter: 2)
    partiID = 60
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'joel123@gmail.com', 'joel123', 'Joel Constantinos'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 600 , 'Brenneri D', 'lys', '20.02.2018', 'Sommerkaffe 2018', 'En velsmakende floral kaffe for våren', 900
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 9000, 9, '19.04.2018', 'Denne er verdt å prøve!'

    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 300, 'Kigali', 'RWD Farm', 'Rwanda'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Bærtørket', 'Hele kaffebønnen tørkes'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 14, 2018
    


    #Innseter data slik at databasen representerer brukerhistorien:

    
    
   
      

    
    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))

    
       
   
    
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()


def kaffeData10():

    #Sørger for at python kan brukes til å skrive sql.
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()


    #Lager variabler som innholder data til vær av tabellene:  

    #Kaffebønne(Art | attributter: 1) 
    art1, art2 = "coffea arabica", "coffea robusta"

    #DyrkesAV(gårdID, art | attributter: 2)
    gårdID = 5

    #partiInhold(partiID, art | attributter: 2)
    partiID = 50
    
    #bruker (epostadresse, passord, navn | attributter: 3)
    epostadresse, passord, navn = 'kim123@gmail.com', 'kim123', 'Kim-Iver Blindheimsvik'

    #kaffe (kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK, partiID | attributter: 8)
    kaffeID, brennerinavn, brenningsGrad, brennDato, kaffeNavn, kaffeBeskrivelse, pris_NOK = 500 , 'Jacobsens & Svart', 'lys', '20.01.2022', 'Vinterkaffe 2022', 'En velsmakende og kompleks kaffe for mørketiden', 600
   
    #kaffesmaking ( smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID | attributter: 6)
    smaksID, poengscore, smaksDato, smaksNotater = 10000, 8, '21.02.2022', 'Vanskelig å overgå!'

    #Gård (gårdID, moh, gårdsNavn, region, land | attributter: 5)
    moh, gårdsNavn, region, land = 700, 'Nombre De Dios', 'Santa Ana', 'El Salvador'
   
    #Foredlinsgmetode ( foredlingsNavn, metodeBeskrivelse | attributter: 2)
    foredlingsNavn, metodeBeskrivelse = 'Bærtørket', 'Hele kaffebønnen tørkes'
   
    #KaffebønneParti (partiID, pris_USD, innhøstingsår, foredlingsNavn, gårdID | attributter: 5)
    pris_USD, innhøstingsår = 8, 2021
    


    
    
    
    #Innseter data slik at databasen representerer brukerhistorien:    

    cursor.execute('''INSERT INTO kaffesmaking VALUES (?,?,?,?,?,?)''', (smaksID, poengscore, smaksDato, smaksNotater, epostadresse, kaffeID))   
    
    
    #Lagrer data som ble skrevet, og lukker sql tilkoblesen:
    con.commit()
    con.close()

