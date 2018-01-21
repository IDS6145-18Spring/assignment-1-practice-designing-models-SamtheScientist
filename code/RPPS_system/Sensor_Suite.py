import random


class SensorSuite:
    '''This is a multi-purpose sensor suite that controls which sensor is considered the primary and secondary'''


    def __init__(self, infrared, ladar):
        '''Initializes the sensor suite'''
        self.infrared = True #identifies whether this sensor is active
        self.ladar = True #identifies whether this sensor is active


    def info(self):
        '''Sensor use status'''
        if self.infrared == True:
            active_sensor = "infrared"
            tasking = "collecting social cue data"
            if self.ladar == True:
                active_sensor = "ladar"
                tasking = "mapping the surrounding environment"
        else:
            active_sensor = "none"
        print(f"{active_sensor} is currently active and sensor is {tasking}.")

    def weather(self):
        '''Gets current weather'''
        weather = ["clear", "sunny", "cloudy", "foggy", "rain", "windy", "hot", "cold", "snow"]
        weather_status = random.sample(weather, 1)
        if weather_status == ["clear", "sunny", "windy", "hot", "cold"]:
            viz_state = "good"
        else:
            viz_state = "bad"
        print(f"Visualization will be {viz_state} due to {weather_status}.")

    def movement_mode(self):
        '''Gets status of movement mode from "robot platform" component'''
        if RobotPlatform.movement_mode == "aerial":
            movement_mode = "aerial"
        else:
            movement_mode = "ground"

    def target_detected(self):
        '''Determines whether a target has been detected and if the robot is in the correct mode'''
        if target_detected == True:
            active_sensor = "infrared"
            RobotPlatform.movement_mode = "ground"
        else:
            active_sensor = "other"
        print(f"The possibility of successfully navigating the environment to catch target human are approximately 3,720 to 1.")