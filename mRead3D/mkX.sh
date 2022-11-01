#!/bin/bash
#TODO make more general
mkdir ${1}plotData${2}

runs=()
for i in {1..200..10}; 
do	
	num=$i
	#inum=$(( $i*10 ))
	#num=$(( $i+1 ))
	echo $num
	jid=$(sbatch mkXSub.sh $1 $num $2)
    jidi=${jid##* }
	echo $jidi>>joblists/mk${2}list.txt
	runs+=($jidi)
done
sbatch --dependency=afterany:$(echo ${runs[*]} | tr ' ' ,) regroup.sh $1 $2


