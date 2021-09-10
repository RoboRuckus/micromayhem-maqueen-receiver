def move_backward(backwardAmount: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < moveAmount[backwardAmount] or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < moveAmount[backwardAmount]:
        pass
def display_backward():
    basic.show_leds("""
        . . # . .
                . . # . .
                # . # . #
                . # . # .
                . . # . .
    """)
def display_smile():
    basic.show_leds("""
        # . . . #
                . # # # .
                . . . . .
                . . . . .
                . . . . .
    """)
def convert_received_string(received: str):
    for k in range(2):
        convertedString[k] = int(received.char_at(k))
def left_turn_signal(leftBlink: number):
    for index in range(leftBlink + 1):
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.WHITH)
        basic.pause(250)
def right_turn_signal(rightBlink: number):
    for index2 in range(rightBlink + 1):
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.WHITH)
        basic.pause(250)
def setBTGroup():
    global done, btgroupnum
    basic.show_string("SET CHANNEL")
    soundExpression.giggle.play_until_done()
    done = 0
    btgroupnum = 0
    while done == 0:
        if input.button_is_pressed(Button.B):
            music.play_tone(131, music.beat(BeatFraction.SIXTEENTH))
            btgroupnum += 1
        if input.button_is_pressed(Button.A):
            soundExpression.spring.play_until_done()
            done = 1
        basic.show_number(btgroupnum)
    radio.set_group(btgroupnum)
    basic.show_icon(IconNames.YES)
def display_damage():
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)
def display_forward():
    basic.show_leds("""
        . . # . .
                . # . # .
                # . # . #
                . . # . .
                . . # . .
    """)
def display_left():
    basic.show_leds("""
        . . # . .
                . . . # .
                # # # . #
                . . . # .
                . . # . .
    """)
def turn_left(leftTurnAmount: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < turnAmount[leftTurnAmount] or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < turnAmount[leftTurnAmount]:
        pass
def display_right():
    basic.show_leds("""
        . . # . .
                . # . . .
                # . # # #
                . # . . .
                . . # . .
    """)

def on_received_string(receivedString):
    convert_received_string(receivedString)
    if convertedString[0] == BACKWARD:
        display_backward()
        move_backward(convertedString[1])
    elif convertedString[0] == FORWARD:
        display_forward()
        move_forward(convertedString[1])
    elif convertedString[0] == LEFT:
        display_left()
        left_turn_signal(convertedString[1])
        turn_left(convertedString[1])
    elif convertedString[0] == RIGHT:
        display_right()
        right_turn_signal(convertedString[1])
        turn_right(convertedString[1])
    elif convertedString[0] == DAMAGE:
        display_damage()
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.WHITH)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.WHITH)
    clear_convertedString()
    display_damage()
radio.on_received_string(on_received_string)

def clear_convertedString():
    for i in range(2):
        convertedString[i] = 0

def on_received_value(name, value):
    if name == "forward":
        display_forward()
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
    elif name == "backward":
        display_backward()
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
    elif name == "left":
        display_left()
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
    elif name == "right":
        display_right()
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
    display_damage()
radio.on_received_value(on_received_value)

def move_forward(forwardAmount: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < moveAmount[forwardAmount] or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < moveAmount[forwardAmount]:
        pass
def turn_right(rightTurnAmount: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < turnAmount[rightTurnAmount] or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < turnAmount[rightTurnAmount]:
        pass
btgroupnum = 0
done = 0
turnAmount: List[number] = []
moveAmount: List[number] = []
turnSpeed = 0
basespeed = 0
convertedString: List[number] = []
DAMAGE = 0
BACKWARD = 0
FORWARD = 0
RIGHT = 0
LEFT = 0
LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
DAMAGE = 5
convertedString = [0, 0, 0]
basespeed = 50
turnSpeed = 50
moveAmount = [0.01, 0.751, 1.7, 2.73] # [A slight adjustment, 6" movement, 12" movement, 18" movement]
turnAmount = [0.01, 0.36, 0.8] # [A slight adjustment, 90 degree turn, U-turn]
setBTGroup()