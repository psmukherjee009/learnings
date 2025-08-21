import streamlit as st
import configparser
# Dashboard Code to display like ipad



class ExtendedEnvInterpolation(configparser.ExtendedInterpolation):
  """Interpolation which expands environment variables in values."""
  def before_get(self, parser, section, option, value, defaults):
    value = os.path.expandvars(value)
    # print(value)
    return super().before_get(parser, section, option, value, defaults)
  m = st.markdown("""
  <style>
  div.stButton > button:first-child {
    // background-color: #ce1126;
    // color: black;
    height: 8em;
    width: 8em;
    border-radius:8px;
    border:1px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
  }

  div.stButton > button:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }
  div.stButton > button:active {
`   position:relative;
    top:3px;
  }
  </style>""", unsafe_allow_html=True)

  st.markdown("<h1 style='text-align: center;'>Select an APP</h1>", unsafe_allow_html=True)
  st.markdown("<p></p>", unsafe_allow_html=True)
  st.markdown("<p></p>", unsafe_allow_html=True)
  st.markdown("<p></p>", unsafe_allow_html=True)
