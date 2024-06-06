# from userservice.data.response.userresponse import dropdown_response
# from userservice.models import dropdown_table


# class utlis:
#     male = 1
#     female = 2
#     male_val = 'male'
#     female_val = 'female'


#     def get_gender(self, value):
#         id = [utlis.male, utlis.famale]
#         val = [utlis.male_val, utlis.female_val]
#         length = len(id)
#         for i in id : 
#             if value == utlis.male:
#                 data = utlis.male_val
#                 list_item.append(data)

#             elif value == utlis.female:
#                 data = utlis.female_val
#                 list_item.append(data)
#             return list_item


#     def drop_down(self):
#         id = [utlis.male, utlis.female]
#         val = [utlis.male_val, utlis.female_val]
#         length = len(id)
#         list_item =List()
#         for i in range(length):
#             data = {"id": id[i], "value": val[i]}
#             list_item.append(data)
#         return list_item

#     def get_dropdown(self,id_obj):
#         obj=drop_down.objects.get(id=id_obj)

#         response = dropdown_response()
#         # response.set_id(obj.id)
#         # response.set_list_type(obj.list_type)
#         response.set_list_value(obj.list_value)
#         response.district=obj.list_value
#         # response.set_status(obj.status)

#         return response
