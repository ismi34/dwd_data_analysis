import pandas as pd
import numpy as np
import geopandas as gpd
from pathlib import Path

def make_bbox(vector_path):
    """
    Create a bounding box from a vector file and give a list of coordinates.
    """
    # Read the vector file using geopandas
    vector = gpd.read_file(vector_path)
    # Ensure the vector data is in a projected coordinate system
    vector = vector.to_crs(epsg=4326)  # Convert to WGS 84 if necessary
    # Calculate the bounding box
    bounds = np.round(vector.total_bounds, 2)   # Round to 2 decimal places 
    
    return bounds

    