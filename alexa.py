import speech_recognition as sr
import pyttsx3
import requests
import json
import random

API_KEY = "2a4d786761a3181d0b902bbc4556d0f5"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

r = sr.Recognizer()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    
def unfunnyDadJokes():
    jokes = [
    "Did you hear about the cartoonist found dead at his home? Details are sketchy.",
    "What did the 0 say to the 8? Nice belt!",
    "What's E.T. short for? Because he's only got little legs!",
    "Last night my wife and I watched two DVDs back to back. Luckily I was the one facing the TV.",
    "A sandwich walks into a bar. The barman says: 'sorry we don't serve food here'",
    "Where did Napoleon keep his armies? Up his sleevies!",
    "Did you hear about the guy who had his left side cut off? He's all right now!",
    "I slept like a log last night. Woke up in the fireplace!",
    "I went to a seafood disco last week! Pulled a mussel!",
    "What do you call a man with a rubber toe? Roberto!",
    "Two cannibals are eating a clown. One says to the other 'Does this taste funny to you?'",
    "I fear for the calendar. It's days are numbered.",
    "Did you hear about the hungry clock? It went back four seconds.",
    "I heard there is a new shop called Moderation. They have everything in there.",
    "An invisible man married an invisible woman. The kids were nothing to look at.",
    "I gave away all my used batteries today. Free of charge!",
    "I remember the first time I saw a universal remote control. I thought to myself 'well this changes everything'.",
    "What did the police officer say to the belly button? You're under a vest!",
    "Did you hear about the kidnapping at school? It's ok, he woke up.",
    "Did you hear about the giant that threw up? It's all over town!",
    "I stayed up all night wondering where the sun went. Then it dawned on me.",
    "Have you heard the joke about the butter? I better not tell you, it might spread!",
    "What do you call a seagull that flies over the bay? A bagel.",
    "What is the difference between an angry circus owner and a Roman barber? One is a raving showman, the other is a shaving Roman.",
    "Have you ever tried to eat a clock? It's very time-consuming.",
    "England doesn't have a kidney bank. But it does have a Liverpool.",
    "Yesterday I accidentally swallowed some food coloring. The doctor says I'm ok, but I feel like I've dyed a little inside.",
    "Time flies like an arrow. Fruit flies like a banana.",
    "I don't trust stairs because they're always up to something.",
    "I wasn't going to get a brain transplant. But then I changed my mind.",
    "Two hats were hanging on a hat rack. One said 'You stay here, I'll go on a head.'",
    "Did you hear about the girl who quit her job at the doughnut factory? She was fed up with the hole business.",
    "What do you call a fly without wings? A walk.",
    "My cat was just sick on the carpet. I don't think he's feline well.",
    "Without geometry life is pointless.",
    "People are making apocalypse jokes like there is no tomorrow!",
    "What's Forrest Gump's computer password? 1forrest1.",
    "Did you hear the story about the haunted lift? It really raised my spirits!",
    "I dreamt about drowning in an ocean made of orange soda last night. It took me a while to work out it was just a Fanta sea.",
    "I'd tell you a chemistry joke but I know I wouldn't get a reaction.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What kind of magic do cows believe in? Moodoo!",
    "What did the late tomato say to the other tomatoes? Don't worry, I'll ketchup.",
    "Can I watch TV? Yes, but don't turn it on.",
    "Why didn't the skeleton cross the road? Because he had no guts!",
    "What did the fish say when it swam into a wall? Damn!",
    "Have you heard of a music group called Cellophane? They mainly wrap.",
    "My dog has no nose. How does it smell? Awful!",
    "What's the advantage of living in Switzerland? Well, the flag is a big plus!",
    "There's a new type of broom in stores. It's sweeping the nation!",
    "A red and blue ship have collided in the Caribbean sea. Apparently the survivors are marooned.",
    "A police officer caught two kids playing with a firework and a car battery. He charged one and let the other off.",
    "What do you call a group of killer whales playing instruments? An Orca-stra!",
    "I'm reading a book about anti-gravity. It's impossible to put down.",
    "Why was the big cat disqualified from the race? Because it was a cheetah!",
    "What do you call a cow with no legs? Ground beef.",
    "A steak pun is a rare medium well done.",
    "What did the mountain climber name his son? Cliff.",
    "Milk is the fastest liquid on earth. It's pasteurized before you even see it!",
    "Struggling to think of what to buy someone for Christmas? Get them a fridge and watch their face light up when they open it."
]
    
    rand = random.randint(0, len(jokes) - 1)
    printedJoke = jokes[rand] 
    print(printedJoke)
    SpeakText(printedJoke)
    

def calculate():
    a  = int(input("Bir sayi giriniz : "))    
    SpeakText("Please enter a number  ")
    b = int(input("Bir sayı daha giriniz : "))
    SpeakText("Please enter another number ")
    sum = a + b
    abssub = abs(a-b)
    if(b != 0):
        division = a / b
    else:
        print("0'a bölünmez") 
        SpeakText("You can't divide to 0")
    multiply = a * b
    power = pow(a,b)
    
    SpeakText(f"Summary = {sum} , Absolute value is {abssub} , Division {division} , Multiply {multiply} and power is {power}")
    
def get_weather():
    try:
        with sr.Microphone() as source2:
            SpeakText("Please say the city name.")
            print("Lütfen şehir adını söyleyin:")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            city = r.recognize_google(audio2)
            city = city.lower()
            print(f"Şehir: {city}")
            SpeakText(f"Fetching the weather for {city}.")
            
            url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                main = data['main']
                weather = data['weather'][0]

                temperature = main['temp']
                description = weather['description']

                print(f"{city} için hava durumu:")
                print(f"Sıcaklık: {temperature}°C")
                print(f"Hava durumu: {description}")

                SpeakText(f"The temperature in {city} is {temperature} degrees Celsius with {description}.")
            else:
                print("Şehir bulunamadı.")
                SpeakText("City not found.")
    except sr.UnknownValueError:
        print("Anlamadım, lütfen tekrar deneyin.")
        SpeakText("Sorry, I didn't catch that. Please try again.")

def Main():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Lütfen komut verin: Weather , Calculator , Joke")
                SpeakText("Please say Weather, Calculator, Joke.")
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say: ", MyText)
                SpeakText("You said " + MyText)

                if "weather" in MyText:
                    SpeakText("You selected option Weather. Fetching the weather information.")
                    get_weather()
                elif "calculator" in MyText:
                    SpeakText("You selected option Calculator .")
                    calculate()
                elif "joke" in MyText:
                    SpeakText("You selected option Joke.")
                    print("Option THREE is selected.")
                    unfunnyDadJokes()
                else:
                    SpeakText("Invalid command, please say Weather, Calculator  or Joke.")
                    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))        
        except sr.UnknownValueError:
            print("Unknown error occurred")
            SpeakText("Sorry, I didn't catch that. Please try again.")
Main()