
#!/bin/bash

#usage: bash metaSbatch.sh <patchName> <metaRunName>
myWD=$(pwd)
python writeRuns.py #writes the names (gotten from meta nml) of the subruns to a file
runs=() #load names into array
while read line; do
runs+=($line)
done < 'runs.txt'

rm runs.txt

mkdir QAmetaDir3
for d in ${runs[@]};
do
        cd $d

        cp -r QA $myWD/QAmetaDir3/${d::-1}

        cd ..
done

cp MetaNml.py QAmetaDir3/

sbatch zipper.sh QAmetaDir3

