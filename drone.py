from abc import ABC, abstractmethod
from status import DroneStatus, MissionType
class Drone(ABC):
    def __init__(self,id,model,batarya): 
     self.id=id
     self.model=model 
     self.batarya=batarya
    @abstractmethod
    def Mission_types(self):
        pass

    @property 
    def status(self):
        if self.batarya<30:
           return DroneStatus.CANTFLY
        elif self.batarya<50:
           return DroneStatus.LOWBATARY
        elif self.batarya<80:
           return DroneStatus.FLYABLE
        else:
           return DroneStatus.READY
    def to_dict(self):
      return{
         "id":self.id,
         "model":self.model,
         "batarya":self.batarya
      }

class CargoDrone(Drone):
   def __init__(self,id,model,batarya,max_payload):
      super(). __init__(id,model,batarya)
      self.max_payload=max_payload
   def Mission_types(self):
      return [MissionType.CARGO]
   def to_dict(self):
         data=super().to_dict()
         data["max_payload"]=self.max_payload
         data["type"] = "cargo"
         return data

      

class SurveillanceDrone(Drone):
   def __init__(self,id,model,batarya,max_altitude_m):
      super().__init__(id,model,batarya)
      self.max_altitude_m=max_altitude_m
   def Mission_types(self):
      return [MissionType.RECON,MissionType.MAP]
   def to_dict(self):
         data= super().to_dict()
         data["max_altitude_m"]=self.max_altitude_m
         data["type"] = "surveillance"
         return data 
      
