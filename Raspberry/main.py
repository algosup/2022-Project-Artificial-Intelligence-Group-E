#Start this code using the command "streamlit run [this code filename]"

import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development
import random
import tensorflow as tf
from PIL import Image
import shutil
from tensorflow import keras

LOGSIZE = 20
REFRESHDELAY = 1
MODELPATH = "./model_77_accuracy.h5"

dataTemp = {'Timestamp': [],
            'Language' : []}

def getPredictionFromimage(model_path, image_path):
    model_saved = keras.models.load_model(model_path)
    
    img = tf.keras.utils.load_img((image_path), target_size=(500, 128),color_mode='grayscale')
    img_array = tf.keras.utils.img_to_array(img) / 255
    img_array = tf.expand_dims(img_array, 0)

    return model_saved.predict(img_array)

def avoidOverflow():
    if (len(dataTemp['Timestamp'])>LOGSIZE):
        dataTemp['Timestamp'] = dataTemp['Timestamp'][-LOGSIZE:]
        dataTemp['Language'] = dataTemp['Language'][-LOGSIZE:]

def addValue(value):
    dataTemp['Timestamp'].append(time.strftime('%H:%M:%S', time.localtime(time.time())))
    dataTemp['Language'].append(value)

def LanguageSpoken(pred):
    if pred > 0.75:
        return "You are speaking French"
    elif pred > 0.50:
        return "You are speaking mostly French"
    elif pred > 0.25:
        return "You are speaking mostly English"
    else:
        return "You are speaking English"

st.set_page_config(
    page_title="Groupe E Realtime Stats",
    page_icon="📈",
    layout="wide",
)

placeholder = st.empty()

im1 = Image.open('./imageSource.png')
im2 = Image.open('./imageComp.png')


while True:
    with placeholder.container():

        #while the image is the same, no need to analyse it again
        WaitingCheck = False
        try:
            #CHANGE WITH THE TWO IMAGES GENERATED
            im1.close()
            im2.close()
            im1 = Image.open('./imageSource.png')
            im2 = Image.open('./imageComp.png')
            im1.LOAD_TRUNCATED_IMAGES = True
            im2.LOAD_TRUNCATED_IMAGES = True
            WaitingCheck = list(im1.getdata()) == list(im2.getdata())
        except:
            time.sleep(1)
            im1.LOAD_TRUNCATED_IMAGES = True
            im2.LOAD_TRUNCATED_IMAGES = True
            WaitingCheck = list(im1.getdata()) == list(im2.getdata())
        if WaitingCheck:
            time.sleep(REFRESHDELAY)
        else:
            time.sleep(REFRESHDELAY)
            shutil.copy2("./imageSource.png", "./imageComp.png")

            #st.image("./imageComp.png")
            
            #Get the prediction by selecting a model and a image
            prediction = getPredictionFromimage(MODELPATH,"./imageComp.png")
            #Then we add the prediction to the dataframe to display it afterward
            addValue(prediction[0][0])
            df = pd.DataFrame({
                'date' : dataTemp['Timestamp'],
                'Language' : dataTemp['Language']
                })
            #Here we rename the date to be the index in order to display the date bellow the prediction.
            df = df.rename(columns={'date':'index'}).set_index('index')

            #we display which language the AI think we're speaking
            st.markdown("### Graph")
            st.line_chart(df)

            DispValPred = 1-prediction[0][0] if prediction[0][0] < 0.5 else prediction[0][0]

            st.info(LanguageSpoken(prediction[0][0]) + " with a prediction value of "+ str(round(DispValPred*100, 2)) + "%")

            #we limit the number of data in the lists in order not to run out of memory and to be more readable.
            avoidOverflow()
            
