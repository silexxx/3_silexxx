import streamlit as st
import sqlite3 as lite 
import sys 


username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')

login_checkbox = st.sidebar.checkbox('Login')



def Add_New_Bank():
	with st.form(key='Add_New_Bank_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name of the New Bank')
		location=st.text_input('Please Enter Location of the New Bank')
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
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name

if login_checkbox:
	if username=='1' and password=='1':
		st.write('Logged In')

		operation = st.sidebar.radio("Please Select type of operation:",('Add_New_Bank', 'Update_Existing_Bank','Assign_New_USER'))

		

		blood_bank_location = st.text_input('Please Enter New Bank Location')
		blood_bank_name = t.text_input('Please Enter New Bank Name')


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