import streamlit as st 
import pandas as pd 
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
st.set_page_config(page_title="Data Profiler", layout="wide")



with st.sidebar:
    uploaded_file = st.file_uploader('Upload .csv, .xlsx file not exceeding 10MB')
    
    st.markdown('---')
    st.text('Mode of Operation')
    if uploaded_file is not None:  
        minimal= st.checkbox("Do you want minimal report ?")
        #print(minimal)
        display_mode = st.radio('Display Mode',('Primary','Dark','Orange'))
        if display_mode == 'Dark':
            dark_mode = True
            orange_mode = False
        elif display_mode == 'Orange':
            dark_mode = False
            orange_mode = True
        else:
            dark_mode = False
            orange_mode = False
    


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    with st.spinner('Please wait while processing'):
        #print(minimal)    
        pr = ProfileReport(df,
                        minimal=minimal,
                        explorative=False,
                        dark_mode=dark_mode,
                        orange_mode=orange_mode
                        )
    
    st_profile_report(pr)
    

    
