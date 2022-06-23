# 2022-Project-Artificial-Intelligence-Group-E

# The goal of the project

The goal of the project is to build a device that can listen to conversations (in project rooms for instance) and detect when English is spoken or when French is spoken. The device could emit a sound or display different colors based on the language.

# What we used 

To perform the project we used a Raspberry Pi 4 as well as a microphone connected to it to listen to the conversations in order to predict the language spoken thanks to the AI stored on it.

In order to create the [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning), we used [Google Colab](https://colab.research.google.com/?utm_source=scs-index) to be able to retrieve and process the audio data and turn it into spectrograms so that we could train the AI. Here is the link to our [Google Colab](https://colab.research.google.com/drive/1AGPS3GyS9HJcMQ5R2TGQSomvVcMiNvNe?usp=sharing) notebook.

To be able to get the audio data, we use the Mozilla Common Voice Dataset by the way of [Kaggle](https://www.kaggle.com/datasets/mozillaorg/common-voice) for the English datset as well as the
Commun Voice Corpus 9.0 still from the [Mozilla Common Voice Dataset](https://commonvoice.mozilla.org/fr/datasets) for the French datatset.

To be able to store the datasets and the spectrograms, we used [Google Drive](https://drive.google.com/drive/u/2/my-drive) to store the files.

