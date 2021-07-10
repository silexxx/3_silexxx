# creating table
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("CREATE TABLE depositions(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,EMAIL TEXT,CITY TEXT,ZIPCODE INTEGER,PHONENO INTEGER,BLOOD_GROUP TEXT,BLOOD_QUANTITY INTEGER,BLOOD_BANK_LOCATION TEXT,BLOOD_BANK_NAME TEXT)")
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()


# altering table
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("ALTER TABLE depositions(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,EMAIL TEXT,CITY TEXT,ZIPCODE INTEGER,BLOOD_GROUP TEXT,BLOOD_QUANTITY INTEGER,BLOOD_BANK_LOCATION TEXT,BLOOD_BANK_NAME TEXT)")
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()


#drop tables
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("DROP TABLE depositions;")
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()


#inserting row into database
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute('''INSERT INTO depositions(NAME,EMAIL,CITY,ZIPCODE,PHONENO,BLOOD_GROUP,BLOOD_QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME) VALUES ('Daneshwar', 'daneshsgobbani@gmail.com', 'Belgaum', '590008','7406800528','A+','100','HUBLI','KLE')''')
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()


# import sqlite3 as lite 
# import sys 
 
# try:
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute('''select * from depositions''')
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



# creating table requests
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("CREATE TABLE BloodRequests(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT,EMAIL TEXT,CITY TEXT,ZIPCODE INTEGER,PHONENO INTEGER,BLOOD_GROUP TEXT,BLOOD_QUANTITY INTEGER,BLOOD_BANK_LOCATION TEXT,BLOOD_BANK_NAME TEXT,SHIP_ADDRESS TEXT)")
#     con.commit() 
             
# except e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()