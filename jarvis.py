import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            print("Audio captured")
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', " ")
                print(instruction)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return instruction

def play_Jarvis():
    instruction = input_instruction()
    print(instruction)
    
    if "play" in instruction:
        song = instruction.replace('play', " ")
        talk("Playing" + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%p')
        talk('Current time is ' + time)
    
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Today's date is " + date)
    
    elif 'how are you' in instruction:
        talk('I am fine, how are you')
    
    elif 'what is your name' in instruction:
        talk('I am Jarvis. What can I do for you?')
    
    elif 'who is' in instruction:
        human = instruction.replace('who is ', " ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
    
    else:
        talk('Please repeat')

play_Jarvis()
