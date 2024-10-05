from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "FenaJain_Resume.pdf"
profile_pic = current_dir / "assets" / "circle_profile_pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Fena Jain"
PAGE_ICON = ":clipboard:"
NAME = "Fena Jain"
DESCRIPTION = """Organized and motivated employee eager to apply time management and organizational skills in various environments. 
Seeking entry level opportunities to expand skills while facilitating company’s growth
"""

PROJECTS = {
    "🏆 Sales Dashboard - Perfect overview of sales in particular state wise": "https://public.tableau.com/app/profile/darshan6443/viz/Task3_16496633540690/Dashboard1?publish=yes",
    "🏆 Whatsapp Chat Analyzer - Detailed analysis of your Whatsapp Chats": "https://darshan660-whatsapp-chat-analyzer-app-39qdr8.streamlit.app/",
"🏆 Laptop Price Predictor - Predicts your laptop price with respect to specifications": "https://darshans-project-laptop-price-predictor.streamlit.app/",
"🏆 Asian Landmark Detection - Predicts the name and provides the location of your uploaded Asian landmark": "https://darshans-project-landmark-detection.streamlit.app/"

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write("\n")
    st.image(profile_pic, width=290)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

# --- Educational Background ---
st.write('\n')
st.subheader("Qualifications")

st.write("- ✔️ **KES Shroff College - Mumbai**")
st.markdown("- - " + "Bachelors of Science, Data Science")
st.markdown("- - " + "June 2020 - May 2023")
st.write("- ✔️ **Shri T.P. Bhatia College of Science - Mumbai**")
st.markdown("- - " + "HSC from Science Stream")
st.markdown("- - " + "June 2016 - May 2018")
st.write("- ✔️ **St. Lawrence High School - Mumbai**")
st.markdown("- - " + "SSC")
st.markdown("- - " + "June 2005 - March 2016")


# --- SKILLS ---
st.write('\n')
st.subheader("Professional Proficiencies")

col1,col2 = st.columns(2)
with col1:
    st.write(
        """
    - ➡️ Python Programming
    - ➡️ Machine Learning
    - ➡️ Deep Learning
    - ➡️ Data Analysis
    - ➡️ Database Management & SQL
    """
    )
with col2:
    st.write(
        """
        - ➡️ Data Visualization - Power BI, Tableau
        - ➡️ Statistical Analysis
        - ➡️ Business Acumen
        - ➡️ Problem-Solving
        - ➡️ Attention to detail
        """
    )

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**DronaPay | Business Analyst**")
st.write("- "+"**11/2023 - Present**")
# st.markdown("span style='line-height: 0.8; font-size: 14px;'>🚧 [**DronaPay | Business Analyst**)
st.write("*Key Responsibilities :*")
st.write(
    """
- ► Collaborating with clients to gather and analyze requirements, translating them into pseudocode, algorithms, and detailed test conditions for effective fraud detection solutions.
- ► Defining and executing comprehensive test cases covering a range of criteria to ensure high-quality delivery of fraud detection systems. Validating user interface (UI) designs to ensure adherence to banking industry norms and client-specific requirements.
- ► Ensuring thorough testing of edge cases to identify potential vulnerabilities in fraud detection algorithms.
- ► Developing and implemented strategies for continuous improvement in fraud detection methodologies, enhancing overall system security.
- ► Facilitating communication between technical teams and clients, ensuring that fraud detection solutions met both technical and business objectives.
"""
)

# --- JOB 2
st.write("🚧", "[**BugendaiTech | Data Science Intern**](https://drive.google.com/file/d/1ipqWo5KgW-0QMkcY06alpGzgXi2b5jmU/view?usp=sharing)")
st.write("- "+"**06/2023 - 09/2023**")
# st.markdown("span style='line-height: 0.8; font-size: 14px;'>🚧 [**BugendaiTech | Data Science Intern**](https://drive.google.com/file/d/1RdlEus2yYHSQduBE3rPmU-MK_cZA0WYW/view?usp=sharing)</span>", unsafe_allow_html=True)
st.write("*Key Responsibilities :*")
st.write(
    """
- ►  Cleaned and Manipulated raw data
- ►  Performed EDA on large datasets to identify patterns, trends
- ►  Creating graphs and charts detailing data analysis with Tableau and PowerBI 
- ►  Implemented NLP algorithms for text-based analysis task
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "[**Bharat Intern | Data Science Intern**](https://drive.google.com/file/d/1DqJPLfulcmYrqUNwCmCjTxUF3yjo0hZb/view?usp=sharing)")
st.write("- "+"**07/2023 - 08/2023**")
st.write("*Key Responsibilities :*")
st.write(
    """
- ►  Developed and implemented Stacked LSTM architecture tailored for Stock Market Price Prediction.
- ►  Data Preprocessing and Feature Engineering
- ►  Hyperparameter Optimization
- ►  Time Series Data Handling
- ►  Overfitting Prevention
- ►  Model Evaluation
"""
)

# --- JOB 4
st.write('\n')
st.write("🚧", "[**LetsGrowMore | Data Science Intern**](https://drive.google.com/file/d/1dmd8yvsoq3g-oeICMO58vMzVh3H5UnhA/view?usp=sharing)")
st.write("- "+" **06/2023 - 07/2023**")
st.write("*Key Responsibilities :*")
st.write(
"""
- ►  Designed and implemented machine learning models tailored for classification tasks.
- ►  Cleaned, preprocessed, and engineered features to enhance model compatibility and performance.
- ►  Implemented and evaluated a range of classification algorithms including [Logistic Regression, Decision Tree, SVM] for optimal model selection.
- ►  Utilized data visualization libraries (e.g., Matplotlib, Seaborn) to create informative plots, aiding in exploratory data analysis and model interpretation.
"""
)


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")



# --- Certificates ---
st.write('\n')
st.subheader("Certifications")
st.write("---")

st.write("⭐ [Machine Learning by Great Learning](https://drive.google.com/file/d/1X3UNpG3wL0iiw2m2qmsb6onzd3YzxJSX/view?usp=sharing)")
# st.write(
#     '''
#     <style>
#         a:hover {
#             color: blue !important;
#         }
#     </style>
#     <a href="https://drive.google.com/file/d/1X3UNpG3wL0iiw2m2qmsb6onzd3YzxJSX/view?usp=sharing" target="_blank" style="text-decoration:none; color: white; display: inline-block; position: relative;">⭐ Machine Learning by Great Learning</a>
#     ''', 
#     unsafe_allow_html=True
# )

st.write("⭐ [Data Warehousing & BI by KES Shroff College](https://drive.google.com/file/d/12SX9n-WjHjq34WZTBN90cYBiq8n8R_Cm/view?usp=sharing)")
st.write("⭐ [Data Visualization in PowerBI by Great Learning](https://drive.google.com/file/d/1qdkZtohzpIAINgsATIPf6ej2mr8UnHz0/view?usp=sharing)")
st.write("⭐ [Introduction to Image Generation by Google Skill Boost](https://drive.google.com/file/d/1O5e4I8RSfwbGSTZqHY5M7ZNPVcIC4IGN/view?usp=sharing)")
st.write("⭐ [Introduction to Generative AI by Google Skill Boost](https://drive.google.com/file/d/1qpdd27LkE_799uW5pWijSk7crPuvz4us/view?usp=sharing)")

st.write('')
# Create columns for each social media link
col1, col2, col3, col4 = st.columns(4)

# Add LinkedIn link
with col1:
    st.markdown('<a href="https://www.linkedin.com/in/thefenajain" target="_blank" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" alt="LinkedIn" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">LinkedIn</p>', unsafe_allow_html=True)

# Add GitHub link
with col2:
    st.markdown('<a href="https://github.com/fenajain?tab=repositories" target="_blank" style="text-decoration:none;"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">GitHub</p>', unsafe_allow_html=True)

# Add Twitter link
with col3:
    st.markdown('<a href="https://wa.me/918286708984?text=Hello%20there,%20I%20thanks%20for%20connecting!" style="text-decoration:none;"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/WhatsApp.svg/1200px-WhatsApp.svg.png" alt="Twitter" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">WhatsApp</p>', unsafe_allow_html=True)

# Add Email link
with col4:
    st.markdown('<a href="mailto:wish2fena678@gmail.com"  target="_blank" style="text-decoration:none;"><img src="https://workspace.google.com/static/img/products/png/gmail.png?cache=f50ecb6" alt="Email" width="40" height="40" style="display:block;margin-left:auto;margin-right:auto;"></a>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;font-size:16px;margin-top:10px;">Email</p>', unsafe_allow_html=True)

# Add footer
st.write('---')
st.write('© Fena Jain  |  Last updated: October 2023')
