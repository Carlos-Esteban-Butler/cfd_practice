from foamlib import FoamCase
import os

# get path to case
parent_dir = os.path.dirname(os.path.dirname(__file__))
pathToCase = os.path.join(parent_dir, "elbow_cases", "elbow_quad")
# fetch foam case
case = FoamCase(pathToCase) # Load an OpenFOAM case
print(case[0])
for time in case:
    print(time.time)