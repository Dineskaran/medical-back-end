import json

class nurse_duty_response:
    id=None
    date = None
    time = None
    person_details_id = None
    person_type = None
    duty_option = None
    status = None
    note = None
    designation = None
    by_whom = None
    
    
    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)

    
    def set_id(self, id):
        self.id=id

    def set_date(self, date):
        self.date=date

    def set_time(self, time):
        self.time=time

    def set_person_details_id(self, person_details_id):
        self.person_details_id=person_details_id

    def set_person_type(self, person_type):
        self.person_type=person_type

    def set_duty_option(self, duty_option):
        self.duty_option=duty_option

    def set_status(self,status):
        self.status=status

    def set_note(self,note):
        self.note=note
        
    def set_designation(self,designation):
        self.designation=designation

    def set_by_whom(self,by_whom):
        self.by_whom=by_whom
        
        
        
class dutyCountResponse:
    duty_date=None
    dressing_count=None
    catheter_change_count=None
    blood_presser_count = None
    blood_sugar_count = None

    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)


    def set_duty_date(self, duty_date):
        self.duty_date = duty_date   

    def set_dressing_count(self, dressing_count):
        self.dressing_count = dressing_count

    def set_catheter_change_count(self, catheter_change_count):
        self.catheter_change_count = catheter_change_count

    def set_blood_presser_count(self, blood_presser_count):
        self.blood_presser_count = blood_presser_count

    def set_blood_sugar_count(self, blood_sugar_count):
        self.blood_sugar_count = blood_sugar_count
        
        
        
        
class nurse_duty_report_response:
    def __init__(self):
        self.person_id = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.district = None
        self.duty_count = None

    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_person_id(self, person_id):
        self.person_id = person_id

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_gender(self, gender):
        self.gender = gender

    def set_district(self, district):
        self.district = district

    def set_duty_count(self, duty_count):
        self.duty_count = duty_count