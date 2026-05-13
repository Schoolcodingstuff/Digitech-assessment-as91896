from lesson_header import *

#The basics are done, I'm now going to start on improvements.
 
cups = 0
#Implemented the dictionary.
dict_decision = {
    0: "right",
    1: "left",
    2: "right",
    3: "left"
}

while cups < 4:
 distance_cm = sonar.get_distance_cm(filtered=True)
 print(f"distance {distance_cm} cups {cups}")
 if distance_cm > 20:
  moves.forward(0.5)
 elif dict_decision[cups] == "right":
  moves.move_right(1.5)
  cups += 1
 elif  dict_decision[cups] == "left":
  moves.move_left(2)
  cups += 1 

moves.forward(2)
print("Finished")
