from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY") )

## FUNCTION TO LOAD GEMINI PRO MODEL AND GET REPONSE

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[])

chat.send_message("Hi")

def get_gemini_response(question):
    # res1= chat.
    respones = chat.send_message(question)
    
    return respones

## INITIALIZE OUT STREAMLIT APP

st.set_page_config( page_title = "Q&A Demo")

st.header( "Gemini LL Application part2 ")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]
    
input = st.text_input( "Input:" , key =" Input")

submit = st.button("Ask the question")

if input and submit:
    response = get_gemini_response(input)
    ## add user query and response to session chat history
    
    st.session_state["chat_history"].append(("YOU: ",input))
    st.subheader("The response is :")
    for chunk in response :
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Bot: ",chunk.text))
        
st.subheader("The Chat History is : ")

for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")