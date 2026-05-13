from lesson_header import *

#I'm going to try write some basics and improve it from there.
 
cups = 0

while cups < 4:
 distance_cm = sonar.get_distance_cm(filtered=True)
 print(f"distance {distance_cm} cups {cups}")
 if distance_cm > 10:
  moves.forward(0.3)
 elif cups == 1:
  moves.move_right(1)
 elif cups == 2:
   moves.move_left(1)
 elif cups == 3:
   moves.move_right(1)
 elif cups == 4:
   moves.move_left(1)
 else:
  cups += 1

moves.forward(1)
