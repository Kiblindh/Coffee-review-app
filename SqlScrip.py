import sqlite3

def script():
    con = sqlite3.connect("kaffe.db")
    cursor = con.cursor()

    cursor.execute('''DROP TABLE IF EXISTS bruker''')
    cursor.execute('''DROP TABLE IF EXISTS kaffesmaking''')       
    cursor.execute('''DROP TABLE IF EXISTS kaffe''')          
    cursor.execute('''DROP TABLE IF EXISTS kaffebønneParti''')         
    cursor.execute('''DROP TABLE IF EXISTS partiInnhold''')       
    cursor.execute('''DROP TABLE IF EXISTS foredlingsmetode''')        
    cursor.execute('''DROP TABLE IF EXISTS gård''')       
    cursor.execute('''DROP TABLE IF EXISTS dyrkesAv''')        
    cursor.execute('''DROP TABLE IF EXISTS kaffebønne''')     

    cursor.execute('''CREATE TABLE bruker
    (epostadresse TEXT PRIMARY KEY,
    passord TEXT, navn TEXT)''')

    cursor.execute('''CREATE TABLE kaffesmaking
    (smaksID INTEGER PRIMARY KEY AUTOINCREMENT, 
    poengscore INTEGER, smaksDato TEXT, smaksNotater TEXT, epostadresse TEXT, kaffeID INTEGER,
    FOREIGN KEY(epostadresse) REFERENCES bruker(epostadresse)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(kaffeID) REFERENCES kaffe(kaffeID)
        ON DELETE CASCADE ON UPDATE NO ACTION)''')

    cursor.execute('''CREATE TABLE kaffe
    (kaffeID INTEGER PRIMARY KEY AUTOINCREMENT,
    brennerinavn TEXT, brenningsGrad TEXT, brennDato TEXT, navn TEXT, beskrivelse TEXT, kilopris REAL, partiID INTEGER,
    FOREIGN KEY(partiID) REFERENCES kaffebønneParti(partiID)
        ON DELETE CASCADE ON UPDATE NO ACTION)''')

    cursor.execute('''CREATE TABLE kaffebønneParti
    (partiID INTEGER PRIMARY KEY AUTOINCREMENT,
    kgpris_parti REAL, innhøstingsår INTEGER, foredlingsmetode TEXT, gårdID INTEGER,
    FOREIGN KEY(foredlingsmetode) REFERENCES foredlingsmetode(navn)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(gårdID) REFERENCES gård(gårdID)
        ON DELETE CASCADE ON UPDATE NO ACTION)''')

    cursor.execute('''CREATE TABLE partiInnhold
    (partiID INTEGER NOT NULL,
    kaffebønneArt TEXT NOT NULL,
    PRIMARY KEY (partiID, kaffebønneArt),
    FOREIGN KEY(kaffebønneArt) REFERENCES kaffebønne(art)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(partiID) REFERENCES kaffebønneParti(partiID)
        ON DELETE CASCADE ON UPDATE NO ACTION)''')

    cursor.execute('''CREATE TABLE foredlingsmetode
    (navn TEXT PRIMARY KEY,
    beskrivelse TEXT)''')

    cursor.execute('''CREATE TABLE gård
    (gårdID INTEGER PRIMARY KEY AUTOINCREMENT,
    meterOverHavet INTEGER, navn TEXT, region TEXT, land TEXT)''')

    cursor.execute('''CREATE TABLE dyrkesAv
    (gårdID INTEGER NOT NULL,
    kaffebønneArt TEXT NOT NULL,
    PRIMARY KEY (gårdID, kaffebønneArt),
    FOREIGN KEY(kaffebønneArt) REFERENCES kaffebønne(art)
        ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY(gårdID) REFERENCES gård(gårdID)
        ON DELETE CASCADE ON UPDATE NO ACTION)''')

    cursor.execute('''CREATE TABLE kaffebønne
    (art TEXT PRIMARY KEY)''')

    con.close()