# 2022-Project-Artificial-Intelligence-Group-E

# The goal of the project

The goal of the project is to build a device that can listen to conversations (in project rooms for instance) and detect when English is spoken or when French is spoken. The device could emit a sound or display different colors based on the language.

# What we used 

To perform the project we used a Raspberry Pi 4 as well as a microphone connected to it to listen to the conversations in order to predict the language spoken thanks to the AI stored on it.

In order to create the [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning), we used [Google Colab](https://colab.research.google.com/?utm_source=scs-index) to be able to retrieve and process the audio data and turn it into spectrograms so that we could train the AI. Here is the link to our [Google Colab](https://colab.research.google.com/drive/106yJAkhgMO-FBhq3uEyNG9jtAzCzUVf6?usp=sharing) notebook.

> Our model is a Binary classification model, which means that it will predict whether the language spoken is English or French by the way of 0 or 1.

> 0 is for English and 1 is for French.

To be able to get the audio data, we use the Mozilla Common Voice Dataset by the way of [Kaggle](https://www.kaggle.com/datasets/mozillaorg/common-voice) for the English dataset as well as the
Common Voice Corpus 9.0 still from the [Mozilla Common Voice Dataset](https://commonvoice.mozilla.org/fr/datasets) for the French dataset.

To be able to store the datasets and the spectrograms, we used [Google Drive](https://drive.google.com/drive/u/2/my-drive) to store the files.  


# Link to the other Google Colab notebooks

We used other Google Collab notebooks to perform the data preprocessing:    

Notebook of the EN data preprocessing [here](https://colab.research.google.com/drive/1PfovKMU0Hb0WhUldsybmvaXD1vCEkBz9?usp=sharing)

Notebook of the FR data preprocessing [here](https://colab.research.google.com/drive/19v3hLpmHs5z-1vMLICxcxRSMHJg1fGxD?usp=sharing)

# Link to the documents

[Functional Specification](https://github.com/algosup/2022-Project-Artificial-Intelligence-Group-E/blob/documents/Documents/Functional_Specifications.md)  

[Technical Specification](https://github.com/algosup/2022-Project-Artificial-Intelligence-Group-E/blob/documents/Documents/Technical_Specifications.md)
