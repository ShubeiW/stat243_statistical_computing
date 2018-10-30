from pyspark import SparkContext
sc = SparkContext()

## load data

dir = '/global/scratch/paciorek/wikistats_full/dated'
lines = sc.textFile(dir + '/' + 'dated')

import re
from operator import add

## find the data of interest

def find(line, regex = "Financial_crisis", language = None):
    vals = line.split(' ')
    if len(vals) < 6:
        return(False)
    tmp = re.search(regex, vals[3], re.IGNORECASE)
    if tmp is None or (language != None and vals[2] != language):
        return(False)
    else:
        return(True)

fin_crisis = lines.filter(find)


def pair(line):
    # create key-value pairs where:
    #   key = date-language
    #   value = number of website hits
    vals = line.split(' ')
    return(vals[0] + '-' + vals[2], int(vals[4]))

# sum number of hits for each key
counts = fin_crisis.map(pair).reduceByKey(add)

## transform to regular form

def transform(pair):
    key = pair[0].split('-')
    return(','.join((key[0],key[1],str(pair[1]))))

outputDir = '/global/home/users/shubei_wang/stat243/ps6/' + 'financial-crisis-counts'
counts.map(transform).repartition(1).saveAsTextFile(outputDir)


