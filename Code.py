from lesson_header import *

#I'm going to try write some basics and improve it from there.

def cups():

 cups = 0
while cups < 4:
 distance = 10
 distance_cm = sonar.get_distance_cm(filtered=True)
 if distance > 10:
  moves.forward
 elif cups == 1:
  moves.right(1.0)
 elif cups == 2:
  moves.left(1.0)
 elif cups == 3:
  moves.right(1.0)
 elif cups == 4:
  moves.left(1.0)
 else:
  cups += 1

moves.forward(1.0)
