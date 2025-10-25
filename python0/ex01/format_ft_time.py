import time
from datetime import datetime

timestamp = time.time()

print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation"
	.format(timestamp, timestamp))
now = datetime.now()
print(now.strftime("%b %d %Y")) # string format time. it's a method of datetime objects that let u format a date or time as a string in any layout you want
