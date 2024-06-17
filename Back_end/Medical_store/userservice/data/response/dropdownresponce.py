import json

class dropdown_response:
    id=None
    list_type = None
    list_value = None
    filter_by = None
    status = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id
    
    def set_filter_by(self, filter_by):
        self.filter_by = filter_by

    def set_list_type(self, list_type):
        self.list_type = list_type

    def set_list_value(self, list_value):
        self.list_value = list_value

    def set_status(self, status):
        self.status = status