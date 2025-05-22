import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>Alina ZHAO</h4>
        <p>Recent Master's Graduate in Marketing<br>
        Chinese University of Hong Kong<br>
        12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
        <a href="mailto:sarah.13381390371@163.com">sarah.13381390371@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "img.jpeg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a marketing professional with a Master's degree in Marketing from The Chinese University of Hong Kong, specializing in big data strategies.

        I am skilled in using tools like SPSS and Python, and I thrive in collaborative environments.

        I aim to leverage my analytical skills and creativity to drive successful marketing initiatives.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Communication: Presentation Skills, Technical Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page