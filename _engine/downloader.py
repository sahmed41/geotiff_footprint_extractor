import os
import urllib.parse
import requests

BASE_URL = "https://citygml.hft-stuttgart.de/citygml?wktPolygon="

def build_citygml_url(wkt_polygon_str):
    """Encodes the WKT polygon string safely into the query parameter."""
    encoded_wkt = urllib.parse.quote(wkt_polygon_str)
    return f"{BASE_URL}{encoded_wkt}"

def download_citygml(wkt_polygon_str, output_path, timeout=60):
    """Downloads the CityGML file for the given WKT polygon."""
    url = build_citygml_url(wkt_polygon_str)
    print(f"Requesting data from: {url}")

    response = requests.get(url, stream=True, timeout=timeout)
    response.raise_for_status()

    # Ensure output directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"File successfully saved to: {output_path}")
    return output_path