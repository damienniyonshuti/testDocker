from calendar import c
from turtle import color
import streamlit as st 
st.set_page_config(layout="wide")
import pandas as pd
from st_aggrid import AgGrid, GridUpdateMode, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

#Styles 

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#f2690d;">
  <a class="navbar-brand" href="" target="_blank">Drought Analytica</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://droughtmonitor.unl.edu/" target="_blank">U.S Drought Monitor</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="https://droughtreporter.unl.edu/map/" target="_blank">Drought Impact Reporter</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

#hide "Made with Streamlit" footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
          #  MainMenu {visibility: hidden;}
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

##Header
st.markdown("<h1 style='text-align: center; color: #CE6D1B;'>DM-DIR Table</h1>", unsafe_allow_html=True)

# Functions

@st.cache
def data_upload():
    df = pd.read_csv("./data/DIR_DM_alllevels_noDuplicates2.csv",low_memory=False)
    df.drop(['Id','End_Date_Known', 'Post_Date','State_Abbr', 'IsPositive', 'None', 'MapDate', 'run', 'weekstart','FIPS_State','FIPS_County', 'FIPS_City', 'Level', 'ValidStart', 'ValidEnd'], inplace=True, axis=1)
    return df

df=data_upload()


gd = GridOptionsBuilder.from_dataframe(df)
gd.configure_pagination(enabled=True)
gd.configure_default_column(editable=False,groupable=True)
# st.subheader("Select Type")
sel_mode = st.sidebar.radio('Selection Type', options = ['single', 'multiple'], key="")
gd.configure_selection(selection_mode=sel_mode,use_checkbox=True)
gridoptions = gd.build()
grid_table = AgGrid(df,gridOptions=gridoptions,
                    update_mode= GridUpdateMode.SELECTION_CHANGED,
                    height = 500,
       
                    allow_unsafe_jscode=True,
                    #enable_enterprise_modules = True,
                    theme = 'material')

                    
                       

sel_row = grid_table["selected_rows"]
st.subheader("Summary")
st.write(sel_row)



st.markdown("""

<footer class="page-footer font-small white style="background-color:#f2690d">

  <!-- Copyright -->
  <div class="footer-copyright text-center py-3">© 2020 Copyright:
    <a href="/"> MDBootstrap.com</a>
  </div>
  <!-- Copyright -->

</footer>



""",unsafe_allow_html=True)