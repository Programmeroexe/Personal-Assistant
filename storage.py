import json
class storage:
    def __init__(self, storage_location):
        self.location = storage_location

    def check_storage_location(self):
        return self.location