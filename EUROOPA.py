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
for country in Countries:
	country=input("Enter your country:")
	if country in Capitals:
		print("The capital of country:" +country +" - "+Capitals[country])
	else:
		 print("There is no country in the wiki with name " +country)
		 q=input("Did you want add " +country+ " in Wiki?\nYes or No - ")
	if q=="No":
		print("Goodbye!")
	if q=="Yes":
		print ("Soon!")
		

	
		


		

		 
		 

	


















s=gTTS(text=Countries[0],lang="et",slow=True).save("heli.mp3")
os.system("heli.mp3")


