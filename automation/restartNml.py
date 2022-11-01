import f90nml
from MetaNml import *
import sys
thiss,restartN =  sys.argv
for run_index, subRunName in enumerate(subRunNames):
	edit = f90nml.read(subRunName+'/namelist.nml')
	edit["run_params"]["nrestart"] = int(restartN)
    
        noutput = edit["output_params"]["noutput"]
        edit["output_params"]["noutput"]=int(noutput)+int(restartN)
        touts = edit["output_params"]["tout"]
        deltat = float(touts[1])-float(touts[0])
        print(float(deltat)*float(restartN))
        for index, i in enumerate(touts):
            touts[index] += float(restartN)*float(deltat)

        edit["output_params"]["tout"]=touts
	f90nml.write(edit, subRunName+'/namelist.nml', force=True)
