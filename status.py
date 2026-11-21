
from enum import Enum       
class DroneStatus(Enum):
    READY="Uçuşa hazır"
    FLYABLE="Uçabilir"
    LOWBATARY="Düşük batarya"
    CANTFLY="Uçamaz"

class MissionStatus(Enum):
    START="Görev atandı."
    CONTINUE="Görev devam ediyor."
    CANCEL="Görev iptal edildi."
    END="Görev bitti."

class MissionType(Enum):
    CARGO="Kargo taşıma görevi"
    RECON="Keşif görevi"
    MAP="Çevre haritalama görevi"

