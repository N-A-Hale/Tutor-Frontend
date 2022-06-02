import streamlit as st
import numpy as np
import pandas as pd

from pages.model_requests import jobs_rec_api_request

def fix_titles(df):
    """Formats the columns to standardized titles"""
    new_col ={col: col.replace('_', ' ').title() for col in df.columns}
    return df.rename(columns = new_col)




def app():
    """
    Page shows all jobs for browsing through
    """

    st.write('''We can provide you with a number of jobs that are best suited to your skills.
             Please tell us a bit about yourself and your experience!''')
    st.write('''Please tick the boxes below to describe your skills.''')

    # List of skills
    skill_list = ['Excellent Communication Skills', 'create', 'Data Analysis', 'develop',
                'development', 'Data Engineering', 'information', 'Project Management',
                'ML Model Build', 'Python Programming', 'science', 'software', 'SQL', 'systems']


    # User input and data collection
    input_collector = {}
    columns = st.columns(2)

    for skill in skill_list[:7]:
        if columns[0].checkbox(skill):
            input_collector[skill] = 1
        else:
            input_collector[skill] = 0

    for skill in skill_list[7:]:
        if columns[1].checkbox(skill):
            input_collector[skill] = 1
        else:
            input_collector[skill] = 0

    st.slider('Years of Experience in Data Science',0, 20, 5)

    if st.checkbox("Happy with your descriptions above?"):
        if sum(input_collector.values()) > 0:
            st.success('Below are the top 5 jobs that we recommend you to apply!')

            #Returns pd.DataFrame from the model, can be manipulated as desired
            answer = jobs_rec_api_request(input_collector, skill_list)

            #Uses fix title formatting of chosen columns
            answer = fix_titles(answer[['job_title','job_description',
                             'company_name','location']])

            #Prints tables of each job posting that matches presented skills
            for index in range(len(answer)):
                st.table(answer.iloc[index])

        else:
            st.info('Would you be interested in some data science courses to improve your skill set?')
