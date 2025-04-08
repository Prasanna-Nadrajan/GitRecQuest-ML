import streamlit as st

def apply_custom_styles():
    """Apply custom CSS styling to the Streamlit app"""
    st.markdown("""
    <style>
    /* Global Styles */
    .main-header {
        font-size: 2.6rem;
        color: #0077B5;
        margin-bottom: 1.5rem;
        text-align: center;
        font-weight: 700;
    }
    
    .app-subtitle {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
        text-align: center;
        font-style: italic;
    }
    
    .section-header {
        background-color: #0077B5;
        color: white;
        padding: 12px 15px;
        border-radius: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
        font-weight: 600;
        font-size: 1.1rem;
        display: flex;
        align-items: center;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .section-header svg {
        margin-right: 8px;
    }
    
    /* Form Styles */
    .stTextInput, .stSelectbox, .stMultiselect {
        margin-bottom: 15px;
    }
    
    /* Job Card Styles */
    .job-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 22px;
        margin-bottom: 25px;
        border-left: 5px solid #0077B5;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        transition: transform 0.2s, box-shadow 0.2s;
    }
    
    .job-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.12);
    }
    
    .job-title {
        color: #0077B5;
        margin-bottom: 8px;
        font-size: 1.3rem;
        font-weight: 600;
    }
    
    .company-name {
        font-weight: 500;
        color: #333;
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    
    .company-name svg {
        margin-right: 6px;
    }
    
    .job-location {
        font-size: 0.9rem;
        color: #666;
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }
    
    .job-location svg {
        margin-right: 6px;
    }
    
    .job-posted {
        font-size: 0.85rem;
        color: #888;
        margin-bottom: 15px;
    }
    
    /* Match Score Styles */
    .match-score-container {
        display: flex;
        align-items: center;
        margin-bottom: 12px;
    }
    
    .match-score-label {
        margin-right: 10px;
        font-weight: 500;
    }
    
    .match-score-high {
        color: #28a745;
        font-weight: bold;
        padding: 4px 10px;
        background-color: rgba(40, 167, 69, 0.1);
        border-radius: 20px;
    }
    
    .match-score-medium {
        color: #ffc107;
        font-weight: bold;
        padding: 4px 10px;
        background-color: rgba(255, 193, 7, 0.1);
        border-radius: 20px;
    }
    
    .match-score-low {
        color: #dc3545;
        font-weight: bold;
        padding: 4px 10px;
        background-color: rgba(220, 53, 69, 0.1);
        border-radius: 20px;
    }
    
    /* Skills Section */
    .skills-section {
        margin-top: 15px;
        background-color: #f9f9f9;
        border-radius: 8px;
        padding: 12px;
    }
    
    .skill-pill {
        display: inline-block;
        background-color: #e1f5fe;
        color: #0288d1;
        padding: 4px 10px;
        border-radius: 20px;
        margin-right: 8px;
        margin-bottom: 8px;
        font-size: 0.85rem;
    }
    
    .missing-skill-pill {
        display: inline-block;
        background-color: #ffebee;
        color: #c62828;
        padding: 4px 10px;
        border-radius: 20px;
        margin-right: 8px;
        margin-bottom: 8px;
        font-size: 0.85rem;
    }
    
    /* Button Styles */
    .stButton button {
        background-color: #0077B5;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 8px 16px;
        transition: all 0.3s;
        border: none;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .stButton button:hover {
        background-color: #005582;
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    
    .apply-button {
        background-color: #28a745 !important;
    }
    
    .apply-button:hover {
        background-color: #218838 !important;
    }
    
    /* Loading Animation */
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    
    /* Tooltip */
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px 0;
        font-size: 0.9rem;
        color: #666;
        margin-top: 40px;
        border-top: 1px solid #eee;
    }
    
    /* Table styling */
    .dataframe {
        font-size: 0.9rem !important;
    }
    
    .dataframe th {
        background-color: #f5f9ff;
        font-weight: 600;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .main-header {
            font-size: 2rem;
        }
        
        .job-title {
            font-size: 1.1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def render_job_card(job, idx, resume_text=""):
    """
    Render a job listing as a card with enhanced UI
    
    Args:
        job (dict): Job listing information
        idx (int): Index for unique keys
        resume_text (str): Resume text if provided
    """
    with st.container():
        st.markdown(f"""
        <div class='job-card'>
            <h3 class='job-title'>{job["title"]}</h3>
            <p class='company-name'>🏢 {job["company"]}</p>
            <p class='job-location'>📍 {job.get("location", "Location not specified")}</p>
            <p class='job-posted'>📅 Posted: {job.get("date_posted", "Recently")}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Score display
        score = job.get("similarity_score", 0)
        score_class = "match-score-high" if score >= 0.7 else "match-score-medium" if score >= 0.4 else "match-score-low"
        
        col1, col2 = st.columns([1, 1])
        with col1:
            if resume_text:
                st.markdown(f"""
                <div class='match-score-container'>
                    <span class='match-score-label'>Match Score:</span>
                    <span class='{score_class}'>{score:.0%}</span>
                </div>
                """, unsafe_allow_html=True)
        with col2:
            st.button(f"Apply Now", key=f"apply_{idx}", help="Click to apply for this position", type="primary")
        
        with st.expander("📝 View Job Description"):
            st.write(job["description"])
        
        if resume_text:
            with st.expander("🧩 Skills Analysis"):
                skill_col1, skill_col2 = st.columns(2)
                
                with skill_col1:
                    if job.get("matched_skills"):
                        st.markdown("✅ **Your Matching Skills:**")
                        skills_html = ""
                        for skill in job["matched_skills"]:
                            skills_html += f"<span class='skill-pill'>{skill}</span>"
                        st.markdown(f"<div>{skills_html}</div>", unsafe_allow_html=True)
                    else:
                        st.info("No skill matches found. Consider updating your resume with relevant keywords.")
                        
                with skill_col2:
                    if job.get("missing_skills"):
                        st.markdown("⚠️ **Skills to Highlight or Develop:**")
                        skills_html = ""
                        for skill in job["missing_skills"]:
                            skills_html += f"<span class='missing-skill-pill'>{skill}</span>"
                        st.markdown(f"<div>{skills_html}</div>", unsafe_allow_html=True)
                    else:
                        st.success("Great! Your resume appears to cover all the key skills mentioned in this job post.")
                
                st.markdown("""
                <div style="margin-top: 15px; font-size: 0.9rem; color: #666;">
                    <p><strong>Tip:</strong> Update your resume to include more relevant keywords from the job description to improve your match score.</p>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("<hr style='margin: 30px 0; border-color: #eee;'>", unsafe_allow_html=True)

def render_loading_animation():
    """Display a loading animation while processing jobs"""
    st.markdown("""
    <div class="loading-spinner">
        <svg width="50" height="50" viewBox="0 0 50 50" xmlns="http://www.w3.org/2000/svg">
            <circle cx="25" cy="25" r="20" fill="none" stroke="#0077B5" stroke-width="5">
                <animate attributeName="stroke-dasharray" dur="1.5s" repeatCount="indefinite" values="1,150;90,150;90,150"/>
                <animate attributeName="stroke-dashoffset" dur="1.5s" repeatCount="indefinite" values="0;-35;-124"/>
            </circle>
        </svg>
    </div>
    """, unsafe_allow_html=True)

def render_search_tips():
    """Render helpful tips for job searching"""
    with st.expander("💡 Tips for Effective Job Search"):
        st.markdown("""
        ### Maximize Your Job Search
        
        - **Be specific** with job titles for better matches
        - **Include your skills** clearly in your resume
        - **Use industry keywords** that are common in job descriptions
        - **Update your resume** for each job application to highlight relevant experience
        - **Check regularly** as new jobs are posted daily
        """)

def render_no_results_message():
    """Render a helpful message when no results are found"""
    st.markdown("""
    <div style="text-align: center; padding: 40px 20px; background-color: #f8f9fa; border-radius: 10px; margin: 20px 0;">
        <img src="https://cdn-icons-png.flaticon.com/512/6134/6134065.png" width="100" height="100" style="margin-bottom: 20px;">
        <h3 style="color: #666;">No Jobs Found</h3>
        <p style="color: #888; max-width: 400px; margin: 0 auto;">
            We couldn't find any jobs matching your search criteria. Try broadening your search terms or checking different locations.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Render the application footer"""
    st.markdown("""
    <div class="footer">
        <p>Built with ❤️ using Streamlit | Data sourced from LinkedIn</p>
        <p>Remember to use this tool responsibly and in accordance with LinkedIn's terms of service.</p>
        <p style="font-size: 0.8rem; color: #999; margin-top: 10px;">This tool is for educational purposes only.</p>
    </div>
    """, unsafe_allow_html=True)