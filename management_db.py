#creating table BloodBanks
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("CREATE TABLE BloodBanks(ID INTEGER PRIMARY KEY AUTOINCREMENT,BLOOD_BANK_NAME TEXT,BLOOD_BANK_LOCATION TEXT,ZIPCODE INTEGER)")
#     con.commit() 
             
# except Exception as e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()

#drop table
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("DROP TABLE BloodBanks;")
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()

# check values
import sqlite3 as lite 
import sys 
 
try:
    con = lite.connect('blood_bank.db') 
    cur = con.cursor()     
    cur.execute('''select * from BloodBanks''')
    con.commit()
    rows = cur.fetchall()

    for row in rows:
        print(row)
             
except Exception as e: 
    if con: 
        con.rollback() 
     
    print("Unexpected error %s:" % e.args[0]) 
    sys.exit(1) 
finally: 
    if con: 
        con.close()
