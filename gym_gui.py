import streamlit as st

from gymview import GymMemberManager

gym_instance=GymMemberManager()
tab1,tab2=st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add New Gym Member")
    name=st.text_input("Name of the Applicant")
    place=st.text_input("Current City")
    mobile=st.text_input("Contact Info")
    plan=st.text_input("Membership Plan")
    fee=st.selectbox("Membership fees",["1 month","3 month","6 month"])
    joined_date=st.date_input("Joining Date(yyyy/mm/dd")
    if st.button("Registration Complete"):
        gym_instance.post(name=name,place=place,mobile=mobile,plan=plan,fee=fee,joined_date=joined_date)
        st.success("Gym Membership Completed")
with tab2:
    st.title("View Gym Memeber Details")
    records=gym_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("Record not found")


