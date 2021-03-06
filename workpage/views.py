#----------------------------------------
#IMPORTS                
#----------------------------------------

# EXTERNAL
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from pyramid.view import view_config, view_defaults
from collections import defaultdict
import json
import transaction

# INTERAL
from .security import USERS, check_password
from .models import DBSession, SomeData, SomeData_2, Tweets

#----------------------------------------
#CODE                   
#----------------------------------------

@view_defaults(renderer='html/start.pt')
class StartView:
    def __init__(self, request):
        self.request = request

@view_defaults(renderer='html/home.pt')
class HomeView:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid
        self.load_data()
        self.load_data_2()

    # DATATRANSFER
    @view_config(route_name='data', renderer='json')
    def load_data(self): 
        data = DBSession.query(SomeData).all()
        data_ = []
        for i in range(len(data)):
            data_.append({"x_data":data[i].x_data, "y_data":data[i].y_data})
        with open ("workpage/data/data.json","w") as fp:
            json.dump(data_,fp)
        return data_

    @view_config(route_name='data_3', renderer='json')
    def load_data_2(self):
        data_ = open("workpage/data/data_3.json","r")
        data = json.load(data_)
        return data

@view_defaults(renderer='html/coming_shortly.pt')
class ComingShortlyView:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='coming_shortly')
    def hello(self):
        return {'name': 'Hello View'}




    


        
