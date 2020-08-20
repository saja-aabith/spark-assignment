# Daemon Solutions Python Assignment

1. This repo uses the data from IMDb and fetches the top 15 movies
2. The ranking is based the formula: (numVotes / averageNumberOfVotes) * averageRating)


## Setup

1. Create a folder and create a python virtual environment using `python3 -m venv /path/to/new/virtual/environment`
2. Then run `source bin/activate`
3. Then run `pip install`
4. Then run `pyspark` which will open Jupyter
5. Download the two .tsv files containing information on the [titles](https://datasets.imdbws.com/name.basics.tsv.gz) and [ratings](https://datasets.imdbws.com/title.ratings.tsv.gz) into the `raw_data` folder. 



Information courtesy of
IMDb
(http://www.imdb.com).
Used with permission.