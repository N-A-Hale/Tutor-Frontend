import streamlit as st
import numpy as np
import pandas as pd

from pages.model_requests import job_class_api_request

def app():
    """
    Page shows all jobs for browsing through
    """
    st.markdown('''Are you looking for a new employee in the data science field?
                There are many different roles in the field of data science, and we
                can help you categorise what you're looking for!
             ''')
    st.write("You can choose one of the two options below")



    #placeholder is used so that the string isn't passed as the input and made
    #part of a api call
    input = st.text_area('Job Description', placeholder = 'Enter Job Description Here')
    if input:
        job_level_type = job_class_api_request(input)
        st.write(job_level_type)


    # Buttons reset the page after a user enters input so I had to default to a
    # single client input -JP
    # columns = st.columns(2)
    # if columns[0].button('Enter a Job Description'):
    #     temp = False

    # if not temp:

    #     st.write(f'{title} + 1', title)


    # if columns[1].button('Upload a Job Description'):
    #     st.set_option('deprecation.showfileUploaderEncoding', False)
    #     uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    #     if uploaded_file is not None:
    #         data = pd.read_csv(uploaded_file)
    #         st.write(data)
