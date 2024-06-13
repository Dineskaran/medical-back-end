class person_details_request:
    
    def __init__(self, object):
        self.id = object.get('id', None)
        self.person_type = object.get('person_type', None)
        self.person_no = object.get('person_no', None)
        self.first_name = object.get('first_name', None)
        self.last_name = object.get('last_name', None)
        self.date_of_birth = object.get('date_of_birth', None)
        self.gender = object.get('gender', None)
        self.civil_status = object.get('civil_status', None)
        self.nic = object.get('nic', None)
        self.effect = object.get('effect', None)
        self.effect_type = object.get('effect_type', None)
        self.effect_status = object.get('effect_status', None)
        self.effect_reason = object.get('effect_reason', None)
        self.effect_date = object.get('effect_date', None)
        self.is_bed_sore = object.get('is_bed_sore', None)
        self.contact_number = object.get('contact_number', None)
        self.address = object.get('address', None)
        self.district = object.get('district', None)
        self.now_status = object.get('now_status', None)
        self.status = object.get('status', None)

    def get_id(self):
        return self.id

    def get_person_type(self):
        return self.person_type

    def get_person_no(self):
        return self.person_no

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_gender(self):
        return self.gender

    def get_civil_status(self):
        return self.civil_status

    def get_nic(self):
        return self.nic

    def get_effect(self):
        return self.effect

    def get_effect_type(self):
        return self.effect_type

    def get_effect_status(self):
        return self.effect_status

    def get_effect_reason(self):
        return self.effect_reason

    def get_effect_date(self):
        return self.effect_date

    def get_is_bed_sore(self):
        return self.is_bed_sore

    def get_contact_number(self):
        return self.contact_number

    def get_address(self):
        return self.address

    def get_district(self):
        return self.district

    def get_now_status(self):
        return self.now_status

    def get_status(self):
        return self.status
