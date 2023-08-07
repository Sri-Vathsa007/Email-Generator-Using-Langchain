import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def get_llm_response(form_input,email_sender,email_receiver,email_style):

    llm = CTransformers(model="models/llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama", config={"max_new_tokens":256, "temperature":0.01})

    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:

    
    """
    
    prompt = PromptTemplate(input_variables=["style","email_topic","sender","recipient"],template=template)
    response = llm(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_receiver,style=email_style))

    return response


st.set_page_config(page_title="Generate Emails", page_icon="📧", layout="centered",initial_sidebar_state="collapsed")

st.header("Generate Email 📧")

form_input = st.text_area("Enter the email topic", height=275)

sender_col, receiver_col, email_style_col = st.columns([10,10,5])

with sender_col:
    email_sender = st.text_input("Sender name")
with receiver_col:
    email_receiver = st.text_input("Receiver name")
with email_style_col:
    email_style = st.selectbox("Writing Style", ("Formal","Appreciating", "Not Satisfied", "Neutral"), index=0)

submit = st.button("Generate")

if submit:
    st.write(get_llm_response(form_input,email_sender,email_receiver,email_style))

