import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    speak("News for today, Let's proceed")
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=******************"  #Use your own API key 
    news = requests.get(url).text
    news_obj = json.loads(news) #string to python object
    print(news_obj["articles"])
    artic = news_obj["articles"]
    for article in artic:
        speak(article["title"])
        if(article== list(artic)[-1]):
            speak("Thats all")
            continue
        speak("Moving on..")
        
    speak("Thanks for listening")
