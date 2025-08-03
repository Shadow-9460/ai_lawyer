import streamlit as st

upload_file = st.file_uploader("Upload PDF",
                               type="pdf",
                               accept_multiple_files=False)

user_query = st.text_area("Enter Your Prompt",height=150,placeholder="Ask Anything")

ask_question = st.button("Ask AI Lawyer")

if ask_question:
    if uploaded_file:
        st.chat_message("user").write(user_query)

    fixed_response = "Hii, this is a fixed response!"
    st.chat_message("AI Lawyer").write("Hii, this is a fixed response!")

else:
    st.error("Kindly Upload a valid file for Bteer response")
    