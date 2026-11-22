# Vienna Urban Mobility Lab — data and attribution

This directory contains the OSM- and Overture-derived input and output datasets used for the atlas. They are distributed as machine-readable GeoPackages and GeoJSON. **© OpenStreetMap contributors; Overture Maps Foundation; data from TomTom; Microsoft Global ML Building Footprints**, where the corresponding sources occur.

OpenStreetMap attribution: https://www.openstreetmap.org/copyright  
ODbL 1.0: https://opendatacommons.org/licenses/odbl/1-0/  
Overture source attribution: https://docs.overturemaps.org/attribution/

## Map and graph extracts

| File | Features | Source and processing |
|---|---:|---|
| `osm_buildings_part_1.gpkg` | 122,478 | OSM-tagged Overture Buildings; Vienna extract; reprojected to EPSG:3416; split on original fid. |
| `osm_buildings_part_2.gpkg` | 128,735 | Remaining OSM-tagged buildings; same source and processing. Both parts together contain 251,213 records. |
| `microsoft_ml_buildings_from_project.gpkg` | 7,698 | Microsoft-tagged features of the same Overture Buildings layer; extracted by source, EPSG:3416. |
| `overture_roads_for_maps.gpkg` | 120,910 | Overture Transportation: 119,483 OSM-tagged and 1,427 TomTom-tagged road features; reprojected to EPSG:3416. |
| `osm_road_graph_source.gpkg` | 40,828 | OSM-tagged road subset used for the locally constructed graph; EPSG:4326. |
| `osm_rail_for_maps.gpkg` | 11,467 | OSM railway extract, EPSG:3416. |
| `osm_water_for_maps.gpkg` | 940 | OSM water polygons, EPSG:3416. |
| `concept_corridors.geojson` | 3 | Exploratory locally routed paths derived from the road graph, EPSG:4326; not engineered transit alignments. |
| `wien_station_records.gpkg` | 14 | Stadt Wien stop records used as route anchors, EPSG:4326; Datenquelle: Stadt Wien, CC BY 4.0. These are not validated entrances. |

The QGIS project metadata identify the Buildings and Transportation inputs as **Overture 21 October 2026, ODbL 1.0**, acquired 18 November 2026. Rail and water metadata identify hosted OSM data dated 19 October 2026. Sources were geographically selected, reprojected, filtered by source and/or routed. The Microsoft-tagged extract was taken from the Overture layer: the licence of Microsoft's separate direct-download repository must not be substituted for the ODbL licence stated for this Overture theme. More provenance and limitations: [`../docs/SOURCE_AUDIT_2026_11_22.md`](../docs/SOURCE_AUDIT_2026_11_22.md).

## Method and limitations

[`../scripts/reproduce_routes.py`](../scripts/reproduce_routes.py) verifies the three road-path lengths using the graph subset and station anchors in this directory. It requires QGIS Python, NetworkX and SciPy. The graph uses 2 m endpoint rounding and the largest strongly connected component; missing crossings and level information remain unresolved. These data do not establish pedestrian accessibility, construction feasibility or travel-time savings.

Retain the OSM, Overture and relevant source notices on reuse. The ODbL applies to the applicable database and derivative database; copyright in the atlas text and design is not automatically ODbL. When ODbL section 4.6 applies, recipients must be offered the derivative database or the permitted alterations file/method and additional contents as specified there, free of charge online. This source note is a technical review, not independent legal advice.
