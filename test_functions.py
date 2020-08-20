import pytest
from functions import filter_100_votes, tuple_conversion, filter_movies, find_mean, rank
from pyspark import SparkContext
sc = SparkContext(master = 'local[2]')

def test_filter_100_votes():
    rdd = sc.parallelize([['tt9916778', '7.3', '24'], ['tt9916766', '6.9', '14'], ['tt9916720', '6.0', '57']])
    assert filter_100_votes(rdd) == sc.parallelize([[]])