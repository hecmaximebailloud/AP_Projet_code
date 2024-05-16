import streamlit as st

st.title("Streamlit App with Code Display")

st.header("Displaying Python Code")

# Use st.echo to show the code and execute it
st.subheader("Using st.echo")
with st.echo():
    st.write("This block of code is both shown and executed.")
    st.write("Streamlit makes it easy to create interactive apps.")
