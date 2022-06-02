from lib2to3.pgen2.literals import test
from operator import mod
from pydoc import cli
# from multimethod import RETURN
import pandas as pd
import requests
import json

### Needs to match the order of the values in recommend_jobs.py's skill_list
### commented and copied below for refernce -JP
top_keywords = ['communication', 'create', 'data data', 'develop', 'development',
                'engineer', 'information', 'management', 'model', 'python',
                'science', 'software', 'sql', 'systems',
]
# skill_list = ['Excellent Communication Skills', 'create', 'Data Analysis', 'develop',
#                 'development', 'Data Engineering', 'information', 'Project Management',
#                 'ML Model Build', 'Python Programming', 'science', 'software', 'SQL', 'systems']


def jobs_rec_api_request(client_skills, skill_list):
    """Takes the client_skills dictionary input and the skill_list and returns
    the processed api response. Skills are transformed back to top keywords that
    the model was trained on."""

    # Creates a dictionary with the appropriate keywords for the model while
    # keeping the user's values
    keyword_skills = {}
    for i in range(len(skill_list)):
        keyword_skills[top_keywords[i]] = client_skills[skill_list[i]]
        keyword_skills[top_keywords[i]] = [keyword_skills[top_keywords[i]]]

    #reshapes the dictionary for the api
    mod_skills = {'possessed_skills' : keyword_skills}

    #makes the api post request
    response = requests.post(
        'https://dssapi-yjgqjabz6a-ew.a.run.app/models/skills_model',
        json = mod_skills)

    #interprets the text response from the api as a python object (dictionary)
    response_dict = json.loads(response.text)

    #returns the pandas interpreted json-like text value stored at the
    #'recommendations' key
    return pd.read_json(response_dict['recommendations'])


def job_class_api_request(job_description):

    #prepares the job_description for the api
    mod_job_description = {'description' : job_description}

    #makes the post request
    response = requests.post(
        'https://dssapi-yjgqjabz6a-ew.a.run.app/models/job_classifier_model',\
            json = mod_job_description)

    #interprets the text response from the api as a python object (dictionary)
    response_dict = json.loads(response.text)

    #returns the dictionary with the model prediction
    return response_dict
