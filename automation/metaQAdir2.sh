#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName> 
myWD=$(pwd)
mkdir QAmetaDir2
for d in */ ; do
    if [ $d == "QAmetaDir/" ] 
    then
	    continue
    fi
    echo $d
    cd $d
    #pwd
    cp -r QA $myWD/QAmetaDir2/${d::-1}

cd $myWD	
done

















































































































































