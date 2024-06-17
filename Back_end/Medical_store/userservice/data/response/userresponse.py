import json


#  06. Home Admission Response Part

class response_home_admission:
    
   
    person_details_id = None
    id=None
    if_new=None
    disease=None
    admission_date=None
    room_no=None
    given_things=None
    is_go_clinic=None
    hospital_name=None
    bed_sores_status=None
    act_independently=None
    toilet_managing=None
    urine_managing=None
    work_in_uyirilai=None
    discharge_date=None
    discharge_reason=None
    note=None
    status=None

    def get(self):
      return json.dumps(self, default=lambda o: o.__dict__,
                         sort_keys=True, indent=4)

    def set_id(self,id):
        self.id=id

    def set_person_details_id(self, person_details_id):
        self.person_details_id=person_details_id

    def set_if_new(self, if_new):
        self.if_new=if_new

    def set_disease(self, disease):
        self.disease=disease

    def set_admission_date(self,admission_date):
        self.admission_date=admission_date

    def set_room_no(self, room_no):
        self.room_no=room_no

    def set_given_things(self, given_things):
        self.given_things=given_things

    def set_is_go_clinic(self,is_go_clinic):
        self.is_go_clinic=is_go_clinic

    def set_hospital_name(self, hospital_name):
        self.hospital_name=hospital_name

    def set_bed_sores_status(self, bed_sores_status):
        self.bed_sores_status=bed_sores_status

    def set_act_independently(self, act_independently):
        self.act_independently=act_independently

    def set_toilet_managing(self, toilet_managing):
        self.toilet_managing=toilet_managing

    def set_urine_managing(self, urine_managing):
        self.urine_managing=urine_managing

    def set_work_in_uyirilai(self, work_in_uyirilai):
        self.work_in_uyirilai=work_in_uyirilai

    def set_discharge_date(self, discharge_date):
        self.discharge_date=discharge_date

    def set_discharge_reason(self, discharge_reason):
        self.discharge_reason=discharge_reason

    def set_note(self, note):
        self.note=note

    def set_status(self, status):
        self.status=status




