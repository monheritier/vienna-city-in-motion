# Transit corridor sensitivity screen

Supplement to the 19-page atlas, prepared 24 November 2026. The original three routes remain exploratory road-path sketches, not official transit plans or engineered alignments. The attached appendix is a preliminary scenario screen, not a Stadt Wien investment appraisal.

## Results

The combined 30.79 km concepts have an estimated gross corridor catchment of about 170,943 district-allocated residents. At the central assumption, this yields approximately 7.36 million annual boardings. The 400 m straight-line buffer union adds about 942 residents beyond the loaded multimodal transit-stop catchments. Individual corridor net-new residents are estimated at about 17 West Arc, 675 North Danube and 250 South Arc.

Central annual net benefit, counting passenger time savings only, is −€36.84m West Arc tram / −€13.19m bus priority; −€24.07m / −€8.71m North Danube; and −€30.61m / −€10.15m South Arc. Combined unique results are −€91.65m tram and −€32.18m bus priority. In the optimistic paired scenario, bus priority is +€2.33m, +€0.95m and +€6.52m respectively; tram remains negative.

At central annualized cost, break-even rides at 7.5 minutes saved per boarding and €10/hour are: West Arc 32.1m tram / 13.2m bus; North Danube 20.8m / 8.5m; South Arc 27.8m / 11.4m. At central forecast demand and €10/hour, required savings are 92 / 38 minutes, 99 / 41 minutes, and 64 / 26 minutes per boarding.

## Method and assumptions

- Stop access: candidate surface stops spaced no farther apart than 395.9 m, Wiener Linien’s reported 2024 mean tram stop spacing, with a 400 m straight-line circular access radius. The baseline unions geometry for the project’s transit-stop inventory (7,928 records), covering bus, tram, metro, rail and other records. Stop records may be platforms or service points, not verified pedestrian entrances; no network walking path, crossings, barriers or elevation is tested.
- Population: official 2025 district totals distributed uniformly by district area to estimate gross residents inside corridor stop catchments. This is a coarse allocation, not address-, census-cell- or workplace-level demand. The separate net-new-access estimate subtracts existing stop buffers.
- Annual boardings: gross catchment residents × 430.3 reported 2024 Wiener Linien passenger boardings per inhabitant × 5%, 10% or 15% assumed capture for low, central and high scenarios. This citywide boarding rate is a proxy, not unique trips, route-specific passengers, fare validations, or demand forecast.
- Tram capital unit costs: €25m / €40m / €60m per route-km; annual operations and maintenance: €0.8m / €1.1m / €1.5m per route-km-year. Bus-priority capital: €5m / €10m / €15m per route-km; O&M €0.5m / €0.8m / €1.0m per route-km-year. These are analyst-set screening assumptions, not sourced project quotations.
- Capital annualized over 30 years at 3.5%; no residual value, construction staging, financing or risk allowance. Passenger time-value cases are 3 minutes at €8/hour, 7.5 minutes at €10/hour and 12 minutes at €15/hour. Net benefit equals valued passenger time savings minus annualized capital and annual O&M.

## Limits

No timetable-based service plan, frequency, reliability, route capacity, fare receipts, jobs and visitor origins, transfer/displacement effects, car journey-time or vehicle-cost savings, congestion, emissions, safety, accessibility quality, land-use response, construction impacts, equity analysis or full lifecycle economic appraisal was modeled. Catchment and population estimates are approximate; scenario results are highly sensitive to capture, actual time savings and alignment/civil works. The optimism case combines favorable demand, time savings and costs and is not a probability interval.

## Data package and sources

`data/transit_corridor_analysis.gpkg` contains three exported layers: `corridor_break_even_sensitivity` (4 rows), `corridor_cost_ridership` (4 rows), and `net_new_tram_access_400m` (one EPSG:3416 MultiPolygon). The 4-row “Combined” entry is a summary, not an extra corridor.

Inputs: the project’s conceptual corridor paths and their local OSM/Overture routing provenance; City of Vienna transit-stop records and district boundaries/population totals; Wiener Linien, Facts & Figures / Operating Data 2024 for 430.3 annual boardings per inhabitant and 395.9 m average tram stop spacing. Unit costs, capture shares, 400 m radius, time savings and time values are assumptions. See `DATA_LICENCES.md`; this note does not constitute independent rights clearance.
