import json


#  07. Nurse Duty Request part

class nurse_duty_response:

    id= None
    date = None
    time = None
    person_details = None
    person_type = None
    duty_option = None
    status = None
    note = None
    
    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)
      
    def set_id(self,id):
        self.id=id

    def set_date(self,date):
        self.date=date

    def set_time(self, time):
        self.time=time

    def set_person_details(self, person_details):
        self.person_details=person_details

    def set_person_type(self,person_type):
        self.person_type=person_type

    def set_duty_option(self,duty_option):
        self.duty_option=duty_option

    def set_status(self,status):
        self.status=status

    def set_note(self,note):
        self.note=note
