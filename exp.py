import streamlit as st

# Title of the web app
st.title("Job Eligibility Checker")

# Subheader
st.subheader("Check if you are eligible for the job")

# Take experience input from the user
exp = st.number_input("Enter your experience in years", min_value=0, step=1)

# Button to check eligibility
if st.button("Check Eligibility"):
    if exp > 5:
        st.success("🎉 Congratulations! You will get the job.")
    else:
        st.warning("❌ Sorry, you will not get the job.")
