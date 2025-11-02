# Find an Euclidian distance between (2, 3) and (10, 8)
#formula = √((x2 - x1)^2 + (y2 - y1)^2)

import math
p = (2, 3)
q = (10, 8)
distance = math.sqrt((q[0] - p[0])**2 + (q[1] - p[1])**2)
print("The Euclidian distance between points p and q is:", distance)
