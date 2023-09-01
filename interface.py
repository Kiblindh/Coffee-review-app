import sqlite3
import connection
import KaffeQueries

def create_user(con, n): #Gjør at brukeren kan lage en bruker til å innsette i databasen
    cursor = con.cursor()
    for i in range(n):
        epostadresse = input('Skriv epostadresse: ')
        cursor.execute("SELECT * FROM bruker WHERE epostadresse = (?)", (epostadresse, ))
        existing_emails = cursor.fetchall()
        while (existing_emails):
            epostadresse = input('Epostadresse finnes, skriv ny!')
            cursor.execute("SELECT * FROM bruker WHERE epostadresse = (?)", (epostadresse, ))
            existing_emails = cursor.fetchall()
        passord = input('Skriv passord: ')
        navn = input('Skriv navn: ')
        cursor.execute("INSERT INTO bruker VALUES (?, ?, ?)", (epostadresse, passord, navn))
        con.commit()

def print_users(liste): #skriver ut en liste med alle brukerne
    brukere = liste
    for i in range(len(brukere)):
        print(i+1,'Bruker:', brukere[i][0], '- Passord:', brukere[i][1])

def print_kaffe_brenneri(liste): #skriver ut en liste med alle de forskjellige kombinasjonene med kaffe og kaffebrennerier
    kaffe_brenneri = liste
    for i in range(len(kaffe_brenneri)):
        print(i+1,'Kaffe:', kaffe_brenneri[i][1], '- Brenneri:', kaffe_brenneri[i][0])

def print_meny(): #Skriver ut menyen som brukes i interfacen
    print('\nVelkommen til menyen \n')
    print('-------------------------')
    print('Velg 1 for brukerhistorie 1/legge inn anmeldelse av kaffe\nVelg 2 for brukerhistorie 2')
    print('Velg 3 for brukerhistorie 3\nVelg 4 for brukerhistorie 4')
    print('Velg 5 for brukerhistorie 5')


def interface(con): #Selve programmet som kjøres, beskriver valgene til brukeren underveis
    cursor = con.cursor()
    x = '-1'
    print('Trykk på 1 hvis du ønsker å bruke en eksisterende bruker, trykk på 2 hvis du ønsker å lage en ny bruker')
    lage_bruker = input('Valg: ')
    if lage_bruker == '2':
        create_user(con, 1)

    while(x != '0'):
        cursor.execute("SELECT epostadresse, passord FROM bruker")
        brukere = cursor.fetchall()
        print_users(brukere)
        epostadresse1 = input('Hvilken bruker er du? Velg 1-5: ')
        epostadresse = brukere[int(epostadresse1)-1][0] #epostadressen til brukeren
        print_meny()
        x = input('Velg et tall fra 1 til 5 (eller 0 hvis du vil avslutte)\n')
        if (x == '1'):
            print('Skriv "ja" hvis du ønsker å legge inn en anmeldelse eller noe annet hvis du ønsker å avslutte')
            b = input('Vil du legge inn en review? \n')
            if b.lower() == 'ja':
                smaksdato = '22.03.2022'

                cursor.execute("SELECT brennerinavn, navn FROM kaffe")
                kaffe_brenneri = cursor.fetchall()
                print('Velg en av de følgende to kombinasjonene. Bruker kan ikke legge inn en anmeldelse på en kaffe og bryggeri som ikke er i databasen')
                print_kaffe_brenneri(kaffe_brenneri)

                navn = input('Skriv kaffenavn: ')
                brenneri = input('Skriv brenneriet: ')
                poeng = input('Skriv poeng: ')

                cursor.execute("SELECT kaffeID FROM kaffe WHERE kaffe.navn = ? AND kaffe.brennerinavn = ? ", [navn, brenneri])
                kaffeID_temp = cursor.fetchall()
                #print(kaffeID_temp)
                kaffeID = kaffeID_temp[0][0]
                #print(kaffeID)

                smaksnotat = input('Skriv smaksnotat\n')
                cursor.execute("INSERT INTO kaffesmaking (epostadresse, smaksDato, kaffeID, poengscore, smaksNotater) VALUES (?, ?,?,?,?)", (epostadresse,smaksdato,kaffeID, poeng, smaksnotat))
                con.commit()
                x = '0'
            else:
                break
        
        elif (x == '2'):
            KaffeQueries.kaffequery2()
            break

        elif (x == '3'):
            KaffeQueries.kaffequery3()
            break

        elif(x == '4'):
            KaffeQueries.kaffequery4()
            break

        elif(x == '5'):
            KaffeQueries.kaffequery5()
            break

        else:
            x = '0'


