from pathlib import Path
from finding_gauge import find_gauge

vector_path = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\codes\dwd_precip_temp\dwd_data_analysis\data\aoi.shp")
t_res = 'daily'
dataset = 'climate_summary'
variable = 'precipitation_height'
out_path = Path(r"C:\Users\kazii\OneDrive - TUM\Desktop\master_thesis\codes\dwd_precip_temp\dwd_data_analysis\data")

find_gauge(vector_path, t_res, dataset, variable, out_path)