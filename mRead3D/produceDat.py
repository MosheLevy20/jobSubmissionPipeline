import subprocess
import sys
thiss,folderStart =  sys.argv
folderStart = int(folderStart)
def genNum(n):
	n = str(n)
	s = "00000"
	s = s[len(n):]
	return s+n
def run(n, out, kind):
	s = ["./amr2cube","-inp", "output/output_"+genNum(n),"-out",out,"-typ ",kind,"-xmi", "0.0","-xma","1.0","-ymi","0.0","-yma","1.0","-zmi","0.0","-zma","1.0","-fil","bin"]
	#print(s)
	command = subprocess.Popen(s, stdout=subprocess.PIPE)
	output = command.communicate()[0]

	print(output)


for i in range(folderStart,10+folderStart):

    run(i,"data/testRho"+str(i)+".dat","1")

    run(i,"data/testP"+str(i)+".dat","5")

    run(i,"data/testScl"+str(i)+".dat","7")

    run(i,"data/vx"+str(i)+".dat","2")
    run(i,"data/vy"+str(i)+".dat","3")
    run(i,"data/vz"+str(i)+".dat","4")
