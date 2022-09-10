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

    st.title("BITS Assignment 2 - Group 02")

    with st.form(key='searchform'):
        nav1, nav2  = st.beta_columns([2, 1])

        with nav1:
            keyword = st.text_input("Enter the keyword ")

        with nav2:
            st.text("Search ")
            submit_search = st.form_submit_button(label='Search')

        st.success("You searched for {}".format(keyword))


        if submit_search:
            if(keyword in ['Data Mining']):
                #video1 = YouTubeVideo("VsYKqOokgaE")
                #video2 = YouTubeVideo("4l4_BREP6ZI")
                #video3 = YouTubeVideo("ZRZHwn")
                #video4 = YouTubeVideo("bvWDe0z45-E")
                #video5 = YouTubeVideo("6P7ceHFuG-o")
                #video6 = YouTubeVideo("9OjRP0ZLKkk")
                #video7 = YouTubeVideo("VcPWL9Nlozs")
                #video8 = YouTubeVideo("aMfzqHNsLug")
                st.video("https://www.youtube.com/watch?v=6P7ceHFuG-o&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=12")
                st.video("https://www.youtube.com/watch?v=aMfzqHNsLug&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=34")

                #st.markdown(JOB_HTML_TEMPLATE_8.format(display(video1), display(video2), display(video3), display(video4),display(video5), display(video6), display(video7), display(video8)),unsafe_allow_html=True)


            if(keyword in ['Data Mining','clustering']):
                #video9 = YouTubeVideo("9OjRP0ZLKkk")
                #video10 = YouTubeVideo("VcPWL9Nlozs")
                #video11 = YouTubeVideo("aMfzqHNsLug")
                st.video("https://www.youtube.com/watch?v=aMfzqHNsLug&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=34")

                #st.markdown(JOB_HTML_TEMPLATE_3.format(display(video9), display(video10), display(video11)), unsafe_allow_html=True)

            if(keyword in ['Data Mining', 'Decision Tree']):
                #video12 = YouTubeVideo("VsYKqOokgaE")
                #video13 = YouTubeVideo("4l4_BREP6ZI")
                #video14 = YouTubeVideo("ZRZHwn")
                #video15 = YouTubeVideo("bvWDe0z45-E")
                #video16 = YouTubeVideo("6P7ceHFuG-o")
                st.video("https://www.youtube.com/watch?v=6P7ceHFuG-o&list=PLLspfyoOYoQcI6Nno3gPkq0h5YSe81hsc&index=12")

                #st.markdown(JOB_HTML_TEMPLATE_4.format(display(video12), display(video13), display(video14), display(video15), display(video16)), unsafe_allow_html=True)




if __name__ == '__main__':
    main()
