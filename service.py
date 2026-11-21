from Repositories.json_repository import JsonRepository
class DroneService:
    def __init__(self,repository):
        self.repository=repository
    def add_drone(self,drone):
        drones = self.repository.load()
        drones.append(drone)
        self.repository.save(drones)
    def list_drones(self):
       return self.repository.load()
    
    def get_drone_by_id(self, drone_id):
        drones=self.list_drones()
        for drone in drones:
            if drone.id== drone_id:
                return drone
            
        return None
    def update_drone(self, drone_id, model=None, batarya=None):
        update=self.list_drones()
        for drone in update :
          if drone.id== drone_id:
            if model is not None:
                drone.model=model
            if batarya is not None:
                drone.batarya=batarya
            self.repository.save(update)
            return drone
        return None
    def delete_drone(self,drone_id):
        liste=self.list_drones()
        for drone in liste:
            if drone.id== drone_id:
                liste.remove(drone)
                self.repository.save(liste)
                return drone
        return None

