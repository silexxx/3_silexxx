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
		zipcode=st.text_input('Please Enter the zipcode of New Bank location')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Records are saved")
		pass


def Update_Excisting_Bank():
	with st.form(key='Update_Excisting_Bank_form'):
		blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli','BANGALORE'))
		blood_bank_name_dict={'Belgaum':('KLE','JNMC'),'Hubli':('KIMS','LAKEVIEW'),'BANGALORE':('LAKEVIEW','APOLLO')}
		print(blood_bank_name_dict[f'{blood_bank_location}'])
		blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_name_dict[f'{blood_bank_location}'])
		st.write('Please Enter the Details to Update')
		name =st.text_input('Please Enter New Name of the  Bank')
		location=st.text_input('Please Enter New Location of the Bank')
		zipcode=st.text_input('Please Enter the New Bank location zipcode')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Records are saved")
		pass

def Assign_New_USER():
	with st.form(key='Assign_New_USER_form'):
		st.write('Please Enter the Details')
		blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli','BANGALORE'))
		blood_bank_name_dict={'Belgaum':('KLE','JNMC'),'Hubli':('KIMS','LAKEVIEW'),'BANGALORE':('LAKEVIEW','APOLLO')}
		print(blood_bank_name_dict[f'{blood_bank_location}'])
		blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_name_dict[f'{blood_bank_location}'])
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		username=st.text_input('Please Enter usename to be assigned')
		password=st.text_input('Please Enter password to be assigned')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Records are saved")
		pass



if login_checkbox:
	if username=='1' and password=='1':
		st.write('Logged In')
		operation = st.sidebar.radio("Please Select type of operation:",('Add_New_Bank', 'Update_Existing_Bank','Assign_New_USER'))
		if operation == 'Add_New_Bank':
			Add_New_Bank()
		elif operation == 'Update_Existing_Bank':
			Update_Excisting_Bank()

		elif operation == 'Assign_New_USER':
			Assign_New_USER()
			

else:
	st.write('Wrong Username or Password')