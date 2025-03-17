import json
import time
import datetime
class brain:
    def __init__(self):
        pass

    def set_storage_location(self, json_name):
        self.storage = json_name

    def check_storage_location(self):
        return self.location
    
    def read_storage(self):
        with open(self.storage,'r') as f:
            return f.read()
    def write_storage(self, json_data):
        """ONLY USE IF YOU KNOW WHAT YOU ARE DOING!! IT REWRITES EVERYTHING!!"""
        with open(self.storage,'w') as f:
            f.write(json_data)

    def current_date(self):
        today_time = datetime.datetime.now()
        
        return today_time.strftime("%d/%B/%Y")

    def current_time(self):
        today_date = datetime.datetime.now()
        return today_date.strftime("%I:%M:%S %p")
    
    def generate_storage_template(self, name):
        template = {"weight_tracker":{},"daily_goals":{}}
        with open(name, "w") as f:
            f.write(json.dumps(template, indent=3))
    
    def add_daily_weight(self, 
    weight,
    unit,
    weight_time, 
    weight_date=current_date("self"),
    recording_time=current_time("self"), 
    recording_date=current_date("self")
    ): # really didnt know what to put here so putted anything lol
    
        """ weight dict must contain 
        {weight(in kg) , "kg/pounds" , "time_recorded",  recording_time, recording_date}"""

        storage_data = self.read_storage()
        storage_json_to_dict = json.loads(storage_data)
        storage_json_to_dict['weight_tracker'][weight_date] = {
            'weight': weight,
            'unit': unit,
            'recorded_time': weight_time,
            'logging_date': recording_date,
            'logging_time': recording_time
        }
        json_data = json.dumps(storage_json_to_dict,indent=4)
        self.write_storage(json_data)


if __name__ == "__main__":
    brain = brain()
    brain.generate_storage_template("test_storage.json")
    brain.set_storage_location('test_storage.json')
    brain.add_daily_weight(80, "kg", "night")