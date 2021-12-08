Capitals={}
Capitals=dict()
Capitals=["Austria","Azerbaijan","Albania","Andorra","Armenia","Belarus","Belgium","Bulgaria","Bosnia and Herzegovina","Vatican","United Kingdom","Hungary","Germany","Greece","Georgia","Denmark","Ireland","Iceland","Spain","Italy","Kazakhstan","Cyprus","Latvia","Lithuania","Liechtenstein","Luxembourg","Malta","Moldova","Monaco","Netherlands","Norway","Poland","Portugal","RepublicofMacedonia","Russia","Romania","SanMarino","Serbia","Slovakia","Slovenia","Turkey","Ukraine","Finland","France","Croatia","Montenegro","Czech","Switzerland","Sweden","Estonia"]
Countries=["Vein","Baku","Tirana","Andorra la Vella","Yerevan","Minsk","Brussels","Sofia","Sarajevo","Vatican","London","Budapest","Berlin","Athens","Tbilisi","Copenhagen","Dublin","Reykjavik","Madrid","Rome","Astana","Nicosia","Riga","Vilnius","Vaduz","Luxembourg","Valletta","Kishinev","Monaco","Amsterdam","Oslo","Warsaw","Lisbon","Skopje","Moscow","Bucharest","San Marino","Belgrade","Bratis", "lava","Ljubljana","Ankara","Kiev","Helsinki","Paris","Zagreb","Podgorica","Prague","Berne","Stockholm","Tallinn"]

while True:
	print("Добро пожаловать!")
	a=input("Напишите страну или столицу - ")
	if a=="Austria":
		print("Vein")
	elif a=="Azerbaijan":
		print("Baku")
	elif a=="Albania":
		print("Tirana")
	elif a=="Andorra":
		print("Andorra la Vella")
	elif a=="Armenia":
		print("Yerevan")
	elif a=="Belarus":
		print("Minsk")
	elif a=="Belgium":
		print("Brussels")
	elif a=="Bulgaria":
		print("Sofia")
	elif a=="Bosnia and Herzegovina":
		print("Sarajevo")
	elif a=="Albania":
		print("Tirana")
	elif a=="Albania":
		print("Tirana")











for country in Countries:
	if country in Capitals:
		print("Столица страны " + country + ": " + Capitals[country])
	else:
		print("В базе нет страны c названием " + country)


