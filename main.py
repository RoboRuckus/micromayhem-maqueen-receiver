
def on_received_string(receivedString):
    if receivedString == "oneForward":
        display_direction("forward")
        MoveForward(fullmove)
    elif receivedString == "oneBackward":
        display_direction("backward")
        MoveBackward(fullmove)
    elif receivedString == "oneLeft":
        turn_signal("left", 3)
        display_direction("left")
        TurnLeft(quarterTurn)
    elif receivedString == "oneRight":
        turn_signal("right", 3)
        display_direction("right")
        TurnRight(quarterTurn)
    elif receivedString == "littleForward":
        display_direction("forward")
        MoveForward(smallmove)
    elif receivedString == "littleBackward":
        display_direction("backward")
        MoveBackward(smallmove)
    elif receivedString == "littleLeft":
        display_direction("left")
        turn_signal("left", 2)
        TurnLeft(smallmove)
    elif receivedString == "littleRight":
        display_direction("right")
        turn_signal("right", 2)
        TurnRight(smallmove)
    else:
        pass
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)
    basic.show_leds("""
        # . . . #
        . # # # .
        . # # . .
        . # . . .
        . . . . .
    """)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.White)
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.White)
radio.on_received_string(on_received_string)

def on_received_value(name, value):
    if name == "forward":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        display_direction("forward")
    elif name == "backward":
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
        display_direction("backward")
    elif name == "left":
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)
        display_direction("left")
    elif name == "right":
        DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.GREEN)
        display_direction("right")
radio.on_received_value(on_received_value)

def TurnLeft(num: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num:
        pass

def TurnRight(num2: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, turnSpeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, turnSpeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num2 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num2:
        pass

def MoveBackward(num3: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num3 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num3:
        pass

def MoveForward(num4: number):
    DFRobotMaqueenPlus.clear_distance(Motors.ALL)
    DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, basespeed)
    while abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M2))) < num4 or abs(parse_float(DFRobotMaqueenPlus.reade_distance(Motors1.M1))) < num4:
        pass

def turn_signal(direction: string, blink: number):
    lightToBlink = "1"
    if direction == "left":
        lightToBlink = "2"
    
    for i in range(blink):
        DFRobotMaqueenPlus.set_rgb_light(lightToBlink, Color.YELLOW)
        basic.pause(500)
        DFRobotMaqueenPlus.set_rgb_light(lightToBlink, Color.WHITE)
        basic.pause(500)



def display_direction(direction: string):
    if direction == "forward":
        basic.show_leds("""
            . . # . .
            . # . # .
            # . # . #
            . . # . .
            . . # . .
        """)
    elif direction == "backward":
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . #
            . # . # .
            . . # . .
        """)
    elif direction == "left":
        basic.show_leds("""
            . . # . .
            . . . # .
            # # # . #
            . . . # .
            . . # . .
        """)
    else:
        basic.show_leds("""
            . . # . .
            . # . . .
            # . # # #
            . # . . .
            . . # . .
        """)

basespeed = 0
quarterTurn = 0
turnSpeed = 0
fullmove = 0
smallmove = 0
radio.set_group(1)

basespeed = 50
turnSpeed = 50

quarterTurn = 0.35
fullmove = 0.75
smallmove = 0.01

def on_forever():
    pass

basic.forever(on_forever)
