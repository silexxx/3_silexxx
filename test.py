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


# def authentication(username,password,name,location):
# 	print(username,password,name,location)
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()     
# 		cur.execute(f"select  *  from usernames WHERE USERA='{username}' and PASSA='{password}' and BLOOD_BANK_LOCATION='{location}' and BLOOD_BANK_NAME='{name}' ")
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


# authentication('admin','admin','KIMS','HUBLI')
# SELECT * 
# FROM usernames
# WHERE USERNAME='daneshwar' and PASSWORD='daneshwar' and BLOOD_BANK_LOCATION='KLE' and BLOOD_BANK_NAME='BELGAUM' 


# def aggregation_adding(QUANTITY,TYPE,BLOOD_BANK_NAME,BLOOD_BANK_LOCATION):
# 	try:
# 	con = lite.connect('blood_bank.db')
# 	cur = con.cursor()
# 	names='BELGAUM'
# 	cur.execute('SELECT sum(* FROM BloodBanks')
# 	print(new_name)
# 	cur.execute(f'''UPDATE BloodBanks SET BLOOD_BANK_NAME='{new_name}',BLOOD_BANK_LOCATION='{new_location}',ZIPCODE={new_zipcode} where BLOOD_BANK_LOCATION='{location}' and BLOOD_BANK_NAME='{name}' ''')
# 	con.commit()
# 	rows = cur.fetchall()
# 	print(rows)


# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()
# print(update_bank_record_db('KLE','BELGAUM','KLES','BELGAUMS','590005'))


def aggregation_fetch(QUANTITY):
	print(QUANTITY)
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''select ID,BLOOD_QUANTITY  FROM depositions WHERE BLOOD_QUANTITY >= {QUANTITY}  ORDER BY BLOOD_QUANTITY DESC LIMIT 1 ''')
		con.commit()
		rows = cur.fetchall()
		print(rows[0])
		return rows[0]


	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()
print(aggregation_fetch(200))


# def blood_quantity_available(BLOOD_BANK_NAME,BLOOD_BANK_LOCATION):
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()
# 		cur.execute(f'''SELECT sum(BLOOD_QUANTITY) FROM depositions WHERE BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATION}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAME}' ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows[0][0])
# 	return rows[0][0]

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# blood_quantity_available('KLE','BELGAUM')




# def requests_names(BLOOD_BANK_NAME,BLOOD_BANK_LOCATION):
# 	requests_names_list=[]
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()
# 		cur.execute(f'''SELECT NAME FROM BloodRequests WHERE BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATION}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAME}' order by EXPIRY_DATE ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)
# 		for i in rows:
# 			print(i[0])
# 			requests_names_list.append(i[0])
# 		return requests_names_list

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# print(requests_names('KLE','BELGAUM'))


# def request_details(NAME,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME):
# 	requests_names_list=[]
# 	try:
# 		con = lite.connect('blood_bank.db')
# 		cur = con.cursor()
# 		cur.execute(f'''SELECT BLOOD_GROUP,BLOOD_TYPE,BLOOD_QUANTITY FROM BloodRequests WHERE NAME='{NAME}' AND BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATION}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAME}' AND EXPIRY_DATE < DATE(CURRENT_TIMESTAMP) order by EXPIRY_DATE; ''')
# 		con.commit()
# 		rows = cur.fetchall()
# 		print(rows)
# 		for i in rows:
# 			return i[0],i[1],i[2]

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()


# print(request_details('Daneshwar','BELGAUM','KLE'))



# SELECT BLOOD_GROUP,BLOOD_TYPE,BLOOD_QUANTITY FROM BloodRequests WHERE NAME='Daneshwar' AND BLOOD_BANK_LOCATION='BELGAUM' AND BLOOD_BANK_NAME='KLE' AND EXPIRY_DATE < DATE(CURRENT_TIMESTAMP) order by EXPIRY_DATE;