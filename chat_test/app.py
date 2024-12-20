from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro Model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title= "Q&A Demo")

st.header("Gemini LLM Application")

input= st.text_input("Input: " , key= "Input")
submit= st.button("Ask the question")

## WHEN SUBMIT IS CLICKED

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is: ")
    st.write(response)
