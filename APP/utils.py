from datetime import datetime

import streamlit as st


def footer():
    """Display the footer with version and copyright information."""
    st.markdown(
        f"""
                <div class="footer">
                    <p>© {datetime.now().year} - Todos os direitos reservados a
                    <a href="https://www.linkedin.com/in/gabriel-pontes-2152a9276/" target="_blank" style="color: #FF5000; text-decoration: none;">Gabriel Pontes</a> e
                    <a href="https://www.linkedin.com/in/nercino-neto/" target="_blank" style="color: #FF5000; text-decoration: none;">Nercino Neto</a>
                    </p>
                </div>
            """,
        unsafe_allow_html=True,
    )
