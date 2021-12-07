from random import*
def listt(file:str)->list:
	file=open(file,"r")
	list_=[]
	for stroka in file:
		list_.append(stroka.strip())
	file.close()
	return list_