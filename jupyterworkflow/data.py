import os
import pandas
import urllib

FREEMONT_URL = 'https://data.seattle.gov/api/views/47yq-6ugv/rows.csv?accessType=DOWNLOAD'

def get_freemont_data(filename = 'Freemont.csv', url = FREEMONT_URL, force_download = False):
    if force_download or not os.path.exists(filename):
        urllib.request.urlretrieve(url, filename)
        
    data = pandas.read_csv('Freemont.csv', index_col = 'Date', parse_dates = True)
    data.columns = ['Total', 'East', 'West']
    
    return(data)
