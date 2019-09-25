import re
from datetime import datetime

start='2015-05-17 10:05:03'

start_time=datetime.strptime(start, '%Y-%m-%d %H:%M:%S')

end='2015-05-17 10:05:10'

end_time=datetime.strptime(end, '%Y-%m-%d %H:%M:%S')

for line in open("apache.log"):
    current = datetime.strptime(
        re.search(r"\[([^]]+)]", line).group(1)[:-6],
        "%d/%b/%Y:%H:%M:%S")
    if current >= start_time and current <= end_time:
        print line
    
