from lesson_header import *

#I'm going to try write some basics and improve it from there.
 
cups = 0

while cups < 4:
 distance_cm = sonar.get_distance_cm(filtered=True)
 print(f"distance {distance_cm} cups {cups}")
 if distance_cm > 15:
  moves.forward(0.3)
 elif cups == 0:
  cups += 1
  moves.move_right(1)
 elif cups == 1:
  cups += 1
  moves.move_left(1)
 elif cups == 2:
  cups += 1
  moves.move_right(1)
 elif cups == 3:
  cups += 1
  moves.move_left(1)
  
moves.forward(1)
