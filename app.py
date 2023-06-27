import streamlit as st 
import openai  
import ast 
import json

import prompts  
import gpt

openai.api_key = st.secrets['OPENAI_API_KEY'] 

def blank(): return st.text('')


st.set_page_config(layout="wide")  

password = st.sidebar.text_input("Password")  
if password.lower().strip() == st.secrets['PASSWORD']: 
    valid_user = True 
else: 
    valid_user = False


st.subheader("Promo Parsing") 
if valid_user: 
    st.success("password accepted") 
else: 
    st.warning("invalid password") 

blank()  



with st.form(key='f'):   

    c1, c2 = st.columns(2)
    monthly_rate = c1.number_input("Monthly Rate", value=100)
    promo_string = c2.text_input("Promo String")
    
    p = st.text_area("GPT Instructions", value=prompts.promo_string) 

    temperature = st.slider("Temperature", 
                            help="Higher temperature means more random/creative output. Lower temperature means more predictable/stable output.",
                            min_value=0.0, 
                            max_value=1.0, 
                            value=0.5, 
                            step=0.01, 
                            key='temp')  
    
    blank()
    go = st.form_submit_button("Go") 

if go:    
    blank()
    if valid_user:

        with st.spinner("Thinking..."): 
            bot = gpt.ai(None, system_prompt=p) 

            bot_input = "Input: " + f"(${str(monthly_rate)}, {promo_string})" + "\n\n" + "Output:"
            res = bot.answer(bot_input, temperature=temperature)  
            
            try: 
                #res = ast.literal_eval(res)  
                res = json.loads(res)
                st.json(res)
            except: 
                st.write(res)
    else: 
        st.warning("Please input valid passowrd in the sidebar")

