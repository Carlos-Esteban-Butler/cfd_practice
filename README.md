# CFD Practice
Home for practicing simulating, running, processing, and analyzing cases in the field of CFD (Computational Fluid Dynamics). The simulations are run using OpenFOAM, a free, open-source CFD software popular among academics and industry alike.  The main components of the codebase are given as directories and are as follows:
1. [cases](/cases): contains the case data, made up of the standard openFOAM inputs, settings, and output files/directories.
2. [analysis_code](/analysis_code): holds the scripts which process and analyze the results of the simulations. The scripts are written in Python3 and make use of the package foamlib for easier data extraction and simulation execution.
3. [results](/results): organizes the results of the analysis and visualizations by case, so that they are more accesible. For example, here you can find screenshots of the grids, videos of the flow, and graphs from the analyses.  

As of 30.06.2025 there is a single case considered, [elbow](/cases/elbow). More will follow as time allows. I mostly base my learning path off of the tutorials found in the [OpenFOAM wiki](https://wiki.openfoam.com/index.php?title=Tutorials) and the examples given in the [OpenFOAM primer](/literature/OFprimer-v2012.1.pdf) written by Tomislav Marić, Jens Höpken, and Kyle G. Mooney.  

None of the resources used in the course of this learning are for commercial purposes and will conform to the licenses set by the creators, most of which follow the [Creative Commons](https://creativecommons.org/) scheme.
