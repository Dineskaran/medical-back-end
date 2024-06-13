import json
import os

class person_details_response:
    
    id = None
    person_type = None
    person_no = None
    first_name = None
    last_name = None
    date_of_birth = None
    gender = None
    civil_status = None
    nic = None
    effect = None
    effect_type = None
    effect_status = None
    effect_reason = None
    effect_date = None
    is_bed_sore = None
    contact_number = None
    address = None
    district = None
    now_status = None
    status = None
    
    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)
    
    
    def set_id (self,id ):
        self.id =id
        
    def set_person_type(self,person_type ):
        self.person_type =person_type
        
    def set_person_no(self, person_no ):
        self. person_no = person_no
        
    def set_first_name(self,first_name ):
        self.first_name =first_name
        
    def set_last_name(self,last_name ):
        self.last_name =last_name
        
    def set_date_of_birth(self,date_of_birth ):
        self.date_of_birth =date_of_birth
        
    def set_gender(self,gender):
        self.gender= gender

    def set_civil_status(self,civil_status):
        self.civil_status= civil_status

    def set_nic(self,nic):
        self.nic= nic

    def set_effect(self,effect):
        self.effect= effect

    def set_effect_type(self,effect_type):
        self.effect_type= effect_type

    def set_effect_status(self,effect_status):
        self.effect_status= effect_status

    def set_effect_reason(self,effect_reason):
        self.effect_reason= effect_reason

    def set_effect_date(self,effect_date):
        self.effect_date = effect_date
        
    def set_is_bed_sore(self,is_bed_sore):
        self.is_bed_sore = is_bed_sore
        
    def set_contact_number(self,contact_number):
        self.contact_number = contact_number
        
    def set_address(self,address):
        self.address = address
        
    def set_district(self,district):
        self.district = district
        
    def set_now_status(self,now_status):
        self.now_status = now_status
        
    def set_status(self,status):
        self.status = status
        