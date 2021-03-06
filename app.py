import streamlit as st
import sqlite3 as lite 
import sys
from PIL import Image
image = Image.open('logo.jpg')

st.sidebar.title('-------------Ray-------------')
st.sidebar.image(image, caption='')

st.title("Blood Bank Deposit and Process Portal")

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
	# print(location)
	blood_bank_names_list=[]
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''select distinct BLOOD_BANK_NAME from BloodBanks where BLOOD_BANK_LOCATION='{location}' ''')
		con.commit()
		rows = cur.fetchall()
		# print(rows)

		for i in rows:
			blood_bank_names_list.append(i[0])
			# print(i[0])
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
	# print(name,passs,bank_name,bank_location)
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()     
		cur.execute(f''' select  *  from usernames WHERE USERA='{name}' and PASSA='{passs}' and BLOOD_BANK_LOCATION='{bank_name}' and BLOOD_BANK_NAME='{bank_location}' ''')
		con.commit()
		rows = cur.fetchall()
		# print(rows)

		if  len(rows) == 0:
			return False
		else:
			return True

		for row in rows:
			pass
			# print(row)
		return row

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()


def blood_quantity_available(BLOOD_BANK_NAMEe,BLOOD_BANK_LOCATIONe,Blood_type_requested,Blood_Group_requested):
	print(BLOOD_BANK_NAMEe,BLOOD_BANK_LOCATIONe,Blood_Group_requested,Blood_type_requested)
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''SELECT sum(BLOOD_QUANTITY) FROM depositions WHERE BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATIONe}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAMEe}' AND BLOOD_TYPE='{Blood_type_requested}' AND BLOOD_GROUP='{Blood_Group_requested}' ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)
		print(rows[0][0])
		return rows[0][0]


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
		sqlite_insert_query='''INSERT INTO depositions(NAME,EMAIL,CITY,ZIPCODE,PHONENO,BLOOD_TYPE,BLOOD_GROUP,BLOOD_QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME) VALUES (?, ?, ?, ?, ?,?,?,?,?,?);'''
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
		phone_no=st.text_input('Please Enter Phone Number')
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,type_of_blood,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,type_of_blood,blood_group,blood_quantity,blood_bank_location,blood_bank_name

def donation_camps():
	with st.form(key='donation_camps_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Institute')
		email=st.text_input('Please Enter Institute Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,type_of_blood,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,type_of_blood,blood_group,blood_quantity,blood_bank_location,blood_bank_name



def hospitals():
	with st.form(key='hospitals_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Hospital')
		email=st.text_input('Please Enter Hospital Email')
		city =st.text_input('Please Enter Hospital city')
		zipcode=st.text_input('Please Enter Hospital city zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,type_of_blood,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,type_of_blood,blood_quantity,blood_bank_location,blood_bank_name

def requests_names(blood_bank_namesr,blood_bank_locationsr):
	requests_names_list=[]
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''SELECT NAME FROM BloodRequests WHERE BLOOD_BANK_LOCATION='{blood_bank_locationsr}' AND BLOOD_BANK_NAME='{blood_bank_namesr}' order by EXPIRY_DATE ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)
		for i in rows:
			print(i[0])
			requests_names_list.append(i[0])
		return requests_names_list

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()

def request_details(NAME,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME):
	requests_names_list=[]
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''SELECT BLOOD_GROUP,BLOOD_TYPE,BLOOD_QUANTITY FROM BloodRequests WHERE NAME='{NAME}' AND BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATION}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAME}' AND EXPIRY_DATE < DATE(CURRENT_TIMESTAMP) order by EXPIRY_DATE; ''')
		con.commit()
		rows = cur.fetchall()
		print(rows)
		for i in rows:
			return i[0],i[1],i[2]

	except Exception as e: 
		if con: 
			con.rollback() 

		print("Unexpected error %s:" % e.args[0]) 
		sys.exit(1) 
	finally: 
		if con: 
			con.close()


def aggregation_fetch(QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME):
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''select ID,BLOOD_QUANTITY  FROM depositions WHERE BLOOD_QUANTITY >= {QUANTITY} and BLOOD_BANK_LOCATION='{BLOOD_BANK_LOCATION}' AND BLOOD_BANK_NAME='{BLOOD_BANK_NAME}' ORDER BY BLOOD_QUANTITY DESC LIMIT 1 ''')
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

def aggregation_update(ids,quantity):
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f'''UPDATE depositions SET BLOOD_QUANTITY='{quantity}' where ID='{ids}' ''')
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


def delete_request(requests_namess,Blood_type_requested,Blood_Group_requested,blood_bank_location,blood_bank_name):
	print(requests_namess,Blood_type_requested,Blood_Group_requested,blood_bank_location,blood_bank_name)
	try:
		con = lite.connect('blood_bank.db')
		cur = con.cursor()
		cur.execute(f''' DELETE FROM BloodRequests WHERE Name='{requests_namess}' AND BLOOD_TYPE='{Blood_type_requested}' AND BLOOD_GROUP='{Blood_Group_requested}' AND BLOOD_BANK_LOCATION='{blood_bank_location}' AND BLOOD_BANK_NAME='{blood_bank_name}'   ; ''')
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

def blood_request():
	global blood_bank_name,blood_bank_location
	# blood_quantity_plasma=blood_quantity_available(blood_bank_name,blood_bank_location,'BLOOD_REPLACEMENT')
	# blood_quantity_replacement=blood_quantity_available(blood_bank_name,blood_bank_location,'BLOOD_REPLACEMENT')
	# st.write("Blood plasma quantity Available is.",blood_quantity_plasma)
	# st.write("Blood replacement quantity Available is.",blood_quantity_replacement)
	
	list_names=requests_names(blood_bank_name,blood_bank_location)
	list_names=tuple(list_names)
	print(list_names)
	requests_namess = st.selectbox('Please Choose request to process',list_names)
	Blood_Group_requested,Blood_type_requested,Blood_quantity_requested=request_details(requests_namess,blood_bank_location,blood_bank_name)
	st.write('Blood type Needed',Blood_type_requested)
	st.write('Blood Group Needed',Blood_Group_requested)
	st.write('Blood quantity Needed',Blood_quantity_requested)
	blood_quantity_av=blood_quantity_available(blood_bank_name,blood_bank_location,Blood_type_requested,Blood_Group_requested)
	st.write("Blood quantity Available is.",blood_quantity_av)
	blood_quantity=st.number_input('Please Enter blood_quantity in ml')
	blood_quantity=int(blood_quantity)
	submit_button = st.button(label='Submit')

	if submit_button:
		fetched_ID,fetched_quantity=aggregation_fetch(blood_quantity,blood_bank_location,blood_bank_name)
		print(fetched_ID,fetched_quantity)
		r_quantity=fetched_quantity-blood_quantity
		print(r_quantity)
		aggregation_update(fetched_ID,r_quantity)
		delete_request(requests_namess,Blood_type_requested,Blood_Group_requested,blood_bank_location,blood_bank_name)
		st.write("Request processed")
		


username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')
login_checkbox = st.sidebar.checkbox('Login')



if login_checkbox:
	# auth=authentication(username,password,blood_bank_name,blood_bank_location)
	# print(auth)

	# if auth==True:
	if username=='admin' and password=='admin@123':
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