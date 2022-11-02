# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc
import requests
from IPython.display import YouTubeVideo
import os
import subprocess


JOB_HTML_TEMPLATE_4 = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
 border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
<h6>{}</h4>
</div>
"""


JOB_HTML_TEMPLATE_3 = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
 border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
</div>
"""

JOB_HTML_TEMPLATE_5 = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
 border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
</div>
"""

JOB_HTML_TEMPLATE_8 = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
 border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
<h5>{}</h4>
<h4>{}</h4>
<h5>{}</h4>
</div>
"""

JOB_DES_HTML_TEMPLATE = """
<div style='color:#fff'>
{}
</div>
"""


def main():

 	st.title("Testing")

 	with st.form(key='searchform'):
 		nav1, nav2 = st.beta_columns([2, 1])

 	with nav1:
 		keyword = st.text_input("Enter the keyword ")

 	with nav2:
 		st.text("Search ")
 		submit_search = st.form_submit_button(label='Search')

 	st.success("You searched for {}".format(keyword))


 	if submit_search:
 		if(keyword in ['Data Mining']):
 			st.video("https://www.youtube.com/watch?v=6P7ceHFuG-o&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=12")
 			st.video("https://www.youtube.com/watch?v=aMfzqHNsLug&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=34")


 	if(keyword in ['Data Mining','clustering']):
 		st.video("https://www.youtube.com/watch?v=aMfzqHNsLug&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=34")

 	if(keyword in ['Data Mining', 'Decision Tree']):
 		st.video("https://www.youtube.com/watch?v=6P7ceHFuG-o&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=12")




if __name__ == '__main__':
 main()
