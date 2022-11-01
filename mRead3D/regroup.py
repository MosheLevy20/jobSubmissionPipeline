#get params and do case by case for each plot type
#
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
import csv
import glob

try:
    thiss, pyfile, var =  sys.argv
except Exception as e: 
    thiss, pyfile =  sys.argv

def save_csv(file,x):
	print(file)
	with open(file, 'wb') as fp:
		writer = csv.writer(fp)
		for index,i in enumerate(x):
			writer.writerow(i)


def load_csv(file):
    with open(file, 'r') as f:
        data = [row for row in csv.reader(f.read().splitlines())]
    return data

variableNames = ["Rho","P","T"]

if pyfile=="QA/QAplotsNdata":

	folder = "QA/QAplotsNdataplotData"+str(var)
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	ts = []
	variable = []
	for i in file_list:
		data = load_csv(i)
		ts += data[0]
		variable += data[1]
	plt.plot(ts,variable,'.',label="simulated")
	plt.ylabel(variableNames[var])
	plt.xlabel("t [s]")
	plt.legend()

	plt.savefig("QA/"+variableNames[var]+"vtQA.pdf",format='pdf')
	plt.clf()



elif pyfile=="QA/dat2gif": #fix
	folder = "QA/dat2gifplotData"+str(var)
	file_list = glob.glob(folder+'/*.png') # Get all the pngs in the current directory
	list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
	os.system('convert @{} {}.gif'.format(file_list,variableNames[var]+".gif")) 


elif pyfile=="QA/PDFs":
	#both types
	folder = "QA/PDFsplotData"
	file_list = glob.glob(folder+'/*.csv')

	list.sort(file_list, key=lambda x: int(x.split('temp_')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	
	rho_list = [i for i in file_list if "Rho" in i]
	T_list = [i for i in file_list if "Temperature" in i]

	data = []
	for i in rho_list:
		data += load_csv(i)

	save_csv("QA/PDFsGroupedRho.csv",data)

	data = []
	for i in T_list:
		data += load_csv(i)

	save_csv("QA/PDFsGroupedT.csv",data)





elif pyfile=="QA/phaseDiagram": #fix
	folder = "QA/phaseDiagramplotData"
	file_list = glob.glob(folder+'/*.png') # Get all the pngs in the current directory
	list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
	os.system('convert @{} {}.gif'.format(file_list,"phaseDiagram.gif")) 



elif pyfile=="QA/coldGasFraction":
	folder = "QA/coldGasFractionplotData"
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	data = []
	for i in file_list:
		data += load_csv(i)

	save_csv("QA/coldGasvtQAgrouped.csv",data)


elif pyfile=="QA/mixingMetric":
	folder = "QA/mixingMetricplotData"
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	data = []
	for i in file_list:
		data += load_csv(i)

	save_csv("QA/mixingvtQAgrouped.csv",data)


elif pyfile=="QA/TvtCellplotData":
	folder = "QA/TvtCellplotDataplotData0"
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	data = []
	for i in file_list:
		data += load_csv(i)

	save_csv("QA/TvtCellgrouped0.csv",data)

	folder = "QA/TvtCellplotDataplotData1"
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	data = []
	for i in file_list:
		data += load_csv(i)

	save_csv("QA/TvtCellgrouped1.csv",data)


elif pyfile=="QA/v_rms":

	folder = "QA/v_rmsplotData"+str(var)
	file_list = glob.glob(folder+'/*.csv')
	list.sort(file_list, key=lambda x: int(x.split('group')[1].split('.csv')[0])) # Sort the images by #, this may need to be tweaked for your use case
	ts = []
	variable = []
	for i in file_list:
		data = load_csv(i)
		ts += data[0]
		variable += data[1]
	plt.plot(ts,variable,'.')
	plt.ylabel("$v_\{rms\}/c_s$")
	plt.xlabel("t/t\{cool\}")
	plt.legend()

	plt.savefig("QA/vrmsVt.pdf",format='pdf')
	plt.clf()





# elif pyfile=="QA/phaseCell": #fix, need to differentiate between jindex
# 	folder = "QA/phaseCellplotData"
# 	file_list = glob.glob(folder+'/*.png') # Get all the pngs in the current directory
# 	list.sort(file_list, key=lambda x: int(x.split('_')[1].split('.png')[0])) # Sort the images by #, this may need to be tweaked for your use case
# 	os.system('convert @{} {}.gif'.format(file_list,"phaseCell.gif")) 


#v_rms



