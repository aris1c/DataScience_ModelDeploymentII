import streamlit as st
import streamlit.components.v1 as stc

#IMPORT OUR APP
from ml_app import run_ml_app

def main():
    st.title("Main App")
    # stc.html(html_temp)

    menu = ["Home","Machine Learning"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        # st.markdown(desc_temp, unsafe_allow_html=True)
    elif choice == "Machine Learning":
        st.subheader("Machine Learning Section")
        run_ml_app()
    

if __name__ == '__main__':
    main()

