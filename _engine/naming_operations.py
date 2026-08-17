import os
import re
from rasterio.crs import CRS

def infer_crs_from_path(file_path):
    """Detects German DOP naming conventions (e.g. dop20rgb_32_...)"""
    filename = os.path.basename(file_path)
    # Check for UTM zone pattern like _32_
    match = re.search(r'_32_', filename)
    if match:
        return CRS.from_epsg(25832)  # ETRS89 / UTM Zone 32N (Standard for BW)
    return None