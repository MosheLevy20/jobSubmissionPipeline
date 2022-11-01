#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)

cd 
source .bashrc

cd /sci/labs/nmandelker/moe_levy_hurcs/
. f90nmlEnv/bin/activate

cd $myWD
python writeRuns.py #writes the names (gotten from meta nml) of the subruns to a file
runs=() #load names into array
while read line; do
runs+=($line)
done < 'runs.txt'

rm runs.txt

#prepare a folder to run each subrun in 
for i in ${runs[@]}; 
do
	prep patch/$1 3d $i
done


cd ../..
#mkdir $2Meta #make meta folder and move all subrun folders into it

#cp $myWD/* $2Meta

for i in ${runs[@]};
do
	echo $i
	mv $i $myWD/
done

cd $myWD/

#calls pynml and modifies the namelist in each subfolder according to meta nml
python modNamelists.py


#submits a job for each subfolder
echo '#!/bin/bash' >> 'abort.sh'
for i in ${runs[@]};
do  
	cd $i 
	cd output
	jid=$(sbatch exec.sh)
	jidi=${jid##* }

	cd ..
	jid2=$(sbatch  --dependency=afterok:$jidi mkdat.sh 0)
	# jidi2=${jid2##* }
	# jid3=$(sbatch  --dependency=afterok:$jidi2 mkQA.sh)
	cd ..
	echo "scancel "$jidi >> 'abort.sh'
done





















































































































































