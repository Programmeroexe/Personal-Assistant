import json
import time
import datetime
class storage:
    def __init__(self, storage_location):
        self.location = storage_location

    def check_storage_location(self):
        return self.location
    
    def read_storage(self):
        with open(self.location,'r') as f:
            return f.read()

    def current_date(self):
        today_time = datetime.datetime.now()
        
        return today_time.strftime("%d/%B/%Y")

    def current_time(self):
        today_date = datetime.datetime.now()
        return today_date.strftime("%I:%M:%S")
    
    def generate_storage_template(self, name):
        template = {"weight_tracker":{},"daily_goals":{}}
        with open(name, "w") as f:
            f.write(json.dumps(template, indent=3))

if __name__ == "__main__":
    memory = storage("storage.json")
    # data = json.loads(memory.read_storage())
    # print(data)