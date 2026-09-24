import geopandas as gpd
import rasterio

def read_boundary(path):
    return gpd.read_file(path)

def find_first_band(directory,band):
    files = sorted(directory.glob(f"*{band}.TIF"))
    if not files:
        raise FileNotFoundError(f"File {band} not found")
    return files[0]

def read_raster(path):
    with rasterio.open(path) as src:
        data = src.read(1)
        profile = src.profile
    return data, profile