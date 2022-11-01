#!/bin/bash
#SBATCH --mem=10G
#pyfile=$1 numstart=$2

python ${1}.py $PWD ${PWD##*/} $2 $3

