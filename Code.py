#These are just from the student library.

def forward(seconds: float = 0.5, speed: float = None):
    setup()
    s = float(BASE_SPEED if speed is None else speed)
    base._spam(+s, +s, +s, +s, seconds)

def move_left(seconds: float = 0.5, speed: float = None):
    setup()
    s = float(BASE_SPEED if speed is None else speed)
    base._spam(-s, +s, +s, -s, seconds)

#I edited the move_right command.

def move_right(seconds: float = 0.5, speed: float = None):
    setup()
    s = float(BASE_SPEED if speed is None else speed)
    base._spam(+s, -s, -s, +s, seconds)

#I'm going to try write some basics and improve it from there.

cup = 0

while cups < 4:
 distance_cm = sonar.get_distance_cm(filtered=True)
 if distance > 10:
  forward(1, 1)
 elif cups == 1:
  move_right(1, 1)
 elif cups == 2:
   move_left(1, 1)
 elif cups == 3:
   move_right(1, 1)
 elif cups == 4:
   move_left(1, 1)
 else:
  cups += 1

forward(1, 1)

