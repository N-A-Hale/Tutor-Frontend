from lib2to3.pgen2.literals import test
from operator import mod
from pydoc import cli
from multimethod import RETURN
# from pages.recommend_jobs import skill_list ### just has to be copied and pasted for now
import pandas as pd
import requests
import json

top_keywords = ['communication', 'create', 'data data', 'develop', 'development',
                'engineer', 'information', 'management', 'model', 'python',
                'science', 'software', 'sql', 'systems',
]
skill_list = ['Excellent Communication Skills', 'create', 'Data Analysis', 'develop',
                'development', 'Data Engineering', 'information', 'Project Management',
                'ML Model Build', 'Python Programming', 'science', 'software', 'SQL', 'systems']


test_push = {'possessed_skills': {'communication': [0],
  'create': [False],
  'data data': [0],
  'develop': [0],
  'development': [0],
  'engineer': [0],
  'information': [0],
  'management': [0],
  'model': [0],
  'python': [0],
  'science': [0],
  'software': [0],
  'sql': [0],
  'systems': [0]}}



def jobs_rec_api_request(client_skills):
    keyword_skills = {}
    for i in range(len(skill_list)):
        keyword_skills[top_keywords[i]] = client_skills[skill_list[i]]
        keyword_skills[top_keywords[i]] = [keyword_skills[top_keywords[i]]]
    # mod_skills = {'possessed_skills' : keyword_skills}
    mod_skills = keyword_skills
    response = requests.post('https://dssapi-yjgqjabz6a-ew.a.run.app/models/skills_model', json = test_push)
    return response
    # return mod_skills

def job_class_api_request(job_description):
    # # response = requests.post(
        # 'https://dssapi-yjgqjabz6a-ew.a.run.app/models/job_classifier_model',\
            # json = client_skills)
    #parsed_response = json.read
    #return
    pass
