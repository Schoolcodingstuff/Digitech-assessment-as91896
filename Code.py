from lesson_header import *

# At this point I am planning on making my robot detect each cup independently and move accordingly depending on the cup detected.
while True:
if cup_1 == True:
 moves.left (1)
elif cup_2 == True:
 moves.right (1)
elif cup_3 == True:
 moves.left (1)
elif cup_4 == True:
 moves.right
else
 moves.forward (1)
