import streamlit as st

# Custom imports
from multipage import MultiPage
from pages import graphs, recommend_jobs, classify_jobs, aboutus

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("TUTOR")

# Add all your applications (pages) here
app.add_page("Data Insights", graphs.app)
app.add_page("Job Recommendation", recommend_jobs.app)
app.add_page("Classify Job", classify_jobs.app)
app.add_page("About Us", aboutus.app)



# The main app
app.run()

# test
# st.write("Hello World!")
