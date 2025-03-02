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
                text-align: center;
                padding: 10px;
                font-size: 16px;
            }
            .footer a {
                color: #1ABC9C;
                text-decoration: none;
            }
            .footer a:hover {
                color: #16A085;
            }
        </style>
        <div class="footer">
            <p>Developed with ❤️ by <a href="https://github.com/its-kundan" target="_blank">Kundan Kumar</a></p>
            <p>
                🌐 <a href="https://kundan-cv-portfolio.vercel.app/" target="_blank">Portfolio</a> | 
                📧 <a href="mailto:kundan51kk@gmail.com">Email</a> | 
                🔗 <a href="https://linkedin.com/in/its-kundan" target="_blank">LinkedIn</a> |
            </p>
            <p>View on <a href="https://github.com/its-kundan/Resume-to-Job-Matcher" target="_blank">GitHub</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
