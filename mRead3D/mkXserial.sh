#!/bin/bash
#TODO make more general
mkdir ${1}plotData${2}


sbatch mkXSub.sh $1 $2
    

