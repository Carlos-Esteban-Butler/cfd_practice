from foamlib import FoamCase
import os

cwd = os.getcwd()
print(cwd)
case = FoamCase("../elbow_cases/elbow_quad") # Load an OpenFOAM case
print(case[0])
for time in case:
    print(time.time)