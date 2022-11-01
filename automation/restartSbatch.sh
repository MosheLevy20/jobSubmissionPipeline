#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)

cd 
source .bashrc

#activate venv
cd /sci/labs/nmandelker/moe_levy_hurcs/ 
. f90nmlEnv/bin/activate

cd $myWD

#python writeRuns.py #writes the names (gotten from meta nml) of the subruns to txt



#calls pynml and modifies the namelist in each subfolder according to meta nml
python restartNml.py 100


#submits a job for each subfolder
#echo '#!/bin/bash' >> 'abort.sh'
for i in */ ; do
    if [ $i == "QAmetaDir/" ] 
    then
            continue
    fi 
	cd $i 
	cd output
	jid=$(sbatch exec.sh)
	jidi=${jid##* }

	cd ..
	jid2=$(sbatch  --dependency=afterok:$jidi mkdat.sh 100)
	jidi2=${jid2##* }
	jid3=$(sbatch  --dependency=afterok:$jidi2 mkQA.sh)
	cd ..
	echo "scancel "$jidi >> 'abort.sh'
done





















































































































































