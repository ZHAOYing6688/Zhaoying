import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = os.path.join("static", "docs", "resume.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="Jane_Doe_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("Jane Doe")

    st.header("Contact Information")
    st.markdown("""
    - **Email:** 13381390371@163.com
    - **Phone:** 13381390371
    - **GitHub:** (https://github.com/ZHAOYing6688/Zhaoying)
    - **Address:** 123 Main St, Anytown, Hongkong
    """)

    st.header("Professional Summary")
    st.markdown("""
    Highly skilled Marketer with over 5 years of experience in Learning in Business School.
    """)

    st.header("Education")
    st.markdown("""
    **Bachelor of Marketing**
    - Renmin University of China
    - *Graduated: June 2024*
    - GPA: 3.8/4.0
    """)

    st.header("Skills")
    st.markdown("""
    - **Programming Languages:** Python, JavaScript, Java, C++
    - **Web Technologies:** HTML, CSS, React, Node.js, Django
    - **Soft Skills:** Team Leadership, Project Management, Problem-Solving, Communication
    """)


    st.header("Projects")
    st.markdown("""
    **E-commerce Website**
    - Developed a full-stack e-commerce application using React and Django.
    - Integrated payment gateways and implemented user authentication.

    **Data Analysis Tool**
    - Created a Python-based tool for analyzing large datasets and visualizing results.
    - Used pandas and matplotlib libraries for data manipulation and plotting.
    """)

    st.header("Languages")
    st.markdown("""
    - **English:** Native
    """)

    st.header("Interests")
    st.markdown("""
    - Open-source contributions
    - Blogging about delicious food
    - Traveling and shopping
    """)

    st.markdown("---") 