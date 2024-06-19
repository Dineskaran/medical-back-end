
#  07. Nurse Duty Request part

class nurse_duty_request:

    id= None
    date = None
    time = None
    person_details_id = None
    person_type = None
    duty_option = None
    status = None
    note = None
    designation = None
    by_whom = None
    


    def __init__(self, object):

        if 'id' in object:
            self.id = object['id']
            
        if 'date' in object:
            self.date = object['date']
        
        if 'time' in object:
            self.time = object['time']
        
        if 'person_details_id' in object:
            self.person_details_id = object['person_details_id']
        
        if 'person_type' in object:
            self.person_type = object['person_type']
        
        if 'duty_option' in object:
            self.duty_option = object['duty_option']
        
        if 'status' in object:
            self.status = object['status']
        
        if 'note' in object:
            self.note = object['note']
            
        if 'designation' in object:
            self.designation = object['designation']
        
        if 'by_whom' in object:
            self.by_whom = object['by_whom']
        

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date
    
    def get_time(self):
        return self.time

    def get_person_details_id(self):
        return self.person_details_id

    def get_person_type(self):
        return self.person_type

    def get_duty_option(self):
        return self.duty_option

    def get_status(self):
        return self.status

    def get_note(self):
        return self.note
    
    def get_designation(self):
        return self.designation

    def get_by_whom(self):
        return self.by_whom


