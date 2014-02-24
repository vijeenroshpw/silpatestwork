from modulehelper import modules, modulenames, MODULES, enabled_modules, \
        load_modules
from json import loads, dumps
from flask.ext import restful


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

    def get(self,method,params):
        module_instance = MODULES.get(method.split('.')[0])
        args = params.split('|')    
        result = self.call(getattr(module_instance,method.split('.')[-1]),args) 
        return self.translate_result(result,None,"1")
 






 

 
  
  


