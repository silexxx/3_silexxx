import streamlit as st
import sqlite3 as lite 
import sys 



st.title('APPNAME')


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

blood_bank_locations=blood_bank_location_list()
blood_bank_location_tuple=tuple(blood_bank_locations)
blood_bank_location = st.sidebar.selectbox('Please Choose Blood Bank location',blood_bank_location_tuple)
blood_bank_names=blood_bank_names_list(blood_bank_location)
blood_bank_names=tuple(blood_bank_names)
blood_bank_name = st.sidebar.selectbox('Please Choose Blood Bank Name',blood_bank_names)


def authentication(name,passs,bank_name,bank_location):
	print(name,passs,bank_name,bank_location)
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()     
		cur.execute(f''' select  *  from usernames WHERE USERA='{name}' and PASSA='{passs}' and BLOOD_BANK_LOCATION='{bank_name}' and BLOOD_BANK_NAME='{bank_location}' ''')
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




def deposit_db(recordList):
	try:
		con = lite.connect('blood_bank.db') 
		cur = con.cursor()     
		sqlite_insert_query='''INSERT INTO depositions(NAME,EMAIL,CITY,ZIPCODE,PHONENO,BLOOD_GROUP,BLOOD_QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME) VALUES (?, ?, ?, ?, ?,?,?,?,?);'''
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



def individual():
	with st.form(key='individual_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.number_input('Please Enter Phone Number')
		phone_no=int(phone_no)
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name

def donation_camps():
	with st.form(key='donation_camps_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Institute')
		email=st.text_input('Please Enter Institute Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.number_input('Please Enter Phone Number')
		phone_no=int(phone_no)
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name



def hospitals():
	with st.form(key='hospitals_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Hospital')
		email=st.text_input('Please Enter Hospital Email')
		city =st.text_input('Please Enter Hospital city')
		zipcode=st.text_input('Please Enter Hospital city zipcode')
		phone_no=st.number_input('Please Enter Hospital Phone Number')
		phone_no=int(phone_no)
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name


def blood_request():
	with st.form(key='blood_request_form'):
		st.write("You selected Request_Processing.")
		st.write("Available .")
		requests_names_d={'Daneshwar G':['BLOOD_REPLACEMENT','A+',100,'587311'],'Sonali S':['PLASMA_REPLACEMENT','B+',100,'590008'],'Vinayak K':['PLASMA_REPLACEMENT','O-',200,'587311']}
		requests_names = st.selectbox('Please Choose Blood Group',('Daneshwar G', 'Sonali S', 'Vinayak K'))
		st.write('Blood type Needed',requests_names_d[f'{requests_names}'][0])
		st.write('Blood Group Needed',requests_names_d[f'{requests_names}'][1])
		st.write('Blood quantity Needed',requests_names_d[f'{requests_names}'][2])
		st.write("Blood quantity Available is.",1000)
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Request processed")
		pass


username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')
login_checkbox = st.sidebar.checkbox('Login')



if login_checkbox:
	# auth=authentication(username,password,blood_bank_name,blood_bank_location)
	# print(auth)

	# if auth==True:
	if username=='1' and password=='1':
		operation = st.sidebar.radio("Please Select type of operation:",('Deposit', 'Request_Processing'))
		if operation == 'Deposit':

			# st.write('You selected Deposit.')
			doners = st.sidebar.radio("Please Select An section",('Individual_Entry', 'Hospital_Entry','Donation_Camps_Entry'))

			if doners == 'Individual_Entry':
				# st.write('You selected Individual_Entry.')
				individual()
			elif doners == 'Hospital_Entry':
				st.write("You selected Hospital_Entry.")
				hospitals()
			elif doners == 'Donation_Camps_Entry':
				st.write("You selected Donation_Camps_Entry.")
				donation_camps()
			
		elif operation == 'Request_Processing':
			blood_request()



	else:
		st.write('Wrong Username or Password')