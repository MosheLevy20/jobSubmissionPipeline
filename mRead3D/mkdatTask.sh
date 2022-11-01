#!/bin/bash
#SBATCH --time=24:0:0
for i in {1..200..10}; 
do	
	num=$i
	echo $num
	jid=$(sbatch mkdatSub.sh $num )
        jidi=${jid##* }
	echo $jidi>>mkdatlist.txt
	
done

