import json

class user_details_response:
    
    id = None
    userid = None
    user_name = None  
    password = None
    privilege = None
    create_date = None
    create_by = None
    status = None
    


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
        
    def set_id(self, id):
        self.id = id

    def set_userid(self, userid):
        self.userid = userid

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_password(self, password):
        self.password = password

    def set_privilege(self, privilege):
        self.privilege = privilege

    def set_create_date(self, create_date):
        self.create_date = create_date

    def set_create_by(self, create_by):
        self.create_by = create_by

    def set_status(self, status):
        self.status = status

   
    
