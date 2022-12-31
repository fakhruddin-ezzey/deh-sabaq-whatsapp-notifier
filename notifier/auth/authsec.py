from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class DEHAdminRegister():

    __rq =  None

    def __init__(self, to_be_morphed_data) -> None:
        self.__rq = to_be_morphed_data

    def __generate_username(self):
        self.__rq['username'] = self.__rq['email'].split('@')[0]
    
    def __make_password(self):
        self.__rq['password'] = make_password(self.__rq['password'])
    
    def __make_admin_inactive(self):
        self.__rq['is_active'] = False
    
    def return_morphed_request(self):
        self.__generate_username()
        self.__make_password()
        self.__make_admin_inactive()
        return self.__rq

