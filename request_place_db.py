#creating table requests
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("CREATE TABLE BloodRequests(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,EMAIL TEXT,CITY TEXT,ZIPCODE INTEGER,PHONENO INTEGER,BLOOD_GROUP TEXT,BLOOD_TYPE TEXT, BLOOD_QUANTITY INTEGER,EXPIRY_DATE TEXT,BLOOD_BANK_LOCATION TEXT,BLOOD_BANK_NAME TEXT,SHIP_ADDRESS TEXT)")
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
#     cur.execute("DROP TABLE BloodRequests;")
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
# import sqlite3 as lite 
# import sys 
 
# try:
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute('''select * from BloodRequests''')
#     con.commit()
#     rows = cur.fetchall()

#     for row in rows:
#         print(row)
             
# except Exception as e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()
