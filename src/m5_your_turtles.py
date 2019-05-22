"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joe O'Connell.
"""
########################################################################
# done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window =rg.TurtleWindow()
greg=rg.SimpleTurtle('turtle')
stacy=rg.SimpleTurtle('turtle')

for k in range(40):
    greg.pen = rg.Pen('red', 5)
    greg.speed=50
    greg.draw_square(k+150)
    greg.pen_up()
    greg.right(60)
    greg.forward(3)
    greg.left(60)
    greg.pen_down()
    stacy.pen=rg.Pen('pink',3)
    stacy.speed=70
    stacy.draw_circle(50)
    stacy.pen_up()
    stacy.right(180)
    stacy.forward(3)
    stacy.right(180)
    stacy.pen_down()
window.close_on_mouse_click()