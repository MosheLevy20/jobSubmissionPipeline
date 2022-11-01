#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)
fileName=$1
target=$2
echo $target
for d in */ ; do
    if [ $d == "QAmetaDir/" ] 
    then
	    continue
    fi
    echo $d
    cp -r $fileName $d$target
    #pwd

    
cd $myWD	
done


















































































































































