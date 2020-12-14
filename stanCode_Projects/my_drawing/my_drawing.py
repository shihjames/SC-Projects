"""
File: my_drawing.py
Name: James Shih
----------------------------------------
In this program, Karel the robot represents the students of stanCode,
and the beepers are what we have learned, what we are learning, and
what we will learn. When users click the mouse, Karel will move, this
means we are one step forward in becoming a professional software
engineer, data scientist, etc. Finally, Karel will walk through
the path, meaning that we have graduated from all the courses, and
we will feel very grateful and lucky to have the opportunity to receive
such a good programming education.
"""

from campy.graphics.gobjects import GRect, GLine, GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(500, 500, title='')
head = GOval(60, 40)
eye_l = GRect(10, 10)
eye_r = GRect(10, 10)
body = GRect(60, 50)
neck = GRect(30, 4)
arm_l = GRect(10, 30)
arm_r = GRect(10, 30)
leg_l = GOval(20, 15)
leg_r = GOval(20, 15)
word = GLabel('K')
count = 0


def main():
    """
    The program will first create a canvas, a background, and lines.
    The first click will show four beepers at the lower part of the
    window. The second click will show a robot at the upper part of
    the window. For the next few clicks will move the robot from the
    upper part to the lower part of the window. The final click will
    show a speech bubble.
    """
    background()
    draw_line()
    build_s()
    build_c()
    onmouseclicked(create_beeper)


def background():
    # Create a red background.
    global window
    back = GRect(window.width, window.height)
    back.filled = True
    back.fill_color = 'tomato'
    window.add(back)


def draw_line():
    # Draw several vertical and horizontal lines.
    for i in range(1, 10):
        line_hor = GLine(0, i*50, window.width, i*50)
        line_ver = GLine(i*50, 0, i*50, window.height)
        window.add(line_hor)
        window.add(line_ver)


def build_s():
    # Create word: S.
    global window
    rect_l = 100
    rect_s = 20
    rect1 = GRect(rect_l, rect_s, x=100, y=150)
    rect2 = GRect(rect_s, rect_l, x=100, y=150)
    rect3 = GRect(rect_l, rect_s, x=100, y=230)
    rect4 = GRect(rect_s, rect_l, x=180, y=230)
    rect5 = GRect(rect_l, rect_s, x=100, y=310)
    rect1.filled = True
    rect1.fill_color = 'white'
    rect1.color = 'white'
    rect2.filled = True
    rect2.fill_color = 'white'
    rect2.color = 'white'
    rect3.filled = True
    rect3.fill_color = 'white'
    rect3.color = 'white'
    rect4.filled = True
    rect4.fill_color = 'white'
    rect4.color = 'white'
    rect5.filled = True
    rect5.fill_color = 'white'
    rect5.color = 'white'
    window.add(rect1)
    window.add(rect2)
    window.add(rect3)
    window.add(rect4)
    window.add(rect5)


def build_c():
    # Create word: C.
    global window
    rect_l = 100
    rect_s = 20
    rect1 = GRect(rect_l, rect_s, x=300, y=150)
    rect2 = GRect(rect_s, rect_l*2-rect_s, x=300, y=150)
    rect3 = GRect(rect_l, rect_s, x=300, y=310)
    rect1.filled = True
    rect1.fill_color = 'white'
    rect1.color = 'white'
    rect2.filled = True
    rect2.fill_color = 'white'
    rect2.color = 'white'
    rect3.filled = True
    rect3.fill_color = 'white'
    rect3.color = 'white'
    window.add(rect1)
    window.add(rect2)
    window.add(rect3)


def build_karel(e):
    # Build up the robot, Karel.
    karel_head()
    karel_eye()
    karel_neck()
    karel_body()
    karel_limb()
    karel_label()
    onmouseclicked(move)


def create_beeper(e):
    # create 4 beepers
    size = 50
    for i in (1, 3, 7, 9):
        beeper = GOval(size, size, x=i*50-size/2, y=400-size/2)
        beeper.filled = True
        beeper.fill_color = 'blue'
        window.add(beeper)
    label1 = GLabel('001', x=50-size/2+9, y=400-size/2+37)
    label2 = GLabel('101', x=150-size/2+9, y=400-size/2+37)
    label3 = GLabel('201', x=350-size/2+9, y=400-size/2+37)
    label4 = GLabel('202', x=450-size/2+9, y=400-size/2+37)
    label1.font = '-15'
    label2.font = '-15'
    label3.font = '-15'
    label4.font = '-15'
    label1.color = 'white'
    label2.color = 'white'
    label3.color = 'white'
    label4.color = 'white'
    window.add(label1)
    window.add(label2)
    window.add(label3)
    window.add(label4)
    onmouseclicked(build_karel)


def karel_head():
    # Build Karel's head.
    global head
    head = GOval(60, 40, x=220, y=20)
    head.filled = True
    head.fill_color = 'gray'
    window.add(head)
    return head


def karel_eye():
    # Build Karel's eyes.
    global eye_l, eye_r
    eye_l = GRect(10, 10, x=235, y=35)
    eye_r = GRect(10, 10, x=255, y=35)
    eye_l.filled = True
    eye_r.filled = True
    eye_l.fill_color = 'blue'
    eye_r.fill_color = 'blue'
    window.add(eye_l)
    window.add(eye_r)


def karel_neck():
    # Build Karel's neck.
    global neck
    neck = GRect(30, 4, x=235, y=58)
    neck.filled = True
    neck.color = 'blue'
    window.add(neck)


def karel_body():
    # Build Karel's body.
    global body
    body = GRect(60, 50, x=220, y=62)
    body.filled = True
    body.fill_color = 'blue'
    window.add(body)


def karel_limb():
    # Build Karel's limbs.
    global arm_l, arm_r, leg_l, leg_r
    arm_l = GRect(10, 30, x=210, y=67)
    arm_r = GRect(10, 30, x=280, y=67)
    leg_l = GOval(20, 15, x=220, y=112)
    leg_r = GOval(20, 15, x=260, y=112)
    arm_l.filled = True
    arm_r.filled = True
    leg_l.filled = True
    leg_r.filled = True
    arm_l.fill_color = 'green'
    arm_r.fill_color = 'green'
    leg_l.fill_color = 'red'
    leg_r.fill_color = 'red'
    window.add(arm_l)
    window.add(arm_r)
    window.add(leg_l)
    window.add(leg_r)


def karel_label():
    # Show the word on Karel's body.
    global word
    word = GLabel('K', x=235, y=115)
    word.font = '-35'
    window.add(word)


def move(e):
    # Move Karel down 100 units.
    global count
    if count < 6:
        head.move(0, 50)
        eye_l.move(0, 50)
        eye_r.move(0, 50)
        body.move(0, 50)
        neck.move(0, 50)
        arm_l.move(0, 50)
        arm_r.move(0, 50)
        leg_l.move(0, 50)
        leg_r.move(0, 50)
        word.move(0, 50)
        count += 1
        if count == 6:
            speech_bub()


def speech_bub():
    # Show what Karel says.
    bub1 = GOval(10, 10, x=300, y=340)
    bub2 = GOval(15, 15, x=320, y=330)
    bub3 = GOval(150, 40, x=345, y=303)
    bub1.filled = True
    bub2.filled = True
    bub3.filled = True
    bub1.fill_color = 'white'
    bub2.fill_color = 'white'
    bub3.fill_color = 'white'
    word1 = GLabel('I love stanCode!', x=365, y=325)
    word2 = GLabel('I love Jerry !', x=375, y=338)
    word1.font = 'Courier-8-bold'
    word2.font = 'Courier-8-bold'
    window.add(bub1)
    window.add(bub2)
    window.add(bub3)
    window.add(word1)
    window.add(word2)


if __name__ == '__main__':
    main()
