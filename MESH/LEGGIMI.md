Some references & explanations.

After some looks to a mesh configuration with a very long channel we can say that at around 100mm far from the inlet the wake effects are negligible, so I set L = 19*l.

In order to catch in a decent way the beahviour of the flow around the corners we do need to have the mesh size near the bodies fixed and very small, this dimension fixes the number of fan (FAN_SIZE), parametrized as $\frac{\pi*r}{2} = MESH_SIZE_BODYES*FAN_SIZE$, $r$ is in our file defined as ```BL_OPTIONS['Thickness']```
This value il limited since the cell closer to the body otherwise are too small.
I also parametrized the number of rows, may be quetioned, but I thought it may be useful.

There are now 3 meshes for  each configuration:
configCoarse.su2
configMed.su2
configFine.su2
The 3 meshes are made by using ```SCALE = [2, 1/2, 1/3]```




The config in the meshes are respecively:
- BASE, just 4 elements
    - coarse ~ 50k  elems
    - med    ~ 100k elems
    - fine   ~ 400k elems
- ADV , just 6 elements
- 666 , 3 cols of 6 elems
- 646 , no need to describe it 

