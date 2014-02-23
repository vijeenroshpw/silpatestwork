from modulehelper import modules, modulenames, MODULES, enabled_modules, \
        load_modules

from flask.ext import restful


class RestHandler(restful.Resource):
  def get(self,functionality):
    return functionality


 

 
  
  


