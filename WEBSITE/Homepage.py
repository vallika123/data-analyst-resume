import streamlit as st 
from pathlib import Path 
from PIL import Image
import base64

#--Path Settings--
current_dir = Path(__file__).parent  if "__file__" in locals() else Path.cwd()
css_file = current_dir /"styles"/ "main.css"
resume_file = current_dir / "pages" /"Vallika Kasibhatla_Resume_Data.pdf"

#--basic info--
email=" vallika.kasibhatla25@gmail.com "
phone_number="+1 (437)-998-5255"
social_media= {"LinkedIn" : ("https://www.linkedin.com/in/vallika-kasibhatla-9b75a1225/","https://static-00.iconduck.com/assets.00/linkedin-emoji-512x512-mx3d67rm.png"),
    "Github" :("https://github.com/vallika123", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/GitHub_Invertocat_Logo.svg/180px-GitHub_Invertocat_Logo.svg.png")
}
linkedin_icon = '<i class="fa fa-linkedin-square" style="font-size:24px;color:#0e76a8;"></i>'
core_skills = [
    {"label": "MS Office", "details": "Microsoft Project, Excel, PowerPoint, Access"},
    {"label": "Data Analytics", "details": "Python, R-studio, Minitab, Matlab"},
    {"label": "Machine Learning", "details": "Data cleaning, Preprocessing, Feature engineering, Data interpretation"},
    {"label": "Data Visualization", "details": "Power BI, Tableau. IBM Cognos, Google Looker"},
    {"label": "Process Optimization", "details": "Automation"},
    {"label": "Natural Language Processing", "details": "NLP libraries, Sentiment analysis"},
    {"label": "Database Management", "details": "SQL (MySQL, SQLite), NoSQL (MongoDB), ETL, Data Warehousing"},
    {"label": "Cloud & Big Data", "details": "AWS, Hadoop, Web Scraping"},
    {"label": "Software Development", "details": "Java, C++, HTML, CSS, JavaScript"},  
]


soft_skills = [
    "Leadership",
    "Team management",
    "Communication",
    "Problem solving",
    "Adaptability",
    "Quick learner",
    "Creativity",
    "Organization skills",
    "Innovation"
]


st.set_page_config(page_title="Digital CV | Vallika Kasibhatla", 
                   page_icon=":tada:", 
                   layout="centered")

#st.subheader("Hi, I am vallika :wave:")
custom_css = """
<style>
    body {
        background-color: #013328;  /* Force background to be white */
        color: #013328;  /* Force text color to be black */
    }
    .stApp {
        background-color: #F7F1ED;  /* Set main app background */
    }
    h1, h2, h3, h4, h5, h6, p{
        color: #013328;  /* Set header text colors */
    }
    .stButton button {
        background-color:#F7F1ED;  /* Customize button colors */
        color: #013328;
    }
</style>
"""

# Apply the custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
#LOAD CSS, PDF ETC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
    
with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
    


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #013328;">
  <a class="navbar-brand" target="_blank" style="pointer-events: none; cursor: default; color: pink;">Vallika Kasibhatla</a>

  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#core-skills">Core Skills</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#certificates">Certificates</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#professional-experience">Professional Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
     <li class="nav-item">
        <a class="nav-link" href="#projects" style="color: white;" onclick="streamlit.run('Projects.py')">Projects</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)




#--HERO SECTION 

# Hero Section
st.markdown("""
    <style>
    .hero-section {
        text-align: center;
        margin-top: 0;
    }
    .hero-title {
        font-size: 2.5em;
        color: #013220;
        font-weight: bold;
    }
    .hero-subtitle {
        font-size: 1.2em;
        color: #013220;
    }
    </style>
    <div class="hero-section">
        <h1 class="hero-title">Vallika Kasibhatla <span style="font-size: 1.2em;"></span></h1>
        <p class="hero-subtitle">Aspiring Data Professional | Specialized in Analytics, Engineering Solutions, and Data Science | M.Eng. in Engineering Management | B.Sc. in Computer Science & Data Science</p>
    </div>
""", unsafe_allow_html=True)

col1,col2 = st.columns(2, gap="medium")
with col1: 
    st.markdown(""" <br> Passionate about leveraging advanced data science and machine learning techniques to address complex challenges and drive innovative solutions.
     """,
    unsafe_allow_html=True
    )
    
with col2:
    st.markdown(
    """
    <style>
    .custom-link {
        color: black !important; /* Ensure the color is applied */
        text-decoration: none; /* Remove underline */
    }
    .custom-link:hover {
        color: black !important; /* Ensure the color remains black on hover */
        text-decoration: underline;
    }
    .social-media-icon {
        vertical-align: middle; /* Aligns image with text */
        width: 24px; /* Adjust size as needed */
        height: 24px; /* Adjust size as needed */
        margin-right: 8px; /* Space between image and text */
    }
    .contact-info {
        color: black; /* Set email and phone number text to black */
        font-size: 1.1em;
        line-height:2em;
         margin-bottom: 0.5em; 
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="contact-info">
        <strong>Email:</strong> {email}<br>
        <strong>Phone Number:</strong> {phone_number}<br>
    </div>
    """, unsafe_allow_html=True)
    
   
# Displaying social media links
    for platform, (link, image_url) in social_media.items():
        st.markdown(
        f"<a class='custom-link' href='{link}' target='_blank'>"
        f"<img class='social-media-icon' src='{image_url}' alt='{platform} icon' />"
        f"{platform}</a>", unsafe_allow_html=True
        )
        
    st.download_button(
    label="📝Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream"
    )


st.markdown(
    """
    <style>
    .card {
        background-color: #fff9f9;
        padding: 15px;
        border-radius: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: 0.3s;
        margin-bottom: 10px;
        
    }
    .card:hover {
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    .card p {
        margin: 0;
        color: #013220;
        /* Remove margin between paragraphs */
    }
    .scrollable-block {
        max-width: 100%; /* Adjust width as needed */
        height: 600px; /* Fixed height for the block */
        overflow: auto; /* Enable scrolling if content overflows */
        border: 1px solid #ccc; /* Optional border for the block */
    }
    iframe {
        width: 100%; /* Make the iframe fill the width of the container */
        height: 100%; /* Make the iframe fill the height of the container */
        border: none; /* Remove iframe border */
    }
    .float-right {
         float: right;
}
    </style>
    """,
    unsafe_allow_html=True
)




###CORE SKILLS
#st.markdown('<p class="custom-subheader">CORE SKILLS</p>', unsafe_allow_html=True)
st.subheader("CORE SKILLS")


# Tabs creation with technical, software packages, and soft skills
tab1, tab2= st.tabs([
    "Technical Skills", 
    "Software Packages", 

])

with tab1:

    # Create a 4x4 grid layout
    cols = st.columns(3, gap="small")
    
    # Calculate number of items per column
    items_per_col = 3
    total_items = len(core_skills)
    
    for i in range(3):
        with cols[i]:
            # Display 4 items in each column
            for j in range(items_per_col):
                index = i * items_per_col + j
                if index < total_items:
                    skill = core_skills[index]
                    st.markdown(f"""
                    <div class='card'>
                        <p style='margin-bottom: 5px;'>
                            <strong>{skill['label']}</strong>: {skill['details']}
                        </p> 
                    </div>
                    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <style>
    .image-container {
        position: relative;
        display: inline-block;
        width: 120px;
        height: 120px;
        margin-right: 20px;
        
    }
    .image-container img {
        width: 130%;
        height: auto;
        transition: transform 0.3s ease;
    }
    .image-container:hover img {
        transform: scale(1.1);
    }
    .image-container .hover-text {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: white;
        text-align: center;
        border-radius: 5px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 110%; /* Position above the image */
        left: 50%;
        margin-left: -60px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .image-container:hover .hover-text {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9, gap="small")
    with col2:
        
        st.markdown("""
        <div class="image-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/1280px-NumPy_logo_2020.svg.png">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1280px-Pandas_logo.svg.png">
            <span class="hover-text">Data Manipulation and Analysis</span>
        </div>
         """, unsafe_allow_html=True)
  
        
    with col4:
        
        st.markdown("""
        <div class="image-container">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png " >
            <span class="hover-text">Scikit-Learn</span>
        </div>
         """, unsafe_allow_html=True)
        
    with col6:
        
        st.markdown("""
        <div class="image-container">
            <img src="https://camo.githubusercontent.com/3eed28e026e4e0220f99e2f4c8a517fcb3a30a1b944c528efc9533ff7840435f/68747470733a2f2f6d6174706c6f746c69622e6f72672f5f7374617469632f6c6f676f322e737667">
             <img src="https://images.ctfassets.net/wkud0epjdpn7/2celPMbF0Cq9iSvK6FOfqa/0e1839a2555364fefed68f3229ea5978/LP-APAC-NUSSOC-AML-Tools-Img-11.png">
            <span class="hover-text">Data Visualization</span>
        </div>
         """, unsafe_allow_html=True)
    
    with col8:
        
        st.markdown("""
        <div class="image-container">
            <img src="https://www.statsmodels.org/dev/_images/statsmodels-logo-v2.svg">
            <span class="hover-text">Data Exploration</span>
        </div>
         """, unsafe_allow_html=True)



###CERTIFICATES

st.write ("---")   
st.subheader("CERTIFICATES")

current_dir=Path(__file__).parent  if "__file__" in locals() else Path.cwd()
Paper1 = current_dir / "pages/FINAL CERTIFICATE.pdf"
with open(Paper1,"rb") as pdf_file:
    PDFbyte_1=pdf_file.read()
    
pdf_base64_1 = base64.b64encode(PDFbyte_1).decode('utf-8')

st.markdown(f"""
        <h5><strong> IBM Professional Certificate in Data Analytics </strong></h5>
        <p> A comprehensive program on Python, SQL, and Excel while providing hands-on experience through real-world projects.
        AI-driven techniques were also explored to enhance data analysis, building a strong foundation for data-driven roles.</p>
    """, unsafe_allow_html=True)


# Button to display the PDF
if st.button(" :receipt: Open Certificate"):
  st.markdown(
    f'''
    <style>
    iframe {{
        width: 100%;
        height: 500px;
        border: none;
        overflow: hidden;
    }}
    </style>
    <iframe src="data:application/pdf;base64,{pdf_base64_1}" width="700" height="800" type="application/pdf"></iframe>
    ''',
    unsafe_allow_html=True
)
####PROFESSIONAL EXPERIENCE
st.write ("---") 
st.subheader("PROFESSIONAL EXPERIENCE")

st.markdown(f""" <div class='card'>
    <h4 style='color: #013220; margin-bottom: 5px;'><strong>💼 Supply Chain Operations Analyst </strong></h4>
    <img src="https://static.cdnlogo.com/logos/c/18/chevron.png" style='width:100px; height:auto; position: absolute; top: 0; right: 10px;'>
    <i style='margin-bottom: 5px;'>Chevron  •  Dubai, United Arab Emirates  •  Jul 2022 - May 2023 </i></h6>
    <p style='color: #013220; margin-top: 5px;'>
    <ul>
        <li>Held positions in downstream operations in Bahrain and UAE, addressed supply chain operations and served as an additives material requirements planner for day-to-day operations. <br></li>
        <li><strong>• Improved Vendor Relationships:</strong> Executed precise product ordering through SAP for external clients and ensured timely procurement of shipment details. Identified vendor issues and managed discontinued/expired products by organizing historical data, resulting in a <strong>60% improvement </strong> in vendor relationships.<br></li>
        <li><strong>• Automated Reporting Processes:</strong> Transformed manual report updates by automating Excel-to-Word links, saving <strong> 25 minutes </strong> per container-wise report and optimizing team productivity. This initiative contributed to overall process efficiency and reduced administrative workload.<br></li>
       <li> <strong>• Enhanced Demand Planning:</strong> Optimized the company’s cost management and additives inventory purchasing by conducting data analysis using Excel and R-Studio, resulting in a <strong>45% increase </strong> in demand planning accuracy and contributing to cost reduction initiatives.<br></li>
    </ul>
     """, unsafe_allow_html=True)


    
st.markdown(f""" <div class='card'>
    <h4 style='color: #013220'; margin-bottom: 5px;'><strong>💼 Data Analyst </strong> </h4>
    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Voltas_logo.png" style='width:100px; height:auto; position: absolute;  top: 10px; right:15px;'>
    <i style='margin-bottom: 5px;'> Voltas Limited TATA Enterprise  •  Doha, Qatar  •  Jan 2020 - Apr 2020 </i></h6>
    <p style='margin-top: 5px;'>
    <ul>
        <li><strong>• Data Analysis and Reporting:</strong> Analyzed employee and management datasets, identifying data gaps and producing a comprehensive report that increased HR analytical insights by <strong>35% </strong>. Utilized Power BI for data visualization, creating interactive dashboards to facilitate data-driven decision-making.<br></li>
        <li><strong>• Employee Engagement Initiatives:</strong> Facilitated monthly newsletters by providing detailed analyses of key company events and organized off-site gatherings, leading to a <strong>25% increase </strong>in employee satisfaction. Demonstrated strong interpersonal and communication skills in managing these initiatives.<br></li>
        <li><strong>• Project Management Optimization:</strong> Leveraged Primavera for project management and scheduling analysis. Evaluated KPI data to optimize workflows for 8 construction managers and 20 subcontractors, resulting in improved operational efficiency and reduced project delays.<br></li>
        <li><strong>• Process Improvement:</strong> Contributed to process improvement projects by identifying inefficiencies and recommending changes, aligning with the company’s continuous improvement goals and enhancing overall project outcomes.<br>
    </ul>
    """, unsafe_allow_html=True)    


######---EDUCATION----####
st.write("---")
st.subheader("EDUCATION")  
subjects = [
    "Calculus I, II",
    "Digital Systems",
    "Graphical User Interface ",
    "Database Systems",
    "Design-Analysis of Algorithms",
    "Software Engineering",
    "Operating Systems",
    "Computer and Communication Networks",
    "Mobile Application Development",
    "Artificial Intelligence",
    "Data Mining",
    "Machine Learning",
    "Statistics for Data Science"
]

# Generate HTML for course bubbles
bubbles_html = ''.join(f'<div class="bubble">{subject}</div>' for subject in subjects)
st.markdown("""
<style>
    .bubble {
        display: inline-block;
        padding: 10px;
        background-color: #e0e0e0;
        border-radius: 15px;
        margin: 5px;
        font-size: 14px;
    }

    .edu-section {
        position: relative;
        margin-bottom: 30px;
    }
</style>

<div class="edu-section">
    <p style='margin-bottom: 5px;'><strong> Ontario Tech University </strong>
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6e/OntarioTech_primary_2019.svg" style='width:150px; height:auto; position: absolute; top: 0px; right: 15px;'>
        <br> M.Eng. of Engineering Management <br> 
        Oshawa, Ontario • Sep 2023 - Aug 2024 <br>
        Grade: 4.18 / 4.30 <br><br>
        <i>Subjects:</i>
    </p>
    <br>
    <div class="bubble">Project Management</div>
    <div class="bubble">Foundation of Engineering Management</div>
    <div class="bubble">Production and Operations Management</div>
    <div class="bubble">Operations Research</div>
    <div class="bubble">Quality Management</div>
    <div class="bubble">Applied Risk Analysis</div>
    <div class="bubble">Knowledge Discovery in Data Science</div>
    <div class="bubble">Accounting</div>
    <div class="bubble">Software Engineering</div>
</div>

<div class="edu-section">
    <p style='margin-bottom: 5px;'><strong> American University of Sharjah </strong>
        <img src="https://upload.wikimedia.org/wikipedia/en/c/c8/American_University_of_Sharjah_%28emblem%29.png" style='width:120px; height:auto; position: absolute; top: 0px; right: 15px;'>
        <br> B.Sc. in Computer Science, Minor in Data Science <br> 
        Sharjah, United Arab Emirates • Sep 2019 - Jun 2023 <br>
        Grade: 3.34 / 4.00 <br><br>
        <i>Subjects:</i>
    </p>
</div> 
""", unsafe_allow_html=True)
st.markdown(bubbles_html, unsafe_allow_html=True)

st.write("---")



###PROJECTS

st.subheader("PROJECTS")

# Upload the PDF file



pdf_link_nba = "https://github.com/vallika123/NBA-Lineup-Prediction"
pdf_link_risk ="https://github.com/vallika123/-In-depth-Risk-Management-of-AI-in-the-medical-field"
pdf_link_soft="https://github.com/vallika123/Generalizing-Speech-Emotion-Recognition-A-Multimodal-and-Multidataset-Approach"
pdf_link_stats="https://github.com/vallika123/-Model-Building-to-Predict-Popularity-Score-of-News-Articles"
st.markdown(f"""
 
    <div class='card'>
        <h5><strong>NBA Players Lineup Prediction</strong></h5>
        <strong>Problem Statement:</strong>
        <ul>
            <li><strong>Predicting Game Outcome:</strong> Given the names of five home team players and five away team players, predict the outcome of the game.</li>
            <li><strong>Enhancing Team Lineup:</strong> Predict the fifth player in the away team's lineup to improve the chances of winning, based on four away team players and five home team players.</li>
        </ul>
        <strong>Tools Used:</strong>
        <ul>
            <li><strong>Feature Engineering:</strong> Feature Selection and Feature Transformation</li>
            <li><strong>Machine Learning Models:</strong> Support Vector Machines (SVM), Logistic Regression (LR), Gradient Boosting (XGBoost), Random Forest (RF)
            <li><strong>Text Data:</strong> Embeddings for player names</li>
        </ul>
       <strong>Outcome:</strong>
        <p>Using Random Forest, we achieved an accuracy of 79% in predicting game outcomes.</p>
        <br>
        <!-- PDF preview inside the same card -->
        <a href="{pdf_link_nba}" target="_blank" class="custom-link">View → </a>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
 
    <div class='card'>
        <h5><strong>Generalizing Speech Emotion Recognition: A Multimodal and Multidataset Approach</strong></h5>
        <strong>Problem Statement:</strong>
        <ul>
            <li><strong>Emotion Detection from Speech:</strong> The task involves accurately predicting emotions from speech, which is challenging due to factors such as speaker diversity, poor audio quality, speaker diarization, and the lack of inclusive and complex datasets.</li>
        </ul>
        <strong>Tools Used:</strong>
        <ul>
            <li><strong>Datasets:</strong> Combined five datasets to enhance generalizability.</li>
            <li><strong>Feature Engineering:</strong> Feature Extraction, Data Augmentation, Noise addition and Time stretching
            <li><strong>Machine Learning and Neural Network Models:</strong> SVM, RF, XGBoost, KNN, Extra Tree Classifer, Convolutional Neural Network (CNN), Multilayer Perceptron (MLP) </li>
        </ul>
       <strong>Outcome:</strong>
        <p>Using Ensemble learning, combining SVM and RF an 80% accuracy was observed.</p>
        <br>
        <!-- PDF preview inside the same card -->
        <a href="{pdf_link_soft}" target="_blank" class="custom-link">View → </a>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
 
    <div class='card'>
        <h5><strong>In-depth Risk Management of AI in the Medical Field</strong></h5>
        <strong>Problem Statement:</strong>
        <ul>
            <li>The research focuses on identifying the risks present at every stage of detecting illness through image inputs using classification models.</strong></li>
        </ul> 
        <strong>Topics:</strong>
        <ul>
            <li>• Hazard scenarios, causes, propagation and escalation, consequences, and risk estimation. </li>
            <li>• Qualitative and quantitative analyses, utilizing techniques like Bayesian Belief Networks and Human Error Analysis. </li>
            <li>• Risk calculations, defining and reducing acceptable risk, layers of protection, reducing failure probability, and reliability. </li>
            <li>• AI model, AI aging, validation and verification, ongoing monitoring, and adherence to standards.</li>
        </ul>
        <!-- PDF preview inside the same card -->
        <a href="{pdf_link_risk}" target="_blank" class="custom-link">View → </a>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""
 
    <div class='card'>
        <h5><strong>Model Building to Predict Popularity Score of News Articles</strong></h5>
        <strong>Problem Statement:</strong>
        <ul>
            <li><strong>Objective:</strong> To determine which independent variables have the most significant impact on the number of shares an article receives.</li>
            <li><strong>Data Analysis:</strong> The project explores summary statistics (mean, median, outliers) and uses visualizations such as histograms, boxplots, and pie charts to analyze the distribution of shares and categorical predictors. Additionally, a correlation matrix is employed to assess relationships between independent variables.
        </ul> 
        <strong>Tools Used:</strong>
        <ul>
            <li><strong>Languages:</strong> Python and Minitab</li>
            <li><strong>Inferential Statistics and Models:</strong> Chi-square test, Confidence intervals, One-way ANOVA, Two-way ANOVA, Logistic and Linear regression</li>
        </ul>
        <!-- PDF preview inside the same card -->
        <a href="{pdf_link_stats}" target="_blank" class="custom-link">View → </a>
    </div>
""", unsafe_allow_html=True)