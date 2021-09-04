function move_backward (backwardAmount: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < moveAmount[backwardAmount] || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < moveAmount[backwardAmount]) {
    	
    }
}
function display_backward () {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        . # . # .
        . . # . .
        `)
}
function display_smile () {
    basic.showLeds(`
        # . . . #
        . # # # .
        . . . . .
        . . . . .
        . . . . .
        `)
}
function convert_received_string (received: string) {
    for (let k = 0; k <= 1; k++) {
        convertedString[k] = parseInt(received.charAt(k))
    }
}
function left_turn_signal (leftBlink: number) {
    for (let index = 0; index < leftBlink + 1; index++) {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.WHITH)
        basic.pause(250)
    }
}
function right_turn_signal (rightBlink: number) {
    for (let index = 0; index < rightBlink + 1; index++) {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.YELLOW)
        basic.pause(250)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.WHITH)
        basic.pause(250)
    }
}
function display_damage () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
}
function display_forward () {
    basic.showLeds(`
        . . # . .
        . # . # .
        # . # . #
        . . # . .
        . . # . .
        `)
}
function display_left () {
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # . #
        . . . # .
        . . # . .
        `)
}
function turn_left (leftTurnAmount: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CCW, turnSpeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, turnSpeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < turnAmount[leftTurnAmount] || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < turnAmount[leftTurnAmount]) {
    	
    }
}
function display_right () {
    basic.showLeds(`
        . . # . .
        . # . . .
        # . # # #
        . # . . .
        . . # . .
        `)
}
radio.onReceivedString(function (receivedString) {
    convert_received_string(receivedString)
    if (convertedString[0] == BACKWARD) {
        display_backward()
        move_backward(convertedString[1])
    } else if (convertedString[0] == FORWARD) {
        display_forward()
        move_forward(convertedString[1])
    } else if (convertedString[0] == LEFT) {
        display_left()
        left_turn_signal(convertedString[1])
        turn_left(convertedString[1])
    } else if (convertedString[0] == RIGHT) {
        display_right()
        right_turn_signal(convertedString[1])
        turn_right(convertedString[1])
    } else if (convertedString[0] == DAMAGE) {
        display_damage()
    } else {
    	
    }
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.WHITH)
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.WHITH)
    clear_convertedString()
})
function clear_convertedString () {
    for (let i = 0; i <= 1; i++) {
        convertedString[i] = 0
    }
}
radio.onReceivedValue(function (name, value) {
    if (name == "forward") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, Math.map(value, 550, 1023, 10, 255))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        display_forward()
    } else if (name == "backward") {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, Math.map(value, 1, 540, 255, 10))
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.BLUE)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.BLUE)
        display_backward()
    } else if (name == "left") {
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, Math.map(value, 1, 450, 255, 40))
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
        display_left()
    } else if (name == "right") {
        DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, Math.map(value, 550, 1023, 40, 255))
        DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, 20)
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.GREEN)
        display_right()
    }
})
function move_forward (forwardAmount: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CW, basespeed)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, basespeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < moveAmount[forwardAmount] || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < moveAmount[forwardAmount]) {
    	
    }
}
function turn_right (rightTurnAmount: number) {
    DFRobotMaqueenPlus.clearDistance(Motors.ALL)
    DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, turnSpeed)
    DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, turnSpeed)
    while (Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M2))) < turnAmount[rightTurnAmount] || Math.abs(parseFloat(DFRobotMaqueenPlus.readeDistance(Motors1.M1))) < turnAmount[rightTurnAmount]) {
    	
    }
}
let turnAmount: number[] = []
let moveAmount: number[] = []
let turnSpeed = 0
let basespeed = 0
let convertedString: number[] = []
let DAMAGE = 0
let BACKWARD = 0
let FORWARD = 0
let RIGHT = 0
let LEFT = 0
LEFT = 1
RIGHT = 2
FORWARD = 3
BACKWARD = 4
DAMAGE = 5
convertedString = [0, 0, 0]
basespeed = 50
turnSpeed = 50
moveAmount = [
0.01,
0.75,
1.5,
2.25
]
turnAmount = [0.01, 0.35, 0.7]
radio.setGroup(1)
