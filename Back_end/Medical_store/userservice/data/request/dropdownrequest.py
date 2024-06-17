

# 10. Drop Down Request part

class dropdown_request:
    id = None
    list_type = None
    list_value = None
    filter_by = None


    def __init__(self, object):
        
        if 'id' in object:
            self.id = object['id']
        
        if 'list_type' in object:
            self.list_type = object['list_type']
        
        if 'list_value' in object:
            self.list_value = object['list_value']
        
        if 'filter_by' in object:
            self.filter_by = object['filter_by']
    

    def get_id(self):
        return self.id
    
    def get_list_type(self):
        return self.list_type
    
    def get_list_value(self):
        return self.list_value
    
    def get_filter_by(self):
        return self.filter_by
