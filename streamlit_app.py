# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc
import requests
from IPython.display import YouTubeVideo
from os.path import join
from math import sqrt
from sklearn.metrics import mean_squared_error

import os
import cv2
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
        nav1, nav2, nav3  = st.beta_columns([3, 2, 1])

        with nav1:
            links = st.text_input("Enter the links")

        with nav2:
            searchedName = st.text_input("Enter the keyword ")

        with nav3:
            st.text("Search ")
            submit_search = st.form_submit_button(label='Search')

        st.success("You searched for {}".format(searchedName))


        if submit_search:
            for link in links.split(","):
                src_vid = cv2.VideoCapture(link)
                process(src_vid)
                for searchedName in os.listdir(image_frames1):
                    if searchedName != '.DS_Store':
                        findDelDuplBw1(searchedName, image_frames1)
                if (searchedName in get_text()):
                    st.video(link)



def findDelDuplBw1(searchedName, bwDir):
    # Join path to orginal image that we are looking duplicates
    searchedImg = join(bwDir, searchedName)
    # print(searchedImg)
    for (j, cmpImageName) in enumerate(os.listdir(bwDir)):
        if cmpImageName != '.DS_Store':
            if cmpImageName == searchedName:
                # If name in bwDir is equal to searched image - pass. I don't wan to deletde searched image in bw dir
                print("same file, skipping")
            else:
                cmpImageBw = join(bwDir, cmpImageName)
                print(searchedName + ": fail : " + cmpImageBw)

                try:
                    # Open image in bwDir - The searched image
                    searchedImageBw = np.array(cv2.imread(searchedImg, cv2.IMREAD_GRAYSCALE))
                    # Open image to be compared
                    cmpImage = np.array(cv2.imread(cmpImageBw, cv2.IMREAD_GRAYSCALE))
                    # Count root mean square between both images (RMS)
                    rms = sqrt(mean_squared_error(searchedImageBw, cmpImage))
                    # print (searchedImg, cmpImageName, rms)
                except Exception as e:

                    print(e)
                    continue

                if rms < 3:
                    # Delete compared image in BW dir
                    os.remove(cmpImageBw)
                    print(searchedImg, cmpImageName, rms)

def get_text():
    for i in os.listdir(image_frames1):
        if i != '.DS_Store':
            print(str(i))
            my_example = Image.open(image_frames1 + "/" + i)
            text = pytesseract.image_to_string(my_example, lang='eng')
    return text


def process(src_vid):
    index = 0
    while src_vid.isOpened():
        ret, frame = src_vid.read()
        if not ret:
            break
        name = 'image_frames1/frame' + str(index) + '.png'

        # save every 50th frame
        if index % 50 == 0:
            print('Extracting frames' + name)
            cv2.imwrite(name, frame)
        index = index + 1
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    src_vid.release()
    cv2.destroyAllWindows()


def files():
    try:
        os.remove(image_frames1)
    except OSError:
        pass
    if not os.path.exists(image_frames1):
        os.makedirs(image_frames1)

    src_vid = cv2.VideoCapture('InputVedio/Physics_Rotation_Introduction_to_Rotational_Motion_PPT.mp4')
    return (src_vid)

if __name__ == '__main__':
    image_frames1 = 'image_frames1'
    main()
