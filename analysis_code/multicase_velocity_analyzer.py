from foamlib import FoamCase

case = FoamCase("../elbow_cases/elbow_quad") # Load an OpenFOAM case
for time in case:
    print(time.time)