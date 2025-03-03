import streamlit as st

def footer():
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #2C3E50;
                color: white;
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 5px 10px;  /* reduced padding to fit the content in one line */
                font-size: 16px;
            }
            .footer a {
                color: #1ABC9C;
                text-decoration: none;
                margin: 0 5px; /* spacing between links */
            }
            .footer a:hover {
                color: #16A085;
            }
            .footer-left {
                text-align: left;
            }
            .footer-center {
                text-align: center;
            }
            .footer-right {
                text-align: right;
            }
        </style>
        <div class="footer">
            <div class="footer-left">
                Developed with ❤️ by <a href="https://github.com/its-kundan" target="_blank">Kundan Kumar</a>
            </div>
            <div class="footer-center">
                🌐 <a href="https://kundan-cv-portfolio.vercel.app/" target="_blank">Portfolio</a> | 
                📧 <a href="mailto:kundan51kk@gmail.com">Email</a> | 
                🔗 <a href="https://linkedin.com/in/its-kundan" target="_blank">LinkedIn</a>
            </div>
            <div class="footer-right">
                View on <a href="https://github.com/its-kundan/Resume-to-Job-Matcher" target="_blank">GitHub</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
