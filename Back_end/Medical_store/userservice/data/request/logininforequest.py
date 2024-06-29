from django.utils import timezone
# 09. Login Info Request part

class login_info_request:

    id = None
    user_details_id = None
    log_date = None
    log_time = None
    location = None
    log_out_time = None
    num_of_attempt = None
    log_status = None
    userid= None


    def __init__(self, object):
        if 'id' in object:
            self.id = object['id']
        
        if 'user_details_id' in object:
            self.user_details_id = object['user_details_id']

        if 'log_date' in object:
            self.log_date = object['log_date']

        if 'log_time' in object:
            self.log_time = object['log_time']
        
        if 'location' in object:
            self.location = object['location']
        
        if 'log_out_time' in object:
            self.log_out_time = object['log_out_time']

        if 'num_of_attempt' in object:
            self.num_of_attempt = object['num_of_attempt']

        if 'log_status' in object:
            self.log_status = object['log_status']

        if 'userid' in object:
            self.userid = object['userid']




    def get_id(self):
        return self.id
    
    def get_user_details_id(self):
        return self.user_details_id

    def get_log_date(self):
        return self.log_date

    def get_userid(self):
        return self.userid

    def get_log_time(self):
        return self.log_time

    def get_location(self):
        return self.location

    def get_log_out_time(self):
        return self.log_out_time

    def get_num_of_attempt(self):
        return self.num_of_attempt

    def get_log_status(self):
        return self.log_status

 
