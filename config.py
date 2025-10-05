"""
Configuration for Google Solar API Detection System
"""

import os
from typing import Dict, Any

# St. Tammany Parish specific settings
ST_TAMMANY_CONFIG = {
    'center_lat': 30.4,
    'center_lon': -90.1,
    'bounds': {
        'north': 30.7,
        'south': 30.1,
        'east': -89.7,
        'west': -90.5
    },
    'assessor_url': 'https://atlas.geoportalmaps.com/st_tammany',
    'parish_name': 'St. Tammany Parish',
    'state': 'Louisiana'
}

# Output settings
OUTPUT_CONFIG = {
    'base_dir': 'google_solar_output',
    'images_dir': 'building_images',
    'data_dir': 'data',
    'reports_dir': 'reports'
}

def get_config() -> Dict[str, Any]:
    """
    Get the complete configuration dictionary
    """
    return {
        'st_tammany': ST_TAMMANY_CONFIG,
        'output': OUTPUT_CONFIG
    }