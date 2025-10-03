#!/bin/bash

cd SIMS
mkdir -p reordered/{base,adv,666,646}/{supercoarse,coarse,medium,fine,superfine}/{CFD,MESH}


configs=('base' 'adv' '666' '646')
refinements=('supercoarse' 'coarse' 'medium' 'fine' 'superfine')
for refinement in ${refinements[@]}; do
    cd $refinement
    for config in ${configs[@]}; do
        #cd $config
        cp -rf $config/* ../reordered/$config/$refinement/.
    done
    cd ..
done

echo "Deleting supercoarse, coarse, medium, fine and superfine directories!!"
rm -rf supercoarse/ coarse/ medium/ fine/ superfine/

mv reordered/* .
rm -rf reordered
