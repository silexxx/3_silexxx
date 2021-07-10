import streamlit as st
import sqlite3 as lite 
import sys


def blood_request():
	with st.form(key='blood_request_form'):
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
		# ship_address=
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name




blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli'))
blood_bank_name = st.selectbox('Please Choose Blood Bank Name',('KLE','KIMS'))
blood_request


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