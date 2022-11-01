#!/bin/bash

bash mkdatTask.sh $1
runs=()
while read line; do
runs+=($line)
done < 'mkdatlist.txt'
echo $runs
sbatch --dependency=afterok:$(echo ${runs[*]} | tr ' ' ,) mkQA.sh
#rm mkdatlist.txt
