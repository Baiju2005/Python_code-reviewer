import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")


def review_code(code):
    prompt = f"Review this Python code for errors and provide corrections:\n\n{code}"
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


st.title("🤖 Python Code Reviewer")
st.write("Paste your Python code below, and the AI will review it.")

code_input = st.text_area("Enter Python code:", height=250)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            result = review_code(code_input)
        st.subheader("Review and Suggestions:")
        st.write(result)
    else:
        st.warning("Please enter some Python code.")

st.sidebar.header("About")
st.sidebar.info("This AI assistant uses Google Gemini to analyze and correct Python code.")