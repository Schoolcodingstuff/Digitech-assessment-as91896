from lesson_header import *

cups = 0

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
  print("No cups detected.")
  print("Moving forward.")
  moves.forward(0.5)
  print("Moved forward.")
 elif dict_decision[cups] == "right":
  cups += 1
  print("Cup detected.")
  print("Moving right.")
  moves.move_right(1.5)
  print("Moved right.")
 elif  dict_decision[cups] == "left":
  cups += 1 
  print("Cup detected.")
  print("Moving left.")
  moves.move_left(1.5)
  print("Moved left.")

print("Moving forward.")
moves.forward(3)
print("Moved forward.")
print("Course completed.")
