
#  06. Home Admission Request Part

class home_admission_request:

    id = None
    person_details_id = None
    if_new = None
    disease = None
    admission_date = None
    room_no = None
    given_things = None
    is_go_clinic = None
    hospital_name = None
    bed_sores_status = None
    act_independently = None
    toilet_managing = None
    urine_managing = None
    work_in_uyirilai = None
    discharge_date = None
    discharge_reason = None
    note = None
    status = None



    def __init__(self, object):

        if 'id' in object:
            self.id = object['id']

        if 'person_details_id' in object:
            self.person_details_id = object['person_details_id']
        
        if 'if_new' in object:
            self.if_new = object['if_new']

        if 'disease' in object:
            self.disease = object['disease']
        
        if 'admission_date' in object:
            self.admission_date = object['admission_date']
        
        if 'room_no' in object:
            self.room_no = object['room_no']

        if 'given_things' in object:
            self.given_things = object['given_things']
        
        if 'is_go_clinic' in object:
            self.is_go_clinic = object['is_go_clinic']

        if 'hospital_name' in object:
            self.hospital_name = object['hospital_name']

        if 'bed_sores_status' in object:
            self.bed_sores_status = object['bed_sores_status']
        
        if 'act_independently' in object:
            self.act_independently = object['act_independently']
        
        if 'toilet_managing' in object:
            self.toilet_managing = object['toilet_managing']

        if 'urine_managing' in object:
            self.urine_managing = object['urine_managing']

        if 'work_in_uyirilai' in object:
            self.work_in_uyirilai = object['work_in_uyirilai']

        if 'discharge_date' in object:
            self.discharge_date = object['discharge_date']

        if 'discharge_reason' in object:
            self.discharge_reason = object['discharge_reason']

        if 'note' in object:
            self.note = object['note']

        if 'status' in object:
            self.status = object['status']



    
    def get_person_details_id(self):
        return self.person_details_id
    
    def get_id(self):
        return self.id
    
    
    def get_if_new(self):
        return self.if_new

    def get_disease(self):
        return self.disease
    
    def get_admission_date(self):
        return self.admission_date 
    
    def get_room_no(self):
        return self.room_no

    def get_given_things(self):
        return self.given_things
    
    def get_is_go_clinic(self):
        return self.is_go_clinic
    
    def get_hospital_name(self):
        return self.hospital_name
    
    def get_bed_sores_status(self):
        return self.bed_sores_status
    
    def get_act_independently(self):
        return self.act_independently
    
    def get_toilet_managing(self):
        return self.toilet_managing
    
    def get_urine_managing(self):
        return self.urine_managing
    
    def get_work_in_uyirilai(self):
        return self.work_in_uyirilai
    
    def get_discharge_date(self):
        return self.discharge_date
    
    def get_discharge_reason(self):
        return self.discharge_reason
    
    def get_note(self):
        return self.note
    
    def get_status(self):
        return self.status



