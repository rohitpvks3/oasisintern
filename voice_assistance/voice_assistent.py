import speech_recognition as sr # type: ignore
import pyttsx3 # type: ignore
import datetime
import webbrowser

def speak(text):
    """
    Convert text to speech.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """
    Capture audio from the microphone and return it as a string.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Request Error")
            return "None"

    return query

def respond_to_query(query):
    """
    Respond to a specific voice command.
    """
    query = query.lower()

    if 'hello' in query:
        speak("Hello! How can I help you?")
    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")
    elif 'search' in query:
        speak("What do you want to search for?")
        search_query = get_audio()
        if search_query != "None":
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Searching for {search_query} on the web.")
    else:
        speak("I am sorry, I don't understand that command.")

def main():
    speak("Voice assistant activated. How can I help you?")
    
    while True:
        query = get_audio()
        if query == "None":
            continue
        if 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break
        respond_to_query(query)

if __name__ == "__main__":
    main()
