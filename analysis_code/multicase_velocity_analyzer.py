from foamlib import FoamCase
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

# get path to case
parent_dir = os.path.dirname(os.path.dirname(__file__))
pathToCases = os.path.join(parent_dir, "elbow_cases")
# and fetch foam cases
cases = [
    {"name": "case_tri", "case": FoamCase(os.path.join(pathToCases, "elbow_tri"))},
    {"name": "case_quad", "case": FoamCase(os.path.join(pathToCases, "elbow_quad"))},
    {"name": "case_quad_refined", "case": FoamCase(os.path.join(pathToCases, "elbow_quad_refined"))}
    ]

# function to process data by gathering time and averaged velocities in a list
cutOffTime = 3 # can choose a time to cutoff the processing. -1 corresponds to no cutoff
def calcAvgU (case):
    t = []
    avgU = []
    for time in case:
        if time.time == 0: 
            continue
        elif time.time == cutOffTime:
            break
        t.append(time.time)
        rawU = time["U"].internal_field
        twodU = rawU[:, :-1] # cut off z component of U, since working in 2d
        avgU.append((np.mean(twodU, axis=0)))
        
    avgU = np.array(avgU)
    return t, avgU[:,0], avgU[:,1]

# run the function for each case and save the result, then translate the data to a dataframe
plotDF = ""
for case in cases:
    case["t"], case["avgUx"], case["avgUy"] = calcAvgU(case["case"])
    tempDFx = pd.DataFrame({"Case": np.full((len(case["t"])), case["name"]),
                            "Direction": np.full((len(case["t"])), "X"),
                            "Time [s]": case["t"],
                            "Average Velocity [m/s]": case["avgUx"],
                            })
    tempDFy = pd.DataFrame({"Case": np.full((len(case["t"])), case["name"]),
                            "Direction": np.full((len(case["t"])), "Y"),
                            "Time [s]": case["t"],
                            "Average Velocity [m/s]": case["avgUy"],
                            })
    if isinstance(plotDF, str): plotDF = pd.concat([tempDFx, tempDFy])
    else: plotDF = pd.concat([plotDF, pd.concat([tempDFx, tempDFy])])
    
# plot the cases
sns.set_theme() # set the plot theme
sns.relplot(
    data=plotDF, col="Direction",
    x="Time [s]", y="Average Velocity [m/s]", kind="line", hue="Case"
)

plt.show()