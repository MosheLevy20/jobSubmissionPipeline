from MetaNml import *

for run_index, subRunName in enumerate(subRunNames):
	with open(subRunName+'/QA/cool_lengths.py', 'w') as f:
            f.write("lcools="+str(lcools))
            f.write('\n')
            f.write("tcools="+str(tcools))
