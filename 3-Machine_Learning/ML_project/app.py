import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# Text input
# user_input = st.text_input('Enter your name:', 'Type here')


option = st.selectbox(
    "Category",
    ("High", "Medium", "Low"))

# pred = model.predict(user_input)
# Display the user input
st.write(f'Hello, {option}!')