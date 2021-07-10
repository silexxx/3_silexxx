import streamlit as st
import sqlite3 as lite 
import sys 


username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')

login_checkbox = st.sidebar.checkbox('Login')



def deposit_db(name,email,city,zipcode,blood_group,blood_quantity,blood_bank_location,blood_bank_name):
	# try:
	# 	con = lite.connect('blood_bank.db') 
	# 	cur = con.cursor()     
	# 	cur.execute(f'''INSERT INTO depositions(NAME,EMAIL,CITY,ZIPCODE,BLOOD_GROUP,BLOOD_QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME) VALUES (f'{name}', f'{email}', f'{city}', f'{zipcode}', f'{blood_group}',f'{blood_quantity}',f'{blood_bank_location}',f'{blood_bank_name}')''')
	# 	con.commit()

	# except Exception as e: 
	# 	if con: 
	# 		con.rollback() 

	# 	print("Unexpected error %s:" % e.args[0]) 
	# 	sys.exit(1) 
	# finally: 
	# 	if con: 
	# 		con.close()

	
	con = lite.connect('blood_bank.db') 
	cur = con.cursor()     
	cur.execute(f'''INSERT INTO depositions(NAME,EMAIL,CITY,ZIPCODE,BLOOD_GROUP,BLOOD_QUANTITY,BLOOD_BANK_LOCATION,BLOOD_BANK_NAME) VALUES (f'{name}', f'{email}', f'{city}', f'{zipcode}', f'{blood_group}',f'{blood_quantity}',f'{blood_bank_location}',f'{blood_bank_name}')''')
	con.commit()

	




def individual():
	with st.form(key='individual_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.number_input('Please Enter Phone Number')
		phone_no=int(phone_no)
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		temp=deposit_db(name,email,city,zipcode,blood_group,blood_quantity,blood_bank_location,blood_bank_name)
		print(temp)
		st.write("records are saved")
		return  name,email,city,zipcode,blood_group,blood_quantity

def donation_camps():
	with st.form(key='donation_camps_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Institute')
		email=st.text_input('Please Enter Institute Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.number_input('Please Enter Phone Number')
		phone_no=int(phone_no)
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("records are saved")
		return  name,email,city,zipcode,blood_group,blood_quantity


def hospitals():
	with st.form(key='hospitals_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of Hospital')
		email=st.text_input('Please Enter Hospital Email')
		city =st.text_input('Please Enter Hospital city')
		zipcode=st.text_input('Please Enter Hospital city zipcode')
		phone_no=st.number_input('Please Enter Hospital Phone Number')
		phone_no=int(phone_no)
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("records are saved")
		return  name,email,city,zipcode,blood_group,blood_quantity



if login_checkbox:
	if username=='1' and password=='1':
		st.write('Logged In')

		blood_bank_location = st.sidebar.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli'))

		blood_bank_name = st.sidebar.selectbox('Please Choose Blood Bank Name',('KLE','KIMS'))


		operation = st.sidebar.radio("Please Select type of operation:",('Deposit', 'Request_Processing'))
		if operation == 'Deposit':

			st.write('You selected Deposit.')
			doners = st.sidebar.radio("Please Select An section",('Individual_Entry', 'Hospital_Entry','Donation_Camps_Entry'))

			if doners == 'Individual_Entry':
				st.write('You selected Individual_Entry.')
				individual()
			elif doners == 'Hospital_Entry':
				st.write("You selected Hospital_Entry.")
				hospitals()
			elif doners == 'Donation_Camps_Entry':
				st.write("You selected Donation_Camps_Entry.")
				donation_camps()
			
		elif operation == 'Request_Processing':
			st.write("You selected Request_Processing.")




		





else:
	st.write('Wrong Username or Password')