import streamlit as st
from member_directory_app import load_members

st.set_page_config(page_title="Members Demo")

st.title("Member List Demo")

members = load_members()

if members.empty:
    st.write("No member data available.")
else:
    st.dataframe(members)
