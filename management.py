import streamlit as st
import sqlite3 as lite 
import sys 
from PIL import Image
image = Image.open('logo.jpg')

st.sidebar.title('-------------Ray-------------')
st.sidebar.image(image, caption='')

st.title('BLOOD BANK SYSTEM AND CREDENTIALS MANAGEMENT')
username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')
login_checkbox = st.sidebar.checkbox('Login')


def Add_New_Bank_db(recordList):
	try:
		con = lite.connect('blood_bank.db') 
		cur = con.cursor()     
		sqlite_insert_query='''INSERT INTO BloodBanks(BLOOD_BANK_NAME ,BLOOD_BANK_LOCATION ,ZIPCODE ) VALUES (?, ?, ?);'''
		cur.executemany(sqlite_insert_query, recordList)
		con.commit()

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()

# def Update_Excisting_Bank(recordList):
# 	try:
# 		con = lite.connect('blood_bank.db') 
# 		cur = con.cursor()     
# 		sqlite_insert_query='''INSERT INTO BloodBanks(BLOOD_BANK_NAME ,BLOOD_BANK_LOCATION ,ZIPCODE ) VALUES (?, ?, ?);'''
# 		cur.executemany(sqlite_insert_query, recordList)
# 		con.commit()

# 	except Exception as e: 
# 		if con: 
# 			con.rollback() 

# 		print("Unexpected error %s:" % e.args[0]) 
# 		sys.exit(1) 
# 	finally: 
# 		if con: 
# 			con.close()



def check_if_exist(name,location):
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()     
		cur.execute(f'''select  *  from BloodBanks  WHERE BLOOD_BANK_NAME='{name}' and BLOOD_BANK_LOCATION='{location}'    ''')
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



def blood_bank_location_list():
	blood_bank_location_list=[]
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()     
		cur.execute('''select distinct BLOOD_BANK_LOCATION from BloodBanks ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)

		for i in rows:
			blood_bank_location_list.append(i[0])
			print(i[0])
		return blood_bank_location_list

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()

def blood_bank_names_list(location):
	print(location)
	blood_bank_names_list=[]
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''select distinct BLOOD_BANK_NAME from BloodBanks where BLOOD_BANK_LOCATION='{location}' ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)

		for i in rows:
			blood_bank_names_list.append(i[0])
			print(i[0])
		return blood_bank_names_list

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()



def Add_New_Bank():
	with st.form(key='Add_New_Bank_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of the New Bank').upper()
		location=st.text_input('Please Enter Location of the New Bank').upper()
		zipcode=st.text_input('Please Enter the zipcode of New Bank location')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		recordList=[(name,location,zipcode)]
		result=check_if_exist(name,location)
		if result==True:
			st.write("Record Alredy Exists")
		else:
			Add_New_Bank_db(recordList)
			st.write("Records are saved")


def Assign_New_USER_db(recordList):
	try:
		con = lite.connect('blood_bank.db') 
		cur = con.cursor()     
		sqlite_insert_query='''INSERT INTO usernames(NAME,EMAIL,CITY ,ZIPCODE ,PHONENO ,USERA ,PASSA ,BLOOD_BANK_LOCATION ,BLOOD_BANK_NAME) VALUES (?, ?, ?,?,?,?,?,?,?);'''
		cur.executemany(sqlite_insert_query, recordList)
		con.commit()

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()

def update_bank_record_db(name,location,new_name,new_location,new_zipcode):
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		names='BELGAUM'
		cur.execute('SELECT * FROM BloodBanks')
		print(new_name)
		cur.execute(f'''UPDATE BloodBanks SET BLOOD_BANK_NAME='{new_name}',BLOOD_BANK_LOCATION='{new_location}',ZIPCODE={new_zipcode} where BLOOD_BANK_LOCATION='{location}' and BLOOD_BANK_NAME='{name}' ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)


	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()


def Update_Excisting_Bank():
	with st.form(key='Update_Excisting_Bank_form'):
		global blood_bank_location,blood_bank_name
		
		st.write('Please Enter the Details to Update')
		name =st.text_input('Please Enter New Name of the  Bank')
		location=st.text_input('Please Enter New Location of the Bank')
		zipcode=st.text_input('Please Enter the New Bank location zipcode')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Records are saved")
		Assign_New_USER_db(blood_bank_name,blood_bank_location,name,location,zipcode)
		

def Assign_New_USER():
	with st.form(key='Assign_New_USER_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		username=st.text_input('Please Enter usename to be assigned')
		password=st.text_input('Please Enter password to be assigned')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,username,password,blood_bank_location,blood_bank_name)]
		Assign_New_USER_db(recordList)
		st.write("Records are saved")
		



if login_checkbox:
	if username=='1' and password=='1':
		
		operation = st.sidebar.radio("Please Select type of operation:",('Add_New_Bank', 'Update_Existing_Bank','Assign_New_USER'))
		if operation == 'Add_New_Bank':
			Add_New_Bank()
		elif operation == 'Update_Existing_Bank':
			blood_bank_locations=blood_bank_location_list()
			blood_bank_location_tuple=tuple(blood_bank_locations)
			blood_bank_location = st.selectbox('Please Choose Blood Bank location',blood_bank_location_tuple)
			blood_bank_names=blood_bank_names_list(blood_bank_location)
			blood_bank_names=tuple(blood_bank_names)
			print(blood_bank_names)
			blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_names)
			Update_Excisting_Bank()

		elif operation == 'Assign_New_USER':
			blood_bank_locations=blood_bank_location_list()
			blood_bank_location_tuple=tuple(blood_bank_locations)
			blood_bank_location = st.selectbox('Please Choose Blood Bank location',blood_bank_location_tuple)
			blood_bank_names=blood_bank_names_list(blood_bank_location)
			blood_bank_names=tuple(blood_bank_names)
			print(blood_bank_names)
			blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_names)
			Assign_New_USER()
			

else:
	st.write('Wrong Username or Password')