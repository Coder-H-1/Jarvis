import os,sys, pyttsx3,pywhatkit, wikipedia, requests, speech_recognition as sr, random, datetime

os.system("cls")
os.system("title J.A.R.V.I.S")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you...")
        audio = r.listen(source)
    try:
        print("Initializing...")
        query = r.recognize_google(audio , language="en-US")
        print(f"User : {query}")
    except:
        query = "none"
    
    query = str(query)
    return query.lower()

def Timeline():
    hour = None
    
class Text:
    """
    It takes sentences as text\n
    An Example to use this Class is given below\n
    >>> Text("Your Text").google() <<<
    """
    def __init__(self,text=None, condition=None):
        self.text = text
        self.condition = condition

    def speak(self):
        audio = self.text
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice' , voices[0].id)
        engine.setProperty('rate' , 210)
        print("JARVIS : " + audio)
        engine.say(audio)
        engine.runAndWait()

    def Google(self):
        query = str(self.text)
        query = query.replace('google search ' , '')
        query1 = query.replace(' ' , "+")
        pywhatkit.search(query1)
        try:
            Text(query , 'google').Wiki()
        except:
            Text("Sorry, The Results got are not speakable").speak()
    
    def CData(self):
        try:
            data = requests.get("https://www.google.com/")
            return "Connected"
        except:
            return "Not Connected"

    def Wiki(self):
        def __speaker__(results ,condition):
            if condition == None:
                Text("According to Wikipedia").speak()
                Text(results).speak()

            elif condition == "google":
                Text("According to Internet").speak()
                Text(results).speak()
            else:
                Text("According to Wikipedia").speak()
                Text(results).speak()

        query = str(self.text)
        condition = self.condition
        if condition != None:
            pass
        elif condition == None:
            condition = "casual"
        query = query.replace("wikipedia search " , "")
        try:
            results = wikipedia.summary(query , sentences=2)
            __speaker__(results, condition)
        except:
            try:
                results = wikipedia.summary("who is " + query , sentences=2)
                __speaker__(results, condition)
            except:
                try:
                    results = wikipedia.summary("what is " + query , sentences=2)
                    __speaker__(results, condition)     
                except:
                    try:
                        results = wikipedia.summary("whom is " + query , sentences=2)
                        __speaker__(results, condition)
                    except:
                        try:
                            results = wikipedia.summary("where is " + query , sentences=2)
                            __speaker__(results, condition)
                        except:
                            Text(f"Sorry, Couldn't fetch any data {query} from Wikipedia").speak()

    def Chat(self):
        query = str(self.text)
        hellohi = ['hi' , 'hello' , 'huh' , 'hello friday' , 'oh hello' , 'oh hello friday' , 'hola' , 'hola amigo' , 'bonjour']

        hellohi_reply = [
            'Oh hello Sir', 'Hello Sir' , f'Hello {os. getlogin()}', 'Oh hello sir, How are you Doing',
            'Hello Sir, How are you?']

        how_send = ['how are you' , 'how are you doing' , 'how about you' , 'how are you friday']
        how_return = ["I'm fine" , "I'm fine Sir" , "Fine Sir" , "I'm good" , "I'm good Sir" , "I'm very well Sir" , "well Sir"]

        work_send = ['what are you doing' , 'what you doing']
        work_reply = ['Sir, I am listening and answering to you.' , 'I am speaking to you']

        iam_send =  ["i am fine" , "i am good" , "mai thik hu" , "not good"]
        iam_reply = ['Totally Fine' , "That's good" , "That's Fine" , "Oh, Great!" , "Great!" , "Good."]

        iam2_send = ["i am not fine" , "i am very good"]
        iam2_reply = ["Oh?, What happened?" , "That's not good" , "OH!" , "Sorry to hear that but what happened?" , "What happened?"]

        Nothing = ['Nothing' , "What can you do" , 'nothing at all']
        Nothing_reply = ['Nothing', 'nothing at all' , 'Absolutely Nothing']

        if query in hellohi:
            Text(random.choice(hellohi_reply)).speak()

        elif query in Nothing:
            Text(random.choice(Nothing_reply)).speak()
        
        elif query in iam2_send:
            Text(random.choice(iam2_reply)).speak()

        elif query in how_send:
            Text(random.choice(how_return)).speak()

        elif query in work_send:
            Text(random.choice(work_reply)).speak()

        elif '*' in query:
            Text("Please don't try to abuse").speak()

        elif query in iam_send:
            Text(random.choice(iam_reply)).speak()

def Welcome():
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    if int(hour) >= 0 and int(hour) < 12:
            Text('Good Morning Sir').speak()
    elif int(hour) >= 12 and int(hour) < 18:
            Text('Good Afternoon Sir').speak()
    elif int(hour) >= 18 and int(hour) < 25:
        Text('Good Night Sir').speak()

Welcome()
Text("What can i do for you Sir")
def Responder():
    query = takecommand().lower()
    if 'wikipedia search' in query or 'define' in query or 'defination of ' in query:
        Text(query).Wiki()
    elif 'google search' in query:
        Text(query).Google()
    elif 'is my net connected' in query:
        data = Text().CData()
        if data == "Connected":
            Text("Yes Sir, It's connected").speak()
        else:Text("No Sir, It's not connected").speak()

    else:
        Text(query).Chat()
while True:
    Responder()