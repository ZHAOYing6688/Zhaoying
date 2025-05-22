import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="personalsite", layout="wide")

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.contact import contact_page

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.sidebar.markdown("## Main Menu")
        app = st.sidebar.radio(
            "Navigation", self.apps, format_func=lambda app: app["title"]
        )
        st.sidebar.markdown("---")
        app["function"]()

# Initialize the app
app = MultiApp()

# Add pages to the app
app.add_app("Home", home_page)  # Add this line
app.add_app("Education", education_page)
app.add_app("Experience", experience_page)
app.add_app("Contact", contact_page)

# Run the app
app.run()
