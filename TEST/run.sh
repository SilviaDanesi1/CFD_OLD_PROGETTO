#! /bin/bash 
# Nproc = 4

# TODO: copy different config files in CONFIG directory (This may be dumb, but is the smartest structure i could think of)
# ConfigCoarse=CONFIG/coarse/config.cfg
# ConfigMedium=CONFIG/medium/config.cfg
# ConfigFine=CONFIG/fine/config.cfg
# Create all the directories
mkdir -p {supercoarse,coarse,medium,fine}/{base,adv,666,646}/{CFD,MESH}
# mkdir -p CFD,MESH

# NOT NEEDED AT THE MOMENT  (Kept just because)
# # Copy config file (Hp different one for coarse, med and fine)
# cp $ConfigCoarse coarse/{base,adv,666,646}/CFD/.
# cp $ConfigMedium medium/{base,adv,666,646}/CFD/.
# cp $ConfigFine  fine/{base,adv,666,646}/CFD/.

# Write in "mesh.py" the grid type and "config", copy the configs and running syms
configs=(base adv 666 646)
refinements=(supercoarse coarse medium fine)

for ((i = 0; i < 4; i++)); do
  cd ${refinements[i]}
  for ((j = 0; j < 4; j++)); do
    cd ${configs[j]}
    cd MESH/
    cp ../../../CONFIGS/mesh.py .
    sed  -i -e "s|##REFINEMENT|refinement=str(\"${refinements[i]}\")|" mesh.py
    sed  -i -e "s|##CONFIG|config=str(\"${configs[j]}\")|" mesh.py
    python3 mesh.py > mesh.log
    echo "Access to" ${refinements[i]}  ${configs[j]}
    pwd
    cd ../CFD
    cp ../../../CONFIGS/config.cfg .
    if [[ i -gt 0 ]]; then
        echo "Copying restart file from coarser mesh"
        sed -i -e "s|RESTART_SOL= NO|RESTART_SOL=YES|" config.cfg
        cp ../../../${refinements[i-1]}/${configs[j]}/CFD/restart_flow.dat .
    fi
    echo "Running case" ${refinements[i]}  ${configs[j]} 
    (time mpirun -n 4 SU2_CFD config.cfg) > screen.log 2>&1
  ##touch restart_flow.dat
    cd ../../
  done
  cd ../
done

# TESTS TO CHECK (All passed, kept them just in case)
# head coarse/adv/MESH/mesh.py
# head coarse/adv/MESH/datas.py
# python3 coarse/adv/MESH/mesh.py
