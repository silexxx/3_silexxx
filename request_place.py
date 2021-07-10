import streamlit as st
import sqlite3 as lite 
import sys
import datetime

st.title("Blood Request Portal")


def requestplace_db(recordList):
	try:
		con = lite.connect('blood_bank.db') 
		cur = con.cursor()     
		sqlite_insert_query='''INSERT INTO BloodRequests(NAME ,EMAIL ,CITY ,ZIPCODE ,PHONENO ,BLOOD_GROUP ,BLOOD_TYPE , BLOOD_QUANTITY ,EXPIRY_DATE ,BLOOD_BANK_LOCATION ,BLOOD_BANK_NAME ,SHIP_ADDRESS) VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?);'''
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


def blood_request():
	with st.form(key='blood_request_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		phone_no=st.text_input('Please Enter Phone Number')
		blood_group = st.selectbox('Please Choose Blood Group',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		type_of_blood=st.selectbox('Please Choose type ',('BLOOD_REPLACEMENT', 'PLASMA_REPLACEMENT'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		blood_quantity=int(blood_quantity)
		expiry_date=st.date_input("Till When do you want this request to be fulfilled",datetime.date(2020, 7, 10))
		ship_address=st.text_input('Please Enter Ship Address')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		global blood_bank_location,blood_bank_name
		recordList=[(name,email,city,zipcode,phone_no,blood_group,type_of_blood,blood_quantity,expiry_date,blood_bank_location,blood_bank_name,ship_address)]
		requestplace_db(recordList)
		st.write("Request is submitted")





blood_bank_location = st.selectbox('Please Choose Blood Bank location',('Belgaum','Hubli','BANGALORE'))
print(blood_bank_location)
blood_bank_name_dict={'Belgaum':('KLE','JNMC'),'Hubli':('KIMS','LAKEVIEW'),'BANGALORE':('LAKEVIEW','APOLLO')}
print(blood_bank_name_dict[f'{blood_bank_location}'])
blood_bank_name = st.selectbox('Please Choose Blood Bank Name',blood_bank_name_dict[f'{blood_bank_location}'])
blood_request()
