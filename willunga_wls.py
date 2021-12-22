# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:30:39 2021

@author: mar886
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Set up data

SAWaCoFolder = r'C:\Users\mar886\WaterTableProject\Willunga\input_data\McLaren_SAWaterConnect'
constr_details = pd.read_csv(os.path.join(SAWaCoFolder, constructiondetails))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Import well data



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Import groundwater level data