import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Text input
# user_input = st.text_input('Enter your name:', 'Type here')


option = st.selectbox(
    "Category",
    ("High", "Medium", "Low", "None"))

# pred = model.predict(user_input)
# Display the user input
st.write(f'Hello, {option}!')

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
col4.metric("Paula", "80%", "10%")