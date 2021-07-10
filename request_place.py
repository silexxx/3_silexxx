import streamlit as st
import sqlite3 as lite 
import sys
import datetime


def blood_request():
	with st.form(key='blood_request_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		# phone_no=int(phone_no)
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		expiry_date=st.date_input("Till When do you want this request to be fulfilled",datetime.date(2020, 7, 10))
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("Request is submitted")
		pass
		# global blood_bank_location,blood_bank_name
		# recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		# deposit_db(recordList)
		# st.write("Records are saved")
		# return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name




blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli','BANGALORE'))
print(blood_bank_location)
blood_bank_name_dict={'Belgaum':('KLE','JNMC'),'Hubli':('KIMS','LAKEVIEW'),'BANGALORE':('LAKEVIEW','APOLLO')}
print(blood_bank_name_dict[f'{blood_bank_location}'])
blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_name_dict[f'{blood_bank_location}'])
blood_request()