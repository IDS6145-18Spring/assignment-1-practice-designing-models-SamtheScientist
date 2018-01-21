import random


class RobotPlatform:
    '''This is a robot platform'''


    def __init__(self, movement_mode, die):
        '''Initializes the platform'''
        self.movement_mode = movement_mode #defines the movement mode
        self.die = False #everybody dies, even robots


    def movement_mode(self):
        '''Gets status of movement mode from "robot platform" component'''
        self.movement_mode = ["aerial", "ground"]
        movement_mode = random.sample(movement, 1)
        print(f"{movement_mode} currently engaged.")

    def environment(self):
        '''Defines the environment'''
        environment = ["forest", "grassland", "desert", "urban", "tundra", "mountain", "hilly", "polar ice"]
        environment_type = random.sample(environment, 1)
        print(f"The surrounding environment is classified as {environment_type}.")

    def switch_movement(self):
        '''Responsible for switching movement mode for a variety of reasons'''
        if environment_type == ["forest", "desert", "tundra", "mountain", "hilly", "polar ice"]:
            enviro_movement = "aerial movement"
        else:
            enviro_movement = "ground movement"
        print(f"{environment_type} entered, robot platform switched to {enviro_movement} for optimal performance.")

    def fire(self):
        '''Halt and catch fire'''
        self.die = ["alive", "death by environment", "death by human", "death by animal", "death by self", "death by sand"]
        die_chance = random.randint(1, 100)
        if die_chance < 20 and environment_type == "desert" and movement_mode == "ground":
                The_Game = "Over"
                print(f"I don't like sand. It's coarse and rough and irritating and it gets everywhere.")