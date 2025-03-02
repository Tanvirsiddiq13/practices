import math
AB = float(input())
BC = float(input())
angle = math.degrees(math.atan2(AB,BC))
print(f"{round(angle)}\u00B0")