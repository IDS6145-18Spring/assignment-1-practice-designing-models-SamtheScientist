import random


class AI:
    '''The artificial intelligence component of the RPPS'''


    def __init__(self):
        '''Initializes the AI'''
        self.active_ai = active #Defines which AI is active


    def active_ai(self):
        '''Indicates which AI is active'''
        ai = ["lens model", "facial recognition"]
        self.active_ai = random.sample(ai, 1)
        print(f"The AI currently active is {self.active_ai}.")

    def ir_values(self):
        '''The infrared radiation and temperature values retrieved from the sensor suite component'''
        ir_value = Infrared.ir_value_raw
        print(f"{ir_value}")
        ir_temp = Infrared.ir_temp_raw
        print(f"{ir_temp}")

    def convert_ad(self):
        '''Converts the infrared radiation value to a degree of activation for use in the lens model'''
        ad = (ir_value + 1)/100
        print(f"{ad}")

    def social_signal(self):
        '''Retrieves the output of the lens model for the actual and perceived social signals'''
        SA = LensModel.ActualSS
        SP = LensModel.PerceivedSS
        print(f"{SA}, {SP}")

    def lens_model_match(self):
        '''Retrieves the achievement of understanding output from the lens model. This number represents the match between the two compared models.'''
        BLM_Match = (LensModel.ra + 1)/100
        print(f"{BLM_Match}")

    def facial_match(self):
        '''Retrieves the output of the facial recognition AI'''
        Match = facialrecognition.facialmatch
        print(f"The target human shares a {Match}% match with {facialrecognition.identity}.")
