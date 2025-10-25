import time
from datetime import datetime

timestamp = time.time()

print("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation"
	.format(timestamp, timestamp))
now = datetime.now()
print(now.strftime("%b %d %Y"))
