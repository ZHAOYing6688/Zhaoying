import streamlit as st
# Remove this import
# from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Market research intern
    **Omnicom Media Group.** | *Dec 2024 - Feb 2025*
  
    - Participated in the preliminary research for Xiaohongshu's (XHS) entry into the Hong Kong market, conducting SWOT 
     and other market analyses
    - Contributed to data collection and organization, analyzing first-hand data using methods such as LDA and K-means. 
     Provided actionable recommendations for Xiaohongshu's market entry strategy in Hong Kong
    """)
    
    st.markdown("""
    ### Film Marketing Intern
    **iQIYI** | *Apr. 2023 - Sept. 2024*
   
    - Contributed to the development of the pre-release marketing strategy for the animated film Master Zhong, defining the film's
     one and designing various marketing activities concerning characters, topics, and boundary-breaking promotions
    - Managed the official Sina Weibo account for the film Raid On the Lethal Zone, creating hashtags, writing copy, and creative
     videos; achieved an increase of 29,000 followers and 155,000 interactions (shares, comments, and likes); assisted in
     organizing the film's premiere event in Beijing, coordinating with 30+ staff members
    - Supported market research on a film proposal; utilized SWOT analysis to identify the target audience for dialect-based films
     and compared market positioning with similar topics, contributing insights for the film's initial positioning
    - Gathered marketing data for 20 films using the Maoyan APP, including trending keywords, popularity on Weibo and Tiktok
     during specific periods, and public opinions, to support the development of new media operational strategies and adjustments
     to future marketing directions
    """)
    
    st.markdown("""
    ### Marketing Development Intern
    **Harper's BAZAAR** | *Jan 2023 - Apr. 2024*
    
    - Produced the brand book of Ba&sh for the organizer’s review to help it gain admission to the Shenzhen Fashion Week
    - Integrated 5 proposals of national fashion weeks from 2019 to 2023 to analyze how they were held and how they conducted
      industry linkage with the government, producing a 10-page case book for Shenzhen Fashion Week, including brand
      introduction, haute couture show, and opening ceremony, which was directly adopted by the leader and put into use
    - Collaborated on planning the Coffee Market for the Bay Garden of Shenzhen MixC Shopping Mall and writing the
      marketing plan; collected coffee-related crossover marketing cases, focusing on their final implementation; provided ideas
      about color matching and photo spot design, which were directly adopted, and prepared the layout of related materials
    - Developed a landing proposal for BAZAAR Coffee, including ideas like environmental protection and themed activities
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Customer Segmentation Analysis",
            "description": "Used K-means clustering to segment customers based on purchasing behavior.",
            "skills": ["Python", "scikit-learn", "Pandas", "Matplotlib"],
            "outcome": "Identified 5 distinct customer segments that informed targeted marketing campaigns."
        },
        {
            "title": "Predictive Maintenance System",
            "description": "Developed a model to predict equipment failures before they occur.",
            "skills": ["Python", "TensorFlow", "Time Series Analysis", "IoT"],
            "outcome": "Reduced downtime by 23% and maintenance costs by 15%."
        },
        {
            "title": "Natural Language Processing for Customer Support",
            "description": "Created a text classification system to automatically categorize customer support tickets.",
            "skills": ["Python", "NLTK", "spaCy", "BERT"],
            "outcome": "Improved response time by 35% and increased customer satisfaction scores."
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
            st.markdown(f"**Outcome:** {project['outcome']}")
    
    # Add the interactive visualization demo
    # Remove the interactive visualization section
    # with st.expander("Interactive Data Visualization Demo", expanded=False):
    #     st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
    #     display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, 
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
     
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Teamwork:** Cooperative team member with experience in Agile settings
        - **Problem-solving:** Strong analytical and critical thinking abilities
        - **Time Management:** Efficient at prioritizing tasks and meeting deadlines
        - **Leadership:** Experience leading small teams and mentoring junior colleagues

        """)
    
    st.markdown("---")