import rasterio
from rasterio.crs import CRS
from rasterio.warp import transform_geom
from shapely.geometry import box, mapping, shape
from shapely import wkt
from .naming_operations import infer_crs_from_path

def get_geotiff_geographic_wkt(tif_path, default_epsg=25832, decimals=6):
    with rasterio.open(tif_path) as src:
        bounds = src.bounds
        native_crs = src.crs

        # Fallback if no CRS tag is embedded
        if native_crs is None:
            native_crs = infer_crs_from_path(tif_path) or CRS.from_epsg(default_epsg)
            print(f"Warning: No CRS embedded in file. Defaulting to {native_crs}.")

        # Create bounding box in source coordinates
        native_polygon = box(bounds.left, bounds.bottom, bounds.right, bounds.top)

        # Reproject to Geographic WGS 84 (EPSG:4326)
        target_crs = CRS.from_epsg(4326)
        transformed_dict = transform_geom(
            src_crs=native_crs,
            dst_crs=target_crs,
            geom=mapping(native_polygon)
        )
        
        geo_polygon = shape(transformed_dict)
        return wkt.dumps(geo_polygon, rounding_precision=decimals)