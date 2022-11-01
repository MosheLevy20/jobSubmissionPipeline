import MetaNml
patch = MetaNml.patch
runName = MetaNml.runName
with open("commandVars.txt","wb") as f:
	f.write(patch)
	f.write(' ')
	f.write(runName)





