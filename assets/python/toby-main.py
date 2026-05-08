#Spacy

from vosk import Model, KaldiRecognizer
import pyaudio
from conv import CONV
from TobyTools import tool
import speech_recognition as sr
 

model = Model(r"C:\Users\Femi\Documents\femi\Python\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")

r = KaldiRecognizer(model,16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=8192)
stream.start_stream()

active = False
text = ""
po = 1
print(tool.internetAccess())
if tool.internetAccess() and False:

	print("Using Google speech recognition")			
	r = sr.Recognizer()

	# create a microphone object
	mic = sr.Microphone()

	# create a variable to control when to stop listening
	stop_listening = False

	# start the loop
	while not stop_listening:
	    # listen for speech
	    print("Listening for speech...")
	    with mic as source:
	        r.adjust_for_ambient_noise(source)
	        audio = r.listen(source)

	    # try to transcribe the speech to text
	    print("Transcribing speech to text...")
	    try:
	        text = r.recognize_google(audio)
	        text = text.lower()
	        print(f"Text: {text}")
	        if (text[0:6] == "toby" or text[0:6] == "debbie" or text[0:5]== "derby" or text[0:5] == "to be" or text[0:5]=="gabby" or text[0:5] == "tommy"  or text[0:5] == "bobby" or text[0:7] == "i'll be" or text[0:5] == "kirby" or text[0:6]=="herbie" or text[0:4]=="joey" or "douglas" in text  or text[0:8]=="japanese" or text[0:4] == "john" or text[0:4] == "jack" or text[0:6]=="judges"  or text[0:3] == "job" or text[0:3] == "jav" or text[0:5]=="jones" or text[0:9]== "germany's"):
	        	CONV.conv(text)
	    except sr.UnknownValueError:
	        print("Sorry, I couldn't understand what you said.")
	    except sr.RequestError as e:
	        print("Error transcribing speech to text:")
	        print(e)
				
				


			 		
			
else:
	print("Using Vosk")
	while True:

	 data = stream.read(4096,exception_on_overflow=False)
	 if r.AcceptWaveform(data):	
	 	text = r.Result() 
	 	text = text[14:-3]
	 	print(text)


	 	if (text[0:6] == "toby" or text[0:6] == "debbie" or text[0:5]== "derby" or text[0:5] == "to be" or text[0:5]=="gabby" or text[0:5] == "tommy"  or text[0:5] == "bobby" or text[0:7] == "i'll be" or text[0:5] == "kirby" or text[0:6]=="herbie" or text[0:4]=="joey" or "douglas" in text  or text[0:8]=="japanese" or text[0:4] == "john" or text[0:4] == "jack" or text[0:6]=="judges"  or text[0:3] == "job" or text[0:3] == "jav" or text[0:5]=="jones" or text[0:9]== "germany's"):																					 				
	 		active = True
	 	if active:
	 		CONV.conv(text)
	 		if (text[0:6] == "toby" or text[0:6] == "debbie" or text[0:6] == "jervis" or text[0:4]=="joey" or "douglas" in text  or text[0:8]=="japanese" or text[0:8] == "johnny's" or text[0:8] == "jackie's" or text[0:6]=="judges" or text[0:3] == "job" or text[0:5]=="jones" or text[0:9]== "germany's") and ("in" in text or ("go" in text and "inactive" in text) or "hibernate" in text or (("i " in text or "buy" in text) and ("neat" in text or "need" in text or "meat" in text))):
	 			CONV.hibernate()

	 			active = False

	 	








	 	

		

