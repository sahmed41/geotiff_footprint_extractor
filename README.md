# GeoTIFF Footprint Extractor & CityGML Downloader

A lightweight Python tool that extracts geographic bounding box footprints (`WGS 84` / `EPSG:4326`) from GeoTIFF orthophoto tiles (such as German State Survey DOP20 datasets), converts projected metric bounds (`UTM Zone 32N / EPSG:25832`) into standard WKT polygons, and automatically queries and downloads matching 3D building models via the **HFT Stuttgart CityGML API**.

---

## Features

- **Automated Footprint Extraction:** Computes exact 4-corner bounding polygons in Well-Known Text (`WKT`) format.
- **Geographic CRS Reprojection:** Converts projected coordinate systems (e.g. UTM Easting/Northing in meters) to Geographic CRS (WGS 84 Longitude/Latitude decimal degrees) required by web services.
- **Smart CRS Fallback & Name Parsing:** Detects German DOP naming conventions (e.g., `dop20rgb_32_...` for Baden-Württemberg UTM 32N) when GeoTIFF headers lack embedded CRS metadata.
- **Automated CityGML Downloader:** URL-encodes WKT bounding polygons and streams `.gml` 3D building datasets directly from the HFT Stuttgart CityGML web service.

---