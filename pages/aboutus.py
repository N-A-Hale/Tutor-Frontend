import streamlit as st
from PIL import Image


def app():

    st.markdown('''### About Us''')
    st.markdown('''
                Hey there! We are three data science enthusiasts from the US and Australia.
                We virtually got together and created this page as our LeWagon Bootcamp project.''')

    st.image(Image.open('images/group_photo.png'))

    st.markdown('''We definitely had a great time learning about data science, working as a team, and building
                this website from just an idea while browsing through job listings! Oh who doesn't love
                data cleaning and long long nights!

                We would like to thank all the teachers and TAs at LeWagon for the help, patience and supports
                throughout the course. We sure will miss raising tickets for help.
                ''')
