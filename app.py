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



genre = st.radio("What's your favorite movie genre",('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
	st.write('You selected comedy.')
else:
	st.write("You didn't select comedy.")


if login_checkbox:
	if username=='1' and password=='1':
		st.write('Logged In')

		st.write('Please Select ')


		individual_checkbox = st.sidebar.checkbox('Individual Data')
		if individual_checkbox:
			individual()

		individual_checkbox = st.sidebar.checkbox('Individual Data')
		if individual_checkbox:
			individual()






else:
	st.write('Wrong Username or Password')