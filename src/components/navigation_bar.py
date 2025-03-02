import streamlit as st

def navigation_bar():
    # Basic navigation bar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "About", "Developer", "Contact"])

    # GitHub icon and link
    github_icon = """
    <a href='https://github.com/its-kundan/Resume-to-Job-Matcher' target='_blank'>
        <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='30' height='30'>
    </a>
    """
    st.sidebar.markdown(github_icon, unsafe_allow_html=True)

    return page
