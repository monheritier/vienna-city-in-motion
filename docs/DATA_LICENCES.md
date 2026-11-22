# Data sources, attribution and licences

These notices describe the included extracts and the study's inputs; they are not a legal opinion. Retain source attribution when using or publishing the maps.

## OpenStreetMap and Overture

© OpenStreetMap contributors, https://www.openstreetmap.org/copyright, Open Database License 1.0, https://opendatacommons.org/licenses/odbl/1-0/. © Overture Maps Foundation; transportation data includes data from TomTom. See https://docs.overturemaps.org/attribution/. Relevant ODbL inputs and modifications in `data/`:

- `osm_road_graph_source.gpkg`: 40,828 OSM-sourced road records from an Overture-derived extract. `concept_corridors.geojson`, `wien_station_records.gpkg` and `scripts/reproduce_routes.py` provide the corresponding outputs, non-OSM anchors and transformation method.
- `overture_roads_for_maps.gpkg`: 120,910 road records, including OSM and TomTom sources.
- `osm_buildings_part_1.gpkg` and `osm_buildings_part_2.gpkg`: OSM-sourced building extract, split by original `fid` <= 125606 versus > 125606; 122,478 and 128,735 features respectively.
- `osm_water_for_maps.gpkg` and `osm_rail_for_maps.gpkg`: OSM water and railway extracts; a track is not evidence that a particular service operates.

These data were clipped, filtered, reprojected or used for local routing. Before public distribution, publish the relevant source/derived database or alterations and method as required, make the URL accessible, and accompany any externally shared PDF with it. Independent review of all ODbL obligations has not been completed. The Microsoft-tagged Overture building extract is included as `microsoft_ml_buildings_from_project.gpkg` (7,698 features). It was extracted from the Overture dataset, not downloaded directly from the Microsoft repository. Figure-by-figure origin and source-specific redistribution conditions have not been independently cleared; do not assert complete third-party rights clearance.

## BEV

Datenquelle: BEV, modified by TerraLab, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. BEV DLM Bauwerke, 25 March 2025 edition: https://www.bev.gv.at/Services/Produkte/Digitales-Landschaftsmodell/Bauwerke.html. The five BEV files are geographically clipped extracts. The `HOEHE_OBJEKT_MEDIAN` field underlies the massing; a median is not an exact architectural roof reconstruction.

## Stadt Wien

Datenquelle: Stadt Wien, https://data.wien.gv.at/, CC BY 4.0. Includes U-Bahn planning lines and stations, dated public transport snapshots and stop records, administrative districts and green space; filters and styling have been modified. The planning dataset is https://www.data.gv.at/katalog/datasets/5982a27f-28a4-4f40-a1cc-5cb650400c50. Dataset opening-date attributes may be historical, not commitments. Stop records may represent platforms or services rather than entrances.

## GHSL and Copernicus

European Commission Joint Research Centre, GHS-POP R2023A, CC BY 4.0, https://doi.org/10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE. The raster itself is not included; the 2025 surface is a projection. The district comparison also uses official City counts. Copernicus DEM GLO-30: Copernicus DEM © DLR e.V. 2010–2014 and © Airbus Defence and Space GmbH 2014–2018, provided under COPERNICUS by EU and ESA; https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM. The DSM itself is not included.

## Original contributions

Copyright and licensing of the author's original writing, graphics and design are separate from dataset licences. No additional blanket licence is asserted here. Open-data licences remain applicable to their respective data.
