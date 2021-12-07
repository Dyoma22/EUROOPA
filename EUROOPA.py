from module1 import*
Capitals={} 
Capitals=dict()
Countries={}
Countries=dict()
Capitals=listt("stranq.txt")
Countries=listt("stolica.txt")


for country in Countries:
	if country in Capitals:
		print("Столица страны"+ country + ":"+Capitals[country])
	else:
		print('В базе нет страны c названием ' + country)

stranq=listt("stranq.txt")
stolica=listt("stolica.txt")