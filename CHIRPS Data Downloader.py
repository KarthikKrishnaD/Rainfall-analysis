import climateserv.api
import os
import numpy as np

geometry = [[103.046, 11.679], [103.046, 13.539], [105.617, 13.539], [105.617, 11.679]]
dataset = 'CHIRP'
operation_type = 'NetCDF' # NetCDF for Daily rasters, (Average, max, min for respective zonal statistics inside the box)
start_date = "09/01/2015" # MM/DD/YYYY
end_date = "10/15/2015"
ensemble = ''
variable = ''
outfile = 'imerg_precip_2.zip' # Zip file generated at the woring directory

climateserv.api.request_data(dataset, operation_type, 
             start_date, end_date,geometry, 
             ensemble, variable,outfile)