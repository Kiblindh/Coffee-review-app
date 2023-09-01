import sqlite3
import connection
import interface
import SqlScrip
import KaffeQueries
import KaffeDataInsertion

#SqlScrip.script()
#KaffeDataInsertion.kaffeData1()
#KaffeDataInsertion.kaffeData2()
#KaffeDataInsertion.kaffeData3()
#KaffeDataInsertion.kaffeData4()
#KaffeDataInsertion.kaffeData5()
#KaffeDataInsertion.kaffeData6()
#KaffeDataInsertion.kaffeData7()
#KaffeDataInsertion.kaffeData8()
#KaffeDataInsertion.kaffeData9()
#KaffeDataInsertion.kaffeData10()

con = sqlite3.connect('kaffe.db')
interface.interface(con)
con.close()