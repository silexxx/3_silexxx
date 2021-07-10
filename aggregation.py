# creating table total_quantity
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("CREATE TABLE total_quantity(QUANTITY INTEGER,TYPE TEXT,BLOOD_BANK_LOCATION TEXT,BLOOD_BANK_NAME TEXT)")
#     con.commit() 
             
# except Exception as e: 
#     if con: 
#         con.rollback() 
     
#     print("Unexpected error %s:" % e.args[0]) 
#     sys.exit(1) 
# finally: 
#     if con: 
#         con.close()

# drop table
# import sqlite3 as lite 
# import sys 
 
# try: 
#     con = lite.connect('blood_bank.db') 
#     cur = con.cursor()     
#     cur.execute("DROP TABLE usernames;")
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
#     cur.execute('''select * from BloodBanks''')
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
