
# # Read an audio file and convert it to text
# ###############################################################################

# import speech_recognition as sr
# r = sr.Recognizer()
# sound = "../Sounds/sound1.wav"

# with sr.AudioFile(sound) as source:
#     # r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
#     audio = r.listen(source)
#     try:
#         text = r.recognize_google(audio)
#         print('Working on...')
#         print("The interlocutor said : "+ text)
#     except:
#         print('Sorry, we could not recognize the audio, try again')

    

    
# Speach Recognition with microphone
##############################################################################

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source: # use the default microphone as the audio source
    
    r.adjust_for_ambient_noise(source)
    print("Adjusting for ambient noise...")
    print("Say something!") # Ask for permission to speak
    audio = r.listen(source) # listen for the user's input

    try :
        text = r.recognize_google(audio) # recognize what the user said
        print('You said  : {}' .format(text))  # display the user's input

    except:
        print('Sorry, could not recognize your voice') # if the user does not speak, the program will say this
