from lesson_header import *

#The basics are done, I'm now going to start on improvements.
 
cups = 0

while cups < 4:
 distance_cm = sonar.get_distance_cm(filtered=True)
 print(f"distance {distance_cm} cups {cups}")
 if distance_cm > 20:
  moves.forward(0.3)
 elif cups == 0:
  moves.move_right(1)
  cups += 1
 elif cups == 1:
  moves.move_left(1)
  cups += 1 
 elif cups == 2:
  moves.move_right(1)
  cups += 1
 elif cups == 3:
  moves.move_left(1)
  cups += 1

moves.forward(1)
