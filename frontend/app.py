import streamlit as st
import time
import pandas as pd
from utils import extract_text_from_file
from scraper import detect_job_cards_with_description
from resume_matcher import ResumeMatcher
from ui_components import (
    apply_custom_styles, 
    render_job_card, 
    render_loading_animation,
    render_search_tips,
    render_no_results_message,
    render_footer
)

# Page configuration
st.set_page_config(
    page_title="LinkedIn Job Scraper with Resume Matching",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Apply custom styles
apply_custom_styles()

# Initialize session state for job listings if it doesn't exist
if 'job_listings' not in st.session_state:
    st.session_state.job_listings = []

if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False

if 'loading' not in st.session_state:
    st.session_state.loading = False

# Header
st.markdown("<h1 class='main-header'>🔍 LinkedIn Job Scraper with Resume Matcher</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Find the perfect job match based on your resume and LinkedIn job listings</p>", unsafe_allow_html=True)

# Create two columns for search parameters and resume upload
col1, col2 = st.columns([2, 1])

with col1:
    # Job search parameters
    st.markdown("<div class='section-header'>🔎 Job Search Parameters</div>", unsafe_allow_html=True)
    keyword = st.text_input(
        "Enter job title or keyword:", 
        placeholder="e.g., Data Scientist, Web Developer",
        help="Enter the job title or relevant keywords to search on LinkedIn"
    )
    
    # Additional filters in an expander
    with st.expander("Advanced Search Options"):
        location = st.text_input(
            "Location:", 
            placeholder="e.g., New York, Remote",
            help="Specify a location or enter 'Remote' for remote positions"
        )
        
        col_exp1, col_exp2 = st.columns(2)
        
        with col_exp1:
            experience_level = st.multiselect(
                "Experience Level:",
                ["Entry level", "Associate", "Mid-Senior level", "Director", "Executive"],
                default=None,
                help="Select one or more experience levels"
            )
        
        with col_exp2:
            job_type = st.multiselect(
                "Job Type:",
                ["Full-time", "Part-time", "Contract", "Temporary", "Internship"],
                default=["Full-time"],
                help="Select one or more job types"
            )
        
        results_limit = st.slider(
            "Maximum number of results:", 
            min_value=5, 
            max_value=30, 
            value=10,
            help="Control how many job listings to display"
        )

with col2:
    st.markdown("<div class='section-header'>📄 Resume Upload</div>", unsafe_allow_html=True)
    
    upload_option = st.radio(
        "Choose resume input method:", 
        ("Upload File", "Paste Text"),
        help="Select how you want to provide your resume"
    )
    
    resume_text = ""
    if upload_option == "Upload File":
        st.markdown("<p style='color: #dc3545; font-weight: 600; font-size: 0.9rem;'>⚠️ Note: Document uploading functionality is currently limited</p>", unsafe_allow_html=True)
        
        resume_file = st.file_uploader(
            "Upload your resume", 
            type=["pdf", "docx", "txt"],
            help="Supported formats: PDF, DOCX, TXT"
        )
        
        if resume_file is not None:
            file_details = {
                "Filename": resume_file.name, 
                "FileType": resume_file.type, 
                "FileSize": f"{resume_file.size / 1024:.2f} KB"
            }
            
            st.markdown(f"""
            <div style="background-color: #f8f9fa; padding: 10px; border-radius: 5px; font-size: 0.9rem;">
                <p><strong>File:</strong> {file_details['Filename']}</p>
                <p><strong>Type:</strong> {file_details['FileType']}</p>
                <p><strong>Size:</strong> {file_details['FileSize']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            try:
                resume_text = extract_text_from_file(resume_file)
                st.success("✅ Resume successfully processed!")
            except Exception as e:
                st.error(f"❌ Error processing file: {str(e)}")
    else:
        resume_text = st.text_area(
            "Paste your resume text:", 
            height=250, 
            placeholder="Copy and paste your resume text here...",
            help="Paste the full text of your resume for matching with job descriptions"
        )

# Search button and tips
search_col1, search_col2 = st.columns([3, 1])
with search_col1:
    search_button = st.button(
        "🔍 Search Jobs", 
        use_container_width=True,
        type="primary",
        help="Click to search for jobs on LinkedIn based on your criteria"
    )

# Search tips
render_search_tips()

# Handle search button click
if search_button:
    if keyword.strip():
        st.session_state.loading = True
        st.session_state.search_performed = True
        
        with st.spinner("Fetching and analyzing job listings... This may take a moment."):
            # Loading animation
            render_loading_animation()
            
            # Call the scraper
            try:
                job_listings = detect_job_cards_with_description(keyword)
                
                # Process results if we have any
                if job_listings:
                    # Resume matcher
                    for job in job_listings:
                        if resume_text:
                            matcher = ResumeMatcher(job["description"])
                            match_result = matcher.match_resume(resume_text)
                            job["similarity_score"] = match_result["similarity_score"]
                            job["missing_skills"] = match_result["missing_skills"]
                            job["matched_skills"] = match_result.get("matched_skills", [])
                        else:
                            job["similarity_score"] = 0
                            job["missing_skills"] = []
                            job["matched_skills"] = []
                    
                    # Sorting by % match if resume provided
                    if resume_text:
                        job_listings.sort(key=lambda x: x["similarity_score"], reverse=True)
                    
                    st.session_state.job_listings = job_listings
                else:
                    st.session_state.job_listings = []
            except Exception as e:
                st.error(f"Error during job search: {str(e)}")
                st.session_state.job_listings = []
        
        st.session_state.loading = False
    else:
        st.error("⚠️ Please enter a valid job keyword to start your search.")

# Display results if search was performed
if st.session_state.search_performed:
    if st.session_state.job_listings:
        st.markdown(f"<div class='section-header'>📊 Results: Found {len(st.session_state.job_listings)} Job Listings</div>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["Card View", "Table View"])
        
        with tab1:
            for idx, job in enumerate(st.session_state.job_listings):
                render_job_card(job, idx, resume_text)
        
        with tab2:
            job_df = pd.DataFrame(st.session_state.job_listings)
            
            if "similarity_score" in job_df.columns and resume_text:
                job_df["match_percentage"] = job_df["similarity_score"].apply(lambda x: f"{x:.0%}")
            
            # Determine which columns to display
            display_cols = ["title", "company", "location"]
            if resume_text and "match_percentage" in job_df.columns:
                display_cols.append("match_percentage")
            
            if "date_posted" in job_df.columns:
                display_cols.append("date_posted")
            
            # Create a more user-friendly table
            st.dataframe(
                job_df[display_cols],
                use_container_width=True,
                column_config={
                    "title": "Job Title",
                    "company": "Company",
                    "location": "Location",
                    "match_percentage": "Match Score",
                    "date_posted": "Date Posted"
                },
                hide_index=True
            )
    elif not st.session_state.loading:
        # Show no results message
        render_no_results_message()

# Footer
render_footer()