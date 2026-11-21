from status import MissionStatus,MissionType
class Mission:
    def __init__(self,mission_id,drone_id,mission_type):
        self.mission_id=mission_id
        self.drone_id=drone_id
        self.mission_type=mission_type
        self.status=MissionStatus.START
    def continue_duty(self):
        self.status=MissionStatus.CONTINUE
    def cancel_duty(self):
        self.status=MissionStatus.CANCEL
    def end_duty(self):
        self.status=MissionStatus.END
    def to_dict(self):
        return{
            "mission_id":
          self.mission_id,
            "drone_id":
          self.drone_id,
            "mission_type":
          self.mission_type.value,
          "status": self.status.value
        }