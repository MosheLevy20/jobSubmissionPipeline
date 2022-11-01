#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)
targetD=$1
targetF=$2

echo $target
for d in */ ; do
    if [ $d == "QAmetaDir/" ] 
    then
	    continue
    fi
    echo $d
    cd $d$targetD
    sbatch $targetF
    #pwd


    
cd $myWD	
done


















































































































































