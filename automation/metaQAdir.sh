#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)
mkdir QAmetaDir
for d in */ ; do
    if [ $d == "QAmetaDir/" ] 
    then
	    continue
    fi
    echo $d
    cd $d
    #pwd

    cd QA
    for i in *; do
	if [[ $i == *.csv ]] || [[ $i == *.pdf ]] || [[ $i == *.gif ]] || [[ $i == *.png ]]
	then
	echo $i
	cp $i $myWD/QAmetaDir/${d::-1}$i
	fi

    
    
done
cd $myWD	
done


















































































































































