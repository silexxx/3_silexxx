import sqlite3 as lite 
import sys 

# def blood_bank_location_list():
# 	blood_bank_location_list=[]
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()     
# 		cur.execute('''select distinct BLOOD_BANK_LOCATION from BloodBanks ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)

# 		for i in rows:
# 			blood_bank_location_list.append(i[0])
# 			print(i[0])
# 		return blood_bank_location_list

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# result=blood_bank_location_list()
# print(result)



# def check_if_exist():
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()     
# 		cur.execute('''select  *  from BloodBanks  WHERE BLOOD_BANK_NAME='BELGAUM' and BLOOD_BANK_LOCATION='BELGAUM'    ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)

# 		if  len(rows) == 0:
# 			return False
# 		else:
# 			return True

# 		for row in rows:
# 			print(row)
# 		return row

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# print(check_if_exist())

# def blood_bank_location_list():
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()     
# 		cur.execute('''DELETE FROM  BloodBanks WHERE ID=5''')
# 		con.commit()
# 		# rows = cur.fetchall()

# 		# for row in rows:
# 		# 	print(row)
# 		# return row

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# result=blood_bank_location_list()
# print(result)


# result=blood_bank_location_list()
# print(result)


# def blood_bank_names_list():
# 	blood_bank_names_list=[]
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()
# 		names='BELGAUM'
# 		cur.execute(f'''select distinct BLOOD_BANK_NAME from BloodBanks where BLOOD_BANK_LOCATION='{names}' ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)

# 		for i in rows:
# 			blood_bank_names_list.append(i[0])
# 			print(i[0])
# 		return blood_bank_names_list

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()

# print(blood_bank_names_list())



# def update_bank_record_db(name,location,new_name,new_location,new_zipcode):
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()
# 		names='BELGAUM'
# 		cur.execute('SELECT * FROM BloodBanks')
# 		print(new_name)
# 		cur.execute(f'''UPDATE BloodBanks SET BLOOD_BANK_NAME='{new_name}',BLOOD_BANK_LOCATION='{new_location}',ZIPCODE={new_zipcode} where BLOOD_BANK_LOCATION='{location}' and BLOOD_BANK_NAME='{name}' ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)


# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()
# print(update_bank_record_db('KLE','BELGAUM','KLES','BELGAUMS','590005'))


def authentication(username,password,name,location):
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()     
		cur.execute('''select  *  from usernames  WHERE USERNAME='{username}' and PASSWORD='{password}' and BLOOD_BANK_LOCATION='{name}',BLOOD_BANK_NAME='{location}'   ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)

		if  len(rows) == 0:
			return False
		else:
			return True

		for row in rows:
			print(row)
		return row

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()

# SELECT * 
# FROM usernames
# WHERE USERNAME='daneshwar' and PASSWORD='daneshwar' and BLOOD_BANK_LOCATION='KLE' and BLOOD_BANK_NAME='BELGAUM' 