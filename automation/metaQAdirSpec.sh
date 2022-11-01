#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)
python writeRuns.py #writes the names (gotten from meta nml) of the subruns to a file
runs=() #load names into array
while read line; do
runs+=($line)
done < 'runs.txt'

rm runs.txt
for d in  ${runs[@]}; do
        mkdir QAmetaDirSpec/$d
done
for d in ${runs[@]};
do  
        cd $d
        
        cp -r QA/$1 $myWD/QAmetaDirSpec/${d::-1}

        cd ..
done

cp MetaNml.py QAmetaDirSpec/

sbatch zipper.sh QAmetaDirSpec















































































































































