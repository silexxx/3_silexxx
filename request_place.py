import streamlit as st
import sqlite3 as lite 
import sys


def blood_request():
	with st.form(key='blood_request_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.number_input('Please Enter Phone Number')
		phone_no=int(phone_no)
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name)]
		deposit_db(recordList)
		st.write("Records are saved")
		return  name,email,city,zipcode,phone_no,blood_group,blood_quantity,blood_bank_location,blood_bank_name




blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli'))
blood_bank_name = st.selectbox('Please Choose Blood Bank Name',('KLE','KIMS'))
blood_request()
