import json



class login_info_response:

    id = None
    user_details_id = None
    log_date = None
    log_time = None
    location = None
    log_out_time = None
    num_of_attempt = None
    log_status = None
    userid = None
    
    
    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)
    
    def set_id(self,id):
        self.id=id
    
    def set_user_details_id(self,user_details_id):
        self.user_details_id=user_details_id
    
    def set_log_date(self,log_date):
        self.log_date=log_date
    
    def set_log_time(self,log_time):
        self.log_time= log_time
        
    def set_location(self,location):
        self.location= location
        
    def set_log_out_time(self, log_out_time):
        self.log_out_time= log_out_time
        
    def set_num_of_attempt(self,  num_of_attempt):
        self.num_of_attempt= num_of_attempt
        
    def set_log_status(self,log_status):
        self.log_status=log_status
        
    def set_userid(self,userid):
        self.userid=userid
        
    
    
    
