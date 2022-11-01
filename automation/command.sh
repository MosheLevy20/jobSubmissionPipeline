#!/bin/bash
python writeCommandVars.py
read patch runName < 'commandVars.txt'
echo $patch
echo $runName

rm commandVars.txt

bash metaSbatch.sh $patch $runName

python writeCoolingScales.py
