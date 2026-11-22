# Source audit — 22 November 2026

## Buildings actually used in the Vienna building layer

The metadata embedded in the QGIS project for `V7 buildings` identifies **Overture Maps buildings, 21 October 2026, ODbL 1.0**. Its history records acquisition using `fetch_overture` on 18 November 2026 followed by a reprojected GeoPackage. The current layer has 258,911 records: 251,213 attributed to OpenStreetMap and 7,698 to Microsoft ML Buildings. The source field is feature attribution, not a direct licence declaration per feature.

The Overture attribution page consulted on 22 November 2026 states **Buildings theme: ODbL**, with attribution to Overture Maps Foundation, © OpenStreetMap contributors and Microsoft Global ML Building Footprints. Preserve all relevant source notices: https://docs.overturemaps.org/attribution/ . Overture release documentation: https://docs.overturemaps.org/blog/2026/10/21/release-notes .

The Microsoft direct repository's current licence file states CLDA Permissive 2.0, understood as CDLA Permissive 2.0: https://github.com/microsoft/GlobalMLBuildingFootprints/blob/main/LICENSE . That is a different distribution from the Overture building theme. Do not relabel the Overture-derived building extract as though it were downloaded directly under Microsoft repository terms. On the available project metadata, retain the Overture theme ODbL notice for the extract. The figure-by-figure export history and original publisher release manifest were not independently reconstructed; this is not legal certification.

The new `data/microsoft_ml_buildings_from_project.gpkg` contains all 7,698 Microsoft-tagged records of `V7 buildings`. Native QGIS extraction preserved attributes and geometries; the GeoPackage keys rows by fid_gpkg and preserves the old fid field. The two OSM parts together contain all 251,213 OSM-tagged records. All three are filtered extracts of the same project layer, not independent direct Microsoft/OSM downloads.

## Roads and map extracts

QGIS metadata identifies **Overture transportation, 21 October 2026, ODbL 1.0**, and attributes © OpenStreetMap contributors, Overture Maps Foundation and TomTom. The source layer has 119,483 OpenStreetMap-tagged and 1,427 TomTom-tagged segments, 120,910 total. `data/overture_roads_for_maps.gpkg` holds the copied road layer; `data/osm_road_graph_source.gpkg` holds the filtered routing subset. `data/osm_water_for_maps.gpkg`, `data/osm_rail_for_maps.gpkg`, the two OSM building parts and `data/concept_corridors.geojson` are also included. Inputs were clipped, filtered, reprojected or locally routed; see `docs/METHODS.md` and `scripts/reproduce_routes.py`.

## ODbL publication requirements

The PDF is a Produced Work, distinct from the database: public uses carry applicable attribution obligations, while section 4.4 requires share-alike for qualifying derivative databases and section 4.6 sets out the permitted means to make the underlying derivative database or qualifying alterations and reconstruction method available. These conditions depend on the facts and the licence; neither every image nor an independent collective database is automatically itself a derivative database. Legal text: https://opendatacommons.org/licenses/odbl/1-0/ .

At the time of this 22 November 2026 audit, the files were **local only** and no public repository URL had been verified. If this archive is later hosted publicly, validate the actual public access to applicable extracts/alterations, attribution and methodology, under the relevant ODbL provisions; retain access and include the real repository URL alongside public PDF distribution. This audit does not by itself certify the later publication. Different licences apply to the City, BEV and GHSL layers; see the existing source inventory. This is a documented technical review, not independent legal advice.
