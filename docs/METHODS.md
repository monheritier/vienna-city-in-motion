# Methods and evidence limits

## Population and pedestrian network

The 2025 population raster is a GHSL R2023A **projection**, not a register. Fractional-cell allocation assumes population is uniform within each cell. It yielded approximately 2,009,240 for the districts compared with 2,028,289 officially on 1 January 2025. Innere Stadt (+237%), Hietzing (+74%) and Brigittenau (−38%) show that a similar city total does not validate the district distribution. The centre-cell method is also retained in the district comparison. The reason for the differences is unresolved.

The 54,777 endpoint-only components were a diagnostic, not a count of isolated walking networks. Crossings, access permissions, grade separation and stop entrances remain insufficiently validated. Neither pedestrian catchments nor population-weighted coverage or timetable-based travel times were produced.

## Three corridor sketches

The exploratory paths were reconstructed locally in EPSG:3416 from 40,828 OSM-sourced road records, yielding 40,823 retained segments, 43,734 nodes and a 17,667-node largest strongly connected component. Nodes use 2 m endpoint rounding; intersections and levels are not fully validated. Stops are anchors, not verified entrances. Paths are not proposed engineering designs.

| Corridor | Checked length | Difference from stored length |
|---|---:|---:|
| West Arc | 12,250.245 m | 0.0046 m |
| North Danube | 7,950.261 m | 0.0015 m |
| South Arc | 10,592.420 m | 0.0005 m |

Route lengths are planar, exclude snap links and do not measure feasibility or accessibility. Re-run `scripts/reproduce_routes.py` on the supplied data to check lengths; route choices can vary with software and tie-breaking.

## BEV 3D massing

BEV DLM Bauwerke, edition 25 March 2025, `HOEHE_OBJEKT_MEDIAN`, gives a surface-derived median object height. Five geographic extracts are included: central/Frankhplatz, Michelbeuern, Meidling, West Arc and North Danube. The views use flat-roof footprint extrusion, a flat base and 2× vertical exaggeration, not actual façade or roof geometry. North Danube was restricted to features intersecting the pre-existing `North Danube building footprints Vienna` project layer, not the entire bounding box. Six footprint parts with null or nonpositive values were omitted in the view. Road and transit lines are cartographic overlays, not depths or elevated structures.

The included QGIS project permits inspection of the source extracts and vector maps; it does not contain the final atlas print layouts or the 3D-generation workflow. The final PDF is a produced work, not a fully reproducible analytical pipeline. The complete GHSL raster and original V3–V9 project are not included. Retrieve GHSL R2023A from https://doi.org/10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE.
