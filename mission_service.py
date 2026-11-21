from json_repository import JsonRepository
from exceptions import MissionNotFoundError
class MissionService:
    def __init__(self,repository):
        self.repository=repository
    def add_mission(self,drone):
        add=self.repository.load()
        add.append(drone)
        self.repository.save(add)
    def list_mission(self):
        return self.repository.load()
    def get_mission_by_id(self,mission_id):
        missions=self.list_mission()
        for mission in missions:
            if mission.mission_id==mission_id:
                return mission 
        raise MissionNotFoundError()
    def continue_mission(self,mission_id):
        missions=self.list_mission()
        for mission in missions:
            if mission.mission_id==mission_id:
                mission.continue_duty()
                self.repository.save(missions)
                return mission 
        raise MissionNotFoundError()

    def end_mission(self,mission_id):
        end=self.list_mission()
        for mission in end:
            if mission.mission_id==mission_id:
               mission.end_duty()
               self.repository.save(end)
               return mission 
        raise MissionNotFoundError()
    def cancel_mission(self,mission_id):
        cancel=self.list_mission()
        for mission in cancel:
            if mission.mission_id==mission_id:
                mission.cancel_duty()
                self.repository.save(cancel)
                return mission 
        raise MissionNotFoundError()
