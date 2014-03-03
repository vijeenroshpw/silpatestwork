from modulehelper import modules, modulenames, MODULES, enabled_modules, \
        load_modules
from json import loads, dumps
from flask import request
from flask.ext import restful
from flask.ext.restful import reqparse



parser = reqparse.RequestParser()
parser.add_argument('text',type=str)
parser.add_argument('targetlang',type=str)
parser.add_argument('font',type=str)

class RestHandler(restful.Resource):
    def __init__(self):
        ''' Loads the necessary modules '''
        load_modules()

    def translate_result(self,result,error,id_):    #parameters are just kept unaltered can be changed in time
        if error != None:
            error = {"name": error.__class__.__name__, "message": error}
            result = None

        #its showing some issues when dumps() is used, so now using python dict
      
        try:
            data = {"result": result, "id": id_, "error": error}
        except:
            error = {"name": "JSONEncodeException", \
                    "message": "Result object is not serializable"}
            data = {"result": None, "id": id_, "error": error}

        return data

   
    def call(self, method, args):
        _args = None
        for arg in args:
            if arg != '':
                if _args == None:
                    _args = []
                _args.append(arg)

        if _args == None:
            # No arguments
            return method()
        else:
            return method(*_args)

    def get(self,module,method):
        args = parser.parse_args()
        arglist=[]
        for arg in args.values():
            if arg!= None:
              arglist.append(arg)

        print arglist[0:2]
        module_instance = MODULES.get(module) # retrieve module instance
        result = self.call(getattr(module_instance,method),arglist[0:2]) # we only require first two arguments
        return self.translate_result(result,None,"1")
 
 
    def post(self,module,method):
        print request.data
        args = json.loads(request.data) 
        arglist = args.values()
        print arglist
        module_instance = MODULES.get(module)
        result = self.call(getattr(module_instance,method),arglist)
        return self.translate_result(result,None,"1")
 

 

 

 
  
  


