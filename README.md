# Nature Energy
# Why we need a standardized state of health deﬁnition for electric vehicle battery packs -- a proposal for energy- and capacity-based metrics

Supplementary python code for the publication. Analyze charging data from state of the art electric vehicles.
Derive curves for vehicle level differential voltage analysis (DVA) and deeper aging assessment.

## Associated Article
Please also check the associated article available online published with npj Clean Energy:
[Link to paper](https://doi.org/10.1038/s44406-025-00010-8)
 
## Features
* Calculation of DVA from timeseries data
* Availabilty of vehicle data
* Filtering methods
* Notebooks for displaying data in paper format

## Project Structure
    ├── data           <- must be created by user, download files from mediatum (link below)
    │   │
    │   ├── font    <- fonts for the figures (STIX)
    │   │
    │   ├── Tesla    <- vehicle data for a Tesla Model 3 (LFP) and two Tesla Model Y (NMC)
    │   │
    │   ├── Cupra    <- vehicle data for five Cupra Borns
    │   │
    │   ├── Taycan    <- vehicle data for two Porsche Taycans
    │   │
    │   └── VW       <- cell, halfcell and vehicle data (mutliple measurements)
    │
    ├── figures    <- generated figures are saved here
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the category, and a short description 
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to load data for further processing
    │   │   
    │   ├── filtering       <- Filtering methods to reduce the noise in DVA/ICA
    │   │
    │   ├── visualization  <- Scripts to create visualizations
    │   │    
    │   └── voltage_capacity_analysis <- Scripts to extract the DVA/ICA from timeseries data
    │
    ├── .gitignore
    │
    ├── LICENSE
    │
    ├── README.md
    │	
    └── requirements.txt

## Requirements

The following requirements are to be met:
* python 3.11.9


## Installation

1. clone repo into directory
```console
git clone https://github.com/TUMFTM/nature_soh.git
```  
2. install libraries via the requirements.txt
```console
pip install -r requirements.txt
```  
3. download data from mediaTUM and place into data folder:
```
https://mediatum.ub.tum.de/1765567
```

## Contributing and Support

For contributing to the code please contact:  

[Philip Bilfinger](mailto:philip.bilfinger@tum.de)<br/>
**[Institute of Automotive Technology](https://www.mos.ed.tum.de/en/ftm/home/)**<br/>
**[Technical University of Munich, Germany](https://www.tum.de/en/)**

## Versioning

V0.1 

## Authors

Philip Bilfigner

## License
 
We are very happy if you choose this code for your projects and provide all updates under GNU LESSER GENERAL PUBLIC LICENSE Version 3 (29 June 2007). Please refer to the license file for any further questions about incorporating these scripts into your projects.
We are looking forward to hearing your feedback and kindly ask you to share bugfixes, improvements and updates on the files provided.
