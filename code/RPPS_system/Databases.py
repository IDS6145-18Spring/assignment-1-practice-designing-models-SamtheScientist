class databases:
    '''These are the databases used to store records'''


    def __init__(self, active_database):
        '''Initializes the databases'''
        self.active_database = database #identifies which database is active


    def active_database(self):
        '''Determines the active database according to which AI is active'''
        self.active_database = AI.active_ai
        print(f"{self.active_database} is the database that is currently active.")

    def activate_database(self):
        databases = ["human activities & behaviors", "mental states", "facial recognition"]
        if AI.active_ai == "human activities & behaviors":
            activate_database = "human activities & behaviors"
            if AI.active_ai == "mental states":
                activate_database = "mental states"
                if AI.active_ai == "facial recognition":
                    activate_database = "facial recognition"
        else:
            activate_database = "none"
        print(f"The database currently active is {activate_database}.")

    def store_record(self):
        '''Store novel data records in the databases for future reference'''
        if AI.match_lens_model < 30:
            store_record = False
        else:
            store_record = True
        if AI.facial_match == AI.active_ai:
            store_record = True
        else:
            store_record = False
