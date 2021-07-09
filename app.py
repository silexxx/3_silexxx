import streamlit as st


username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password')

login_checkbox = st.sidebar.checkbox('Login')




def individual():
	with st.form(key='my_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		blood_group = st.selectbox('Please Choose Blood Group?',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("records are saved")
		return  name,email,city,zipcode,blood_group,blood_quantity

def donation_camps():
	with st.form(key='my_form'):
		st.write('Please Enter the Details')
		name =st.text_input('Please Enter Name')
		email=st.text_input('Please Enter Email')
		city =st.text_input('Please Enter city')
		zipcode=st.text_input('Please Enter zipcode')
		blood_group = st.selectbox('Please Choose Blood Group?',('A+', 'A-', 'B+','B-','AB+','AB-','O+','O-'))
		blood_quantity=st.number_input('Please Enter blood_quantity in ml')
		submit_button = st.form_submit_button(label='Submit')

	if submit_button:
		st.write("records are saved")
		return  name,email,city,zipcode,blood_group,blood_quantity




if login_checkbox:
	if username=='1' and password=='1':
		st.write('Logged In')


		operation = st.sidebar.radio("Please Select type of operation:",('Deposit', 'Request_Processing'))
		if operation == 'Deposit':

			st.write('You selected Deposit.')
			doners = st.sidebar.radio("Please Select An section",('Individual_Entry', 'Hospital_Entry','Donation_Camps_Entry'))

			if doners == 'Individual_Entry':
				st.write('You selected Individual_Entry.')
				individual()
			elif doners == 'Individual_Entry':
				st.write("You selected Hospital_Entry.")
			elif doners == 'Donation_Camps_Entry':
				st.write("You selected Donation_Camps_Entry.")
				donation_camps()
			
		elif operation == 'Request_Processing':
			st.write("You selected Request_Processing.")




		





else:
	st.write('Wrong Username or Password')