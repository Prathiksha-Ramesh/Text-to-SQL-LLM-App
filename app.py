import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
import sqlite3
import google.generativeai as genai
#configure api key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


#function to load google gemini model and provide the sql query as response:

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#funtion to retrieve the query from the sql database:
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#prompt:

prompt=[
    """
you are an expert in converting english questions to sql query!
the sql database has the name student and has the following columns-name,class,section
for example,\n example1 - how many entries of records are present?,
the sql command will be something like this SELECT COUNT(*) FROM STUDENT;
\n example 2 - tell me all the students studying in data science class?,
the sql command will be something like this SELECT * FROM STUDENT where CLASS='Data science;
also the sql code should not have ``` beginning or end and sql word in output"""
]


st.set_page_config(page_title='I can retrieve sql query')
st.header('Gemini App to retrieve SQL Data')
question=st.text_input('Input:',key='input')
submit=st.button('Ask the question')

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,'student.db')
    st.subheader('The Response is ')
    for row in data:
        print(row)
        st.header(row)
