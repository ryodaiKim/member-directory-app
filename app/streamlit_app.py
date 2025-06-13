"""Streamlit interface for the member directory."""

import streamlit as st
from member_directory_app import load_members

st.set_page_config(page_title="Member Directory")
st.title("\U0001F4D8 Member Directory")

# Load data
members = load_members()

if members.empty:
    st.info("No member data found.")
else:
    name_query = st.text_input("Search by name")
    department_options = ["All"] + sorted(members["Department"].unique().tolist())
    department = st.selectbox("Filter by department", department_options)

    filtered = members.copy()
    if name_query:
        filtered = filtered[filtered["Name"].str.contains(name_query, case=False, na=False)]
    if department != "All":
        filtered = filtered[filtered["Department"] == department]

    st.subheader(f"Members ({len(filtered)})")
    if filtered.empty:
        st.write("No matching members.")
    else:
        for _, row in filtered.iterrows():
            with st.expander(row["Name"]):
                st.write(f"**Department:** {row['Department']}")
                st.write(f"**Email:** {row['Email']}")
