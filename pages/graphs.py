import streamlit as st
from PIL import Image
# import numpy as np
# import pandas as pd
# from data_scientist_skills.data import get_data

def app():
    """
    Page shows all jobs for browsing through
    """
    # @st.cache
    # def get_cached_data():
    #     return get_data()

    # st.markdown('''
    #         Welcome to Data2$$$ Job Search - a job search engine curated for the Data Science Field.

    #          We have thousands of job listings available, so have a look!
    #          ''')
    # ['job_title', 'salary_estimate', 'job_description', 'rating',
    #    'company_name', 'location', 'headquarters', 'size', 'founded',
    #    'type_of_ownership', 'industry', 'sector', 'cleaned_description',
    #    'cleaned_title']
    # st.dataframe(get_cached_data()[['job_title','company_name','location','industry','job_description'
    #                                 ]])

    st.markdown('''
                #### Welcome to TUTOR - a website curated for job seekers and recruiters in the data science field!
                ''')
    st.info('''Below are some graphical representation of the jobs available on our website!
                Have a look!''')

    st.write("This is where our jobs come from!")
    locations = Image.open("images/map.png")
    st.image(locations)

    st.markdown('''Data Science is sought after in many different industries!
                You can see the amount of jobs per title per industry''')
    locations = Image.open("images/spiderplot.png")
    st.image(locations)

    st.markdown('''This shows the range of salary across different sectors!''')
    locations = Image.open("images/SalaryVsSector.png")
    st.image(locations)
