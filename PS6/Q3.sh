#!/bin/bash
# Job name:
#SBATCH --job-name=Q3
#
# Account:
#SBATCH --account=ic_stat243
#
# Partition:
#SBATCH --partition=savio2
#
# Number of tasks needed for use case (example):
#SBATCH --nodes=4
#
# Wall clock limit:
#SBATCH --time=02:00:00
#
## Command(s) to run:

module load java spark/2.1.0 python/3.5
source /global/home/groups/allhands/bin/spark_helper.sh
spark-start
spark-submit --master $SPARK_URL $HOME/stat243/ps6/count.py
spark-stop
