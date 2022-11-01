#!/bin/bash

module load openmpi/4.1.2
export OMPI_MCA_btl=tcp,self
export OMPI_MCA_mtl=^ofi

alias moe="cd /sci/labs/nmandelker/moe_levy_hurcs"
alias mp="cd /sci/labs/nmandelker/moe_levy_hurcs/ramses/post"
#alias mkout="mkdir output; mv output_* output; mkdir data"
alias cans="scancel -u moe_levy_hurcs"
alias qs="squeue | grep moe_levy"
alias mpyenv=". /sci/labs/nmandelker/moe_levy_hurcs/f90nmlEnv/bin/activate"

#namelist dimension outdir...in future add time and mem 
function prep {
 echo "namelistDir dim outputDir" 
 cd /sci/labs/nmandelker/moe_levy_hurcs/ramses/
 cd post
 echo "1"
 mkdir "$3"
 cd ..
 cp bin/ramses"$2" post/"$3"
 cp "$1"/namelist.nml post/"$3"
 cd post
 cp mRead3D/* "$3"
 cp -r QA "$3"
 #cp produceDat.py "$3"
 #cp amr2map "$3"
 cd "$3"
 echo "2"
 mkdir output
 mkdir data
 cd output
 echo "#!/bin/bash" >> exec.sh
 echo "#SBATCH -N 8" >> exec.sh
 echo "#SBATCH -n 256" >> exec.sh
 #echo "#SBATCH --mem=20G" >>exec.sh
 echo "#SBATCH --time=24:0:0" >> exec.sh
 echo "mpirun ../ramses"$2" ../namelist.nml" >> exec.sh
}

function letsgo {
moe
. f90nmlEnv/bin/activate
mp
cp -r automation $1
cd $1
}
