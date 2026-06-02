from time import gmtime, strftime
import datetime as dt
import time as t

#print(dt.datetime.time(0))

TEST = "Seconds since January 1, 1970: "
TESTT = strftime("%s", gmtime())

TIME = t.time()
SECONDS_COMA = f"{TIME:,}"
SECONDS_SCIN = "{:e}".format(TIME)

print(
	f"Seconds since January 1, 1970: {SECONDS_COMA} or {SECONDS_SCIN} in scientific notation"
)
print(strftime("%a %d %Y", gmtime()))
