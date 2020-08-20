# 1. Filter
def filter_100_votes(rdd):
    return rdd.filter(lambda x: int(x[2])>=100)

# 2. Tuple conversion
def tuple_conversion(rdd):
    return rdd.map(lambda r: (r[0], r))

# 3. Filtering movies
def filter_movies(rdd):
    return rdd.filter(lambda x: x[1][1][1]=='movie')

# 4. Calculating the mean 
def find_mean(rdd):
    return rdd.map(lambda x: int(x[1][0][2])).mean()   
      
# 5. Calculating the ranking 
def rank(rdd):
    mean = find_mean(rdd)
    return rdd.sortBy(lambda x: (int(x[1][0][2])/mean)*float(x[1][0][1]), False)
