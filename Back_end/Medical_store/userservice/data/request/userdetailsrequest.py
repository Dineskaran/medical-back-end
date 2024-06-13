# 08. User Details Request part

class user_details_request:
    
    id = None
    user_name = None
    user_id = None
    password = None
    privilege = None
    create_date = None
    create_by = None
    status = None

    def __init__(self, object):

        
        if 'id' in object:
            self.id = object['id']    
        
        if 'user_name' in object:
            self.user_name = object['user_name']

        if 'password' in object:
            self.password = object['password']
        
        if 'user_id' in object:
            self.user_id = object['user_id']
            
        if 'privilege' in object:
            self.privilege = object['privilege']
        
        if 'create_date' in object:
            self.create_date = object['create_date']
        
        if 'create_by' in object:
            self.create_by = object['create_by']
        
        if 'status' in object:
            self.status = object['status']
        
   
    def get_id(self):
        return self.id
     
    def get_user_name(self):
        return self.user_name
    
    def get_user_id(self):
        return self.user_id
    
    def get_password(self):
        return self.password
    
    def get_privilege(self):
        return self.privilege
    
    def get_create_date(self):
        return self.create_date
    
    def get_create_by(self):
        return self.create_by
    
    def get_status(self):
        return self.status
    
