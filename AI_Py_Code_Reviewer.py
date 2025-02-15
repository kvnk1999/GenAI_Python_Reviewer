import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyCHGvCV_UsrQLx8EZrb58IQ9qqQEyRNcYI")

sys_prompt = """You are a helpful AI to review Python code and give 
                feedback on potential bugs along with suggestions for fixes. Maintain the output as Bug report (as Bold header), fixed code, explaination.
                Have all these 3 headings in BOLD format.
                Always include a helpful statement at the end saying that 
                'In case if your query is not resolved, feel free to click on this link:
                innomatics.in to get in touch with our mentor in a 1:1 zoom call"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("AI Python Code Reviewer")

user_input = st.text_area(label="Place your Python code here")

btn_click = st.button("Review")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)