# import python text to speech
import pyttsx3

# create an object
engine = pyttsx3.init()

# using an object
engine.say("Hello World")
engine.say("I'm talking in the rate of " + str(engine.getProperty('rate')))

'''RATE'''
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 100)
print(engine.getProperty('rate'))
engine.say("Hello World")
engine.say("I'm talking in the rate of " + str(rate))


'''VOLUME'''
volume = engine.getProperty('volume')
print(volume)

'''VOICE'''
voice = engine.getProperty('voices')
print(voice)
engine.setProperty('voice', voice[1].id)
# voice 0 is for male
# voice 1 is for female

'''SAVING VOICE TO A FILE'''
engine.save_to_file('Hello World', 'test.mp3')

engine.runAndWait()