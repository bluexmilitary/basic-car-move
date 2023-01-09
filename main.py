basic.show_icon(IconNames.HEART)

def on_forever():
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_RUN)
    basic.pause(1000)
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_BACK)
    basic.pause(1000)
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_LEFT)
    basic.pause(1000)
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_RIGHT)
    basic.pause(1000)
    OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_STOP)
    basic.pause(1000)
    basic.show_icon(IconNames.HEART)
    
    def on_forever2():
        OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_RUN)
        basic.pause(1000)
        OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_BACK)
        basic.pause(1000)
        OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_LEFT)
        basic.pause(1000)
        OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_RIGHT)
        basic.pause(1000)
        OSOYOO_Robot.car_ctrl(OSOYOO_Robot.CarState.CAR_STOP)
        basic.pause(1000)
    basic.forever(on_forever2)
    
basic.forever(on_forever)
