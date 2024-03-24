from flask_restful import Api
from .Send.Setup import SetupSend
from .Inquiry.Setup import SetupInquiry

api = Api()

api.add_resource (SetupSend,'/send/setup') 
api.add_resource (SetupInquiry,'/inquiry/setup/') 
