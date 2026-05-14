from lesson_header import *

#I believe I am now mostly finished, just have to do some dictionary stuff.
 
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
  moves.move_left(1.5)
  cups += 1 

moves.forward(3)
print("Finished")
