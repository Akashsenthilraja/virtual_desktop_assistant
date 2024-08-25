import speech_recognition as sr
from requests_html2 import HTMLSession
import speak  # Ensure this module is correctly defined

def spech_to_text():
    r = sr.Recognizer()
    voice_data = ''

    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            voice_data = r.recognize_google(audio)
            return voice_data

        except sr.UnknownValueError:
            speak.speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak.speak("No internet connection, please check your connection.")
        except Exception as e:
            speak.speak(f"An error occurred: {str(e)}")

    return voice_data
