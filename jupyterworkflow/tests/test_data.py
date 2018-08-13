import jupyterworkflow.data
import pandas
import numpy

def test_fremont_data():
    data = jupyterworkflow.data.get_freemont_data()
    assert all(data.columns == ['Total', 'East', 'West'])
    assert isinstance(data.index, pandas.DatetimeIndex)
    assert len(numpy.unique(data.index.time) == 24)
