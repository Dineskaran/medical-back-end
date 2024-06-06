# 01. Goods Main Request part

# class goods_main_request:

#     goods_type = None
#     item_name = None
#     item_brand = None
#     item_description = None
#     quantity = None
#     unit = None
#     num_of_exp_date = None
#     status = None

#     def __init__(self, object):

#         if 'goods_type' in object:
#             self.goods_type = object['goods_type']

#         if 'item_name' in object:
#             self.item_name = object['item_name']

#         if 'item_brand' in object:
#             self.item_brand = object['item_brand']

#         if 'item_description' in object:
#             self.item_description = object['item_description']
            
#         if 'quantity' in object:
#             self.quantity = object['quantity']

#         if 'unit' in object:
#             self.unit = object['unit']

#         if 'num_of_exp_date' in object:
#             self.num_of_exp_date = object['num_of_exp_date']

#         if 'status' in object:
#             self.status = object['status']
        

#     def get_goods_type(self):
#         return self.goods_type
    
#     def get_item_name(self):
#         return self.item_name

#     def get_item_brand(self):
#         return self.item_brand

#     def get_item_discription(self):
#         return self.item_description

#     def get_quantity(self):
#         return self.quantity

#     def get_unit(self):
#         return self.unit

#     def get_num_of_exp_date(self):
#         return self.num_of_exp_date

#     def get_status(self):
#         return self.status

#  06. Home Admission Request Part

class home_admission_request:

    id = None
    person_details = None
    if_new = None
    disease = None
    admission_date = None
    room_no = None
    given_things = None
    is_go_clinic = None
    hospital_name = None
    bed_source_image = None
    able_to_act_independently = None
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

        if 'person_details' in object:
            self.person_details = object['person_details']
        
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

        if 'bed_source_img' in object:
            self.bed_source_image = object['bed_source_img']
        
        if 'able_to_act_indepenently' in object:
            self.able_to_act_independently = object['able_to_act_independently']
        
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



    
    def get_person_details(self):
        return self.person_details
    
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
    
    def get_bed_source_image(self):
        return self.bed_source_image
    
    def get_able_to_act_independently(self):
        return self.able_to_act_independently
    
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



# # 08. User Details Request part

# class user_detail_request:

#     user_name = None
#     user_id = None
#     password = None
#     privilege = None
#     create_date = None
#     create_by = None
#     status = None

#     def __init__(self, object):

#         if 'user_name' in object:
#             self.user_name = object['user_name']
        
#         if 'user_id' in object:
#             self.user_id = object['user_id']
        
#         if 'password' in object:
#             self.password = object['password']
        
#         if 'privilege' in object:
#             self.privilege = object['privilege']
        
#         if 'create_date' in object:
#             self.create_date = object['create_date']
        
#         if 'create_by' in object:
#             self.create_by = object['create_by']
        
#         if 'status' in object:
#             self.status = object['status']
        
    
#     def get_user_name(self):
#         return self.user_name
    
#     def get_user_id(self):
#         return self.user_id
    
#     def get_password(self):
#         return self.password
    
#     def get_privilege(self):
#         return self.privilege
    
#     def get_create_date(self):
#         return self.create_date
    
#     def get_create_by(self):
#         return self.create_by
    
#     def get_status(self):
#         return self.status
    

# # 09. Login Info Request part

# class login_info_request:

#     user_details = None
#     log_date = None
#     log_time = None
#     location = None
#     log_out_time = None
#     num_of_attempt = None
#     log_status = None
#     status = None


#     def __init__(self, object):

#         if 'user_detail' in object:
#             self.user_details = object['user_details']

#         if 'log_date' in object:
#             self.log_date = object['log_date']

#         if 'log_time' in object:
#             self.log_time = object['log_time']
        
#         if 'location' in object:
#             self.location = object['location']
        
#         if 'log_out_time' in object:
#             self.log_out_time = object['log_out_time']

#         if 'num_of_attempt' in object:
#             self.num_of_attempt = object['num_of_attempt']

#         if 'log_status' in object:
#             self.log_status = object['log_status']

#         if 'status' in object:
#             self.status = object['status']




#     def get_user_details(self):
#         return self.user_details

#     def get_log_date(self):
#         return self.log_date

#     def get_log_time(self):
#         return self.log_time

#     def get_location(self):
#         return self.location

#     def get_log_out_time(self):
#         return self.log_out_time

#     def get_num_of_attempt(self):
#         return self.num_of_attempt

#     def get_log_status(self):
#         return self.log_status

#     def get_status(self):
#         return self.status


# 10. Drop Down Request part

class dropdown_request:

    list_type = None
    list_value = None
    filter_by = None


    def __init__(self, object):
        
        if 'list_type' in object:
            self.list_type = object['list_type']
        
        if 'list_value' in object:
            self.list_value = object['list_value']
        
        if 'filter_by' in object:
            self.filter_by = object['filter_by']
    

    def get_list_type(self):
        return self.list_type
    
    def get_list_value(self):
        return self.list_value
    
    def get_filter_by(self):
        return self.filter_by
