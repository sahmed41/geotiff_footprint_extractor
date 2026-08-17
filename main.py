import os
from _engine.coordination_operation import get_geotiff_geographic_wkt
from _engine.downloader import download_citygml

def main():
    tif_path = r"data\dop20rgb_32_507_5407_1_bw_2024.tif"
    
    # Generate output CityGML filename matching the TIFF name
    base_name = os.path.splitext(os.path.basename(tif_path))[0]
    output_gml_path = os.path.join("downloads", f"{base_name}.gml")

    # 1. Get Geographic WKT Polygon
    print("Extracting geographic footprint...")
    wkt_polygon = get_geotiff_geographic_wkt(tif_path)
    print(f"WKT Footprint: {wkt_polygon}\n")

    # 2. Download CityGML file
    print("Downloading CityGML file...")
    download_citygml(wkt_polygon, output_gml_path)

if __name__ == "__main__":
    main()