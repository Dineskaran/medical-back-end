import json

class user_details_response:
    
    id = None
    user_id = None
    user_name = None  
    password = None
    privilege = None
    create_date = None
    create_by = None
    status = None


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
        
    def set_id(self, id):
        self.id = id

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_password(self, password):
        self.password = password

    def set_privilege(self, privilege):
        self.privilege = privilege

    def set_create_date(self, create_date):
        self.create_date = create_date

    def set_create_by(self, create_by):
        self.create_by = create_by

    def set_status(self, status):
        self.status = status

   
    
# import json
# from datetime import datetime
# from typing import Optional

# class user_details_response:
    
#     def __init__(self, id: Optional[int] = None, user_name: Optional[str] = None, user_id: Optional[str] = None,
#                  password: Optional[str] = None, privilege: Optional[str] = None, create_date: Optional[datetime] = None,
#                  create_by: Optional[str] = None, status: Optional[str] = None):
#         self._id = id
#         self._user_name = user_name
#         self._user_id = user_id
#         self._password = password
#         self._privilege = privilege
#         self._create_date = create_date
#         self._create_by = create_by
#         self._status = status

#     @property
#     def id(self):
#         return self._id

#     @id.setter
#     def id(self, id: int):
#         self._id = id

#     @property
#     def user_name(self):
#         return self._user_name

#     @user_name.setter
#     def user_name(self, user_name: str):
#         self._user_name = user_name

#     @property
#     def user_id(self):
#         return self._user_id

#     @user_id.setter
#     def user_id(self, user_id: str):
#         self._user_id = user_id

#     @property
#     def password(self):
#         return self._password

#     @password.setter
#     def password(self, password: str):
#         self._password = password

#     @property
#     def privilege(self):
#         return self._privilege

#     @privilege.setter
#     def privilege(self, privilege: str):
#         self._privilege = privilege

#     @property
#     def create_date(self):
#         return self._create_date

#     @create_date.setter
#     def create_date(self, create_date: datetime):
#         self._create_date = create_date

#     @property
#     def create_by(self):
#         return self._create_by

#     @create_by.setter
#     def create_by(self, create_by: str):
#         self._create_by = create_by

#     @property
#     def status(self):
#         return self._status

#     @status.setter
#     def status(self, status: str):
#         self._status = status

#     def get(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#                           sort_keys=True, indent=4)

#     def __repr__(self):
#         return (f"UserDetailResponse(id={self._id}, user_name={self._user_name}, user_id={self._user_id}, "
#                 f"password={self._password}, privilege={self._privilege}, create_date={self._create_date}, "
#                 f"create_by={self._create_by}, status={self._status})")
