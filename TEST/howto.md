OK so, you want to run many syms without doing the same 4 operations 1000 times, here's how to do that FOR FREE!!!

We firse need a TEST directory structured as below, where in coarse, fine and medium directory there ae the 3 diffs config files.
```
.
├── CONFIGS
│   ├── coarse
│   │   └── config.cfg
│   ├── fine
│   │   └── config.cfg
│   ├── medium
│   │   └── config.cfg
│   └── mesh.py
└── run.sh
```

we then have to make executable the run.sh with ```chmod u+x run.sh```, and finally just ```./run.sh```, this will automatically create alle the 12 meshes and run ALL the syms in a ordered way.

Further improvements can be made by adding a _postprocess.py_ to extract the important datas.
The final tree will be like this (I'm missing the flow.vtu etc, but the idea is the same)
```
.
├── CONFIGS
│   ├── coarse
│   │   └── config.cfg
│   ├── fine
│   │   └── config.cfg
│   ├── medium
│   │   └── config.cfg
│   └── mesh.py
├── coarse
│   ├── 646
│   │   ├── CFD
│   │   └── MESH
│   │       ├── mesh.py
│   │       └── mesh.su2
│   ├── 666
│   │   ├── CFD
│   │   └── MESH
│   │       ├── mesh.py
│   │       └── mesh.su2
│   ├── adv
│   │   ├── CFD
│   │   └── MESH
│   │       ├── mesh.py
│   │       └── mesh.su2
│   └── base
│       ├── CFD
│       └── MESH
│           ├── mesh.py
│           └── mesh.su2
├── fine
│   ├── 646
:   :
:   
├── howto.md
├── medium
│   ├── 646
:   :
:   
└── run.sh
```


In order to simplify postprocessing we thougt to switch the order of the 'tree' and set configType/refinementLevel, in order to make the reorder.sh file run we have to ```chmod u+x reorder.sh``` and then run ```./reorder.sh```
> [!NOTE]
> Is needed  to be out of the SIMS directory or you need to comment the cd SIMS in the first line !!
