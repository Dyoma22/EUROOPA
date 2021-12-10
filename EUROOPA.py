from module1 import*
from random import*
from gtts import gTTS
Capitals={}
Capitals=dict()
Capitals["Austria"]="Vienna"
Capitals["Albania"]="Tirana"
Capitals["Belgium"]="Brussels"
Capitals["Czechia"]="Prague"
Capitals["Poland"]="Warsaw"
Capitals["Portugal"]="Lisbon"
Capitals["Germany"]="Berlin"
Capitals["Sweden"]="Stockholm"
Capitals["Spain"]="Madrid"
Capitals["Serbia"]="Belgrade"
Capitals["Norway"]="Oslo"
Capitals["Moldova"]="Chisinau"
Capitals["Greece"]="Athens"
Capitals["Bulgaria"]="Sofia"
Capitals["France"]="Paris"
Capitals["Finland"]="Helsinki"
Capitals["Estonia"]="Tallinn"
Countries=["Austria","Albania","Belgium","Czechia","Poland","Portugal","Germany","Sweden","Spain","Serbia","Norway","Moldova","Greece","Bulgaria","France","Finland","Estonia"]
while True:
	w=input("Функция:\nНайти страну - 1\nДобавить страну - 2")
	if w=="1":
		count()
	elif w=="2":
		country()




		
		

	
		


		

		 
		 

	


















s=gTTS(text=Countries[0],lang="et",slow=True).save("heli.mp3")
os.system("heli.mp3")


