import MetaNml

runs = MetaNml.subRunNames
with open("runs.txt","wb") as f:
	for i in runs:
		f.write(str(i)+'\n')




