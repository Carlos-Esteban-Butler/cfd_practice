from foamlib import FoamCase
import numpy as np
import os

# get path to case
parent_dir = os.path.dirname(os.path.dirname(__file__))
pathToCases = os.path.join(parent_dir, "elbow_cases")
# fetch foam cases
case_tri = FoamCase(os.path.join(pathToCases, "tri"))
case_quad = FoamCase(os.path.join(pathToCases, "elbow_quad"))
case_quad_refined = FoamCase(os.path.join(pathToCases, "elbow_quad_refined"))

# function to process data by gathering time and averaged velocities in a list
def calcAvgU (case):
    t = []
    avgU = []
    for time in case:
        if time.time == 0: 
            continue
        elif time.time == 5:
            break
        t.append(time.time)
        rawU = time["U"].internal_field
        twodU = rawU[:, :-1] # cut off z component of U, since working in 2d
        avgU.append((np.mean(twodU, axis=0)).tolist())
    return t, avgU

print(calcAvgU(case_quad))