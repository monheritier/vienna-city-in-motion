"""Rebuild V9 exploratory road paths. Open in the QGIS Python console editor and run.
Set REPO below to the repository root. QGIS Python needs scipy and networkx.
No file is modified. Results checked against data/concept_corridors.geojson.
"""
from pathlib import Path
import math
import networkx as nx
from scipy.spatial import cKDTree
from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateTransform, QgsCoordinateReferenceSystem, QgsGeometry

# Change REPO to the actual repository root before running.
REPO = Path(__file__).resolve().parent.parent
prj = QgsProject.instance()
roads = QgsVectorLayer(str(REPO / 'data/osm_road_graph_source.gpkg'), 'OSM road input', 'ogr')
stops = QgsVectorLayer(str(REPO / 'data/wien_station_records.gpkg'), 'City stop anchors', 'ogr')
expected = QgsVectorLayer(str(REPO / 'data/concept_corridors.geojson'), 'Concept routes', 'ogr')
if not all(x.isValid() for x in (roads, stops, expected)):
    raise RuntimeError('An input file did not open')
crs = QgsCoordinateReferenceSystem('EPSG:3416')
tr = QgsCoordinateTransform(roads.crs(), crs, prj)
ts = QgsCoordinateTransform(stops.crs(), crs, prj)
G = nx.DiGraph()
segments = 0
for f in roads.getFeatures():
    g = QgsGeometry(f.geometry()); g.transform(tr)
    parts = g.asMultiPolyline() if g.isMultipart() else [g.asPolyline()]
    for xy in parts:
        if len(xy) < 2: continue
        a = (round(xy[0].x()/2)*2, round(xy[0].y()/2)*2)
        b = (round(xy[-1].x()/2)*2, round(xy[-1].y()/2)*2)
        if a == b: continue
        pts = [(q.x(), q.y()) for q in xy]
        dist = sum(math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1]) for i in range(1,len(pts)))
        if not G.has_edge(a,b) or G[a][b]['weight'] > dist:
            G.add_edge(a,b,weight=dist,coords=pts)
        if str(f['oneway']) == 'both' and (not G.has_edge(b,a) or G[b][a]['weight'] > dist):
            G.add_edge(b,a,weight=dist,coords=pts[::-1])
        segments += 1
component = max(nx.strongly_connected_components(G), key=len)
nodes = list(component)
tree = cKDTree(nodes)
points = {}
for f in stops.getFeatures():
    name = str(f['HTXT'])
    if name in points: continue
    g = QgsGeometry(f.geometry()); g.transform(ts); point = g.asPoint()
    d,i = tree.query([point.x(),point.y()]); points[name] = (nodes[int(i)],float(d))
spec = [('West arc',['Hütteldorf','Hernals','Heiligenstadt']),('North Danube',['Heiligenstadt','Floridsdorf','Kagran']),('South arc',['Alterlaa','Meidling','Matzleinsdorfer Platz','Simmering'])]
reference = {str(f['name']):float(f['length_m']) for f in expected.getFeatures()}
print('OSM inputs: graph segments',segments,'nodes',len(G),'largest strongly connected component',len(component))
for name,via in spec:
    length = 0.0
    for a,b in zip(via,via[1:]):
        route = nx.shortest_path(G,points[a][0],points[b][0],weight='weight')
        length += sum(G[u][v]['weight'] for u,v in zip(route,route[1:]))
    delta=abs(length-reference[name]); print(name,round(length,2),'m; max snap',round(max(points[x][1] for x in via),1),'m; delta',round(delta,3),'m')
    if delta > 0.1: raise AssertionError('Route length differs by > 0.1 m; inspect feature order or QGIS/PROJ version')
print('Length check passed. This does not validate road permissions, transit feasibility or accessibility.')
