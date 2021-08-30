//  The following extensions are required:
//  * MaqueenPlus
//  This program is not block-code compatible.
//  ---------------
//  Hardware Values
//  ---------------
let RADIO_GROUP = 90
let RADIO_DEADZONE = 20
let RADIO_MAX = 1024
let LEFT_MOTOR = Motors.M1
let RIGHT_MOTOR = Motors.M2
let FORWARD = Dir.CW
let REVERSE = Dir.CCW
let MAX_SPEED = 80
let TURN_SPEED_RATIO = 1 / 2
//  -----------
//  Code Begins
//  -----------
let straight_channel = 0
let turn_channel = 0
let left_motor_speed = 0
let right_motor_speed = 0
function constrain(val: number, min_val: number, max_val: number): number {
    return Math.min(max_val, Math.max(min_val, val))
}

function translate(value: number, left_min: number, left_max: number, right_min: number, right_max: number): number {
    let left_span = left_max - left_min
    let right_span = right_max - right_min
    //  Convert the left range into a 0-1 range float
    let value_scaled = (value - left_min) / left_span
    //  Convert the 0-1 range into a value in the right range
    return right_min + value_scaled * right_span
}

function radio_to_speed(radio_value: number): number {
    let speed = translate(radio_value, -RADIO_MAX, RADIO_MAX, -MAX_SPEED, MAX_SPEED)
    speed = constrain(speed, -MAX_SPEED, MAX_SPEED)
    return speed
}

//  Lazy implementation of mixing
function calculate_speeds_from_radio() {
    
    
    //  Reset to 0
    left_motor_speed = 0
    right_motor_speed = 0
    //  Forward/Backward
    if (Math.abs(straight_channel) > RADIO_DEADZONE) {
        left_motor_speed = radio_to_speed(straight_channel)
        right_motor_speed = radio_to_speed(straight_channel)
    }
    
    //  Left/Right
    if (Math.abs(turn_channel) > RADIO_DEADZONE) {
        left_motor_speed += radio_to_speed(turn_channel * TURN_SPEED_RATIO)
        right_motor_speed -= radio_to_speed(turn_channel * TURN_SPEED_RATIO)
    }
    
    //  Constrain motors to max speed when mixing
    left_motor_speed = constrain(left_motor_speed, -MAX_SPEED, MAX_SPEED)
    right_motor_speed = constrain(right_motor_speed, -MAX_SPEED, MAX_SPEED)
}

function set_motor_speeds() {
    if (left_motor_speed > 0) {
        DFRobotMaqueenPlus.mototRun(LEFT_MOTOR, FORWARD, left_motor_speed)
    } else if (left_motor_speed < 0) {
        DFRobotMaqueenPlus.mototRun(LEFT_MOTOR, REVERSE, Math.abs(left_motor_speed))
    } else {
        DFRobotMaqueenPlus.mototStop(LEFT_MOTOR)
    }
    
    if (right_motor_speed > 0) {
        DFRobotMaqueenPlus.mototRun(RIGHT_MOTOR, FORWARD, right_motor_speed)
    } else if (right_motor_speed < 0) {
        DFRobotMaqueenPlus.mototRun(RIGHT_MOTOR, REVERSE, Math.abs(right_motor_speed))
    } else {
        DFRobotMaqueenPlus.mototStop(RIGHT_MOTOR)
    }
    
}

function direction_arrow() {
    //  Mirror channels so that it points in the direction it's moving
    let straight = -straight_channel
    let turn = -turn_channel
    if (straight > RADIO_DEADZONE) {
        if (turn > RADIO_DEADZONE) {
            basic.showLeds(`
                            . # # # #
                            . . . # #
                            . . # . #
                            . # . . #
                            # . . . .
                            `)
        } else if (turn < -RADIO_DEADZONE) {
            basic.showLeds(`
                            # # # # .
                            # # . . .
                            # . # . .
                            # . . # .
                            . . . . #
                            `)
        } else {
            basic.showLeds(`
                            . . # . .
                            . # # # .
                            # . # . #
                            . . # . .
                            . . # . .
                            `)
        }
        
    } else if (straight < -RADIO_DEADZONE) {
        if (turn > RADIO_DEADZONE) {
            basic.showLeds(`
                            # . . . .
                            . # . . #
                            . . # . #
                            . . . # #
                            . # # # #
                            `)
        } else if (turn < -RADIO_DEADZONE) {
            basic.showLeds(`
                            . . . . #
                            # . . # .
                            # . # . .
                            # # . . .
                            # # # # .
                            `)
        } else {
            basic.showLeds(`
                            . . # . .
                            . . # . .
                            # . # . #
                            . # # # .
                            . . # . .
                            `)
        }
        
    } else if (turn > RADIO_DEADZONE) {
        basic.showLeds(`
                            . . # . .
                            . . . # .
                            # # # # #
                            . . . # .
                            . . # . .
                            `)
    } else if (turn < -RADIO_DEADZONE) {
        basic.showLeds(`
                            . . # . .
                            . # . . .
                            # # # # #
                            . # . . .
                            . . # . .
                            `)
    } else {
        basic.showLeds(`
                            . # # # .
                            # . . . #
                            # . . . #
                            # . . . #
                            . # # # .
                            `)
    }
    
}

function setup() {
    basic.showIcon(IconNames.Heart)
    radio.onReceivedValue(function on_received_value(name: string, value: number) {
        
        
        if (name == "straight") {
            straight_channel = value
        } else if (name == "turn") {
            turn_channel = value
        }
        
    })
    radio.setGroup(RADIO_GROUP)
    DFRobotMaqueenPlus.I2CInit()
}

//  basic.pause(25) # Keep the refresh rate sane
setup()
basic.forever(function loop() {
    calculate_speeds_from_radio()
    set_motor_speeds()
    direction_arrow()
})
