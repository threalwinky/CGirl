import datetime
from datetime import *

time_1 = datetime.now()
time_2 = datetime.strptime('2024:7:8:7:00:00',"%Y:%m:%d:%H:%M:%S")

time_interval = time_2 - time_1
time_interval_list = (str(time_interval)).split()

print(time_interval_list[0], time_interval_list[2][:-7])