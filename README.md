# willunga_wt

Repository for water table mapping of the Willunga Basin, South Australia.

This repository contains scripts used for the analysis of hand drawn maps, results presented in the following publication:

'Using expert participation to evaluate the accuracy and variability of hand-drawn water table mapping' Sarah K. Marshall, Okke Batelaan, Tanah Velterop & Luk Peeters

The useful scripts for this publication include:

'shapefile_from_contours.ipynb' --> this is a script to pull each each shapefile of hand-drawn contours (digitised using ArcGIS) and then create a new shapefile of the extent of the drawn contours, because not all participants drew contours for the entire Sub-basin extent. This shapefile is used to mask the rasters used in the analysis in the 'saving_rasters' script.

'saving_rasters.ipynb' --> the rasters generated for each hand-drawn map (generated using ArcGIS TopoToRaster tool) are reprojected and saved as rasters and arrays.  

'analysis_hand_drawn_maps_functions.ipynb' --> a series of functions used to analyse the resultant hand-drawn water table map rasters.

'figures_hand_drawn_paper.ipynb' --> a series of figures used for the hand-drawn analysis and in the final paper. Some figures were not used in the paper.

'figures_paper_residuals.ipynb' --> an important part of the hand-drawn analysis, was the analysis of the residuals. However, this was complicated in the previous script and so the analysis of the residuals specifically is drawn out in this script.

