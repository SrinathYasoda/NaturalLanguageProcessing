TRACK_TERMS=["trump","biden","donaldtrump"]
CONNECTION_STRINGS="sqlite:///tweets.db"
CSV_NAME="G:\\JOBIFY\\tweets1.csv"
TABLE_NAME="election"

try:
	from private import *
except Exception:
    pass