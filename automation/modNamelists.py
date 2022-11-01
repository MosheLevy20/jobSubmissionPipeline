import f90nml
from MetaNml import *

for run_index, subRunName in enumerate(subRunNames):
	edit = f90nml.read(subRunName+'/namelist.nml')
	for i in parameter_master_list:
		paramsi = eval(i)
		for p in paramsi: #add equivalent loop for each param type
			val = eval(p)
			edit[i][p] = val[run_index]

	f90nml.write(edit, subRunName+'/namelist.nml', force=True)
