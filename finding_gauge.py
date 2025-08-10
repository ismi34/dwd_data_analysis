from wetterdienst import Settings
from wetterdienst.provider.dwd.observation import DwdObservationRequest
from make_bbox import make_bbox
import shapely
import geopandas as gpd
from pathlib import Path

def find_gauge(vector_path, t_res, dataset, variable, out_path):
    """Find gauge stations within a bounding box defined by a vector file."""
    bounds = make_bbox(vector_path)
    
    outfile = Path(out_path) / f"{t_res}_{dataset}_{variable}_stations.shp"
    
    settings = Settings(ts_shape='long',
                        ts_humanize=True,
                        ts_convert_units=True)

    request = DwdObservationRequest(settings=settings,
                                    parameters=[(t_res, dataset, variable)])

    stations = request.filter_by_bbox(*bounds).df
    stations_df = stations.to_pandas()
    stations_df['geometry'] = stations_df.apply(lambda row: shapely.geometry.Point(row['longitude'], row['latitude']), axis=1)
    stations_gdf = gpd.GeoDataFrame(stations_df, geometry='geometry', crs='EPSG:4326')
    

    stations_gdf.to_file(outfile, driver='ESRI Shapefile')
    return outfile