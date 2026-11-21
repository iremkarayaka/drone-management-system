import json
from drone import CargoDrone,SurveillanceDrone
from exceptions import InvalidDroneTypeError, RepositoryFileError
class JsonRepository:
    def __init__(self,file_path,from_dict):
        self.file_path=file_path
        self.from_dict=from_dict

    def save(self,items):
        result=[]
        for drone in items:
            result.append(drone.to_dict())
        with open(self.file_path, "w", encoding="utf-8") as dosya:
             json.dump(result, dosya, ensure_ascii=False, indent=2) 
    def load(self):
      try:
        with open(self.file_path, "r",encoding="utf-8") as dosya:
      
           data= json.load(dosya)
           box=[]
           for item in data:
             new_item = self.from_dict(item)
             box.append(new_item)     
        return box  
      except FileNotFoundError:
                   raise RepositoryFileError()    
