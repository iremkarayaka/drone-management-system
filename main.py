from dotenv import load_dotenv
import os

load_dotenv()

from json_repository import JsonRepository
from drone import CargoDrone, SurveillanceDrone, drone_from_dict
from mission import Mission, mission_from_dict
from service import DroneService
from mission_service import MissionService
from status import MissionType
from exceptions import MissionNotFoundError
from getpass import getpass 
drone_repository = JsonRepository(
    "Repositories/drone.json",
    drone_from_dict
)
mission_repository= JsonRepository(
    "Repositories/mission.json",
    mission_from_dict
)
drone_service = DroneService(drone_repository)
mission_service=MissionService(mission_repository) 
#DRONE İŞLEM#
def drone_ekle():
    dronetype = input("Drone türünü giriniz (1-Kargo/2-Keşif):")

    if dronetype == "1":
        drone_id = input("Drone id giriniz:")

        if drone_service.get_drone_by_id(drone_id):
            print("Bu id zaten mevcut!")
            return

        drone_model = input("Drone model giriniz:")
        drone_batary = int(input("Drone mevcut batarya durumu giriniz: "))
        max_yuk = float(input("Maksimum yük kapasitesini giriniz:"))

        drone = CargoDrone(
            drone_id,
            drone_model,
            drone_batary,
            max_yuk
        )

        drone_service.add_drone(drone)
        print(f"{drone_id} başarıyla eklendi.")

    elif dronetype == "2":
        drone_id = input("Drone id giriniz:")

        if drone_service.get_drone_by_id(drone_id):
            print("Bu id zaten mevcut!")
            return

        drone_model = input("Drone model giriniz:")
        drone_batary = int(input("Drone mevcut batarya durumu giriniz: "))
        max_irtifa = float(input("Maksimum irtifa giriniz:"))

        drone = SurveillanceDrone(
            drone_id,
            drone_model,
            drone_batary,
            max_irtifa
        )

        drone_service.add_drone(drone)
        print(f"{drone_id} başarıyla eklendi.")

    else:
        print("Geçersiz drone türü!")

#DRONE GÖREV İŞLEM#
def gorev_ekle():
    mission_id=input("Görev id giriniz:")
    if mission_service.get_mission_by_id(mission_id):
        print("Bu id zaten mevcut!")
        return 
    
    drone_id = input("Drone id giriniz:")
    if not drone_service.get_drone_by_id(drone_id):
         print("Bu drone bulunamadı!")
         return
    mission_type_input = input("Görev türünü giriniz (1-Kargo/2-Keşif/3-Haritalama):")

    if mission_type_input == "1":
     mission_type = MissionType.CARGO
    elif mission_type_input == "2":
     mission_type = MissionType.RECON
    elif mission_type_input == "3":
     mission_type = MissionType.MAP
    else:
     print("Geçersiz görev türü!")
     return
    mission=Mission(mission_id,drone_id,mission_type)
    mission_service.add_mission(mission)
    print(f"{mission_id} başarıyla eklendi.")


    
                                     #GİRİŞ EKRANI  VE MENÜ#
from datetime import datetime
simdi=datetime.now()
formatli_tarih = simdi.strftime("%d-%m-%Y %H:%M")
print("="* 45)
print("**** Drone Yönetim Sistemi****")
print("="* 45)
print("\n GİRİŞ EKRANI")
hak = 3

while hak > 0:
    kullanıcı_adi = input("Kullanıcı Adı:")
    sifre = getpass("Şifre:")

    if kullanıcı_adi == os.getenv("DRONE_USERNAME") and sifre == os.getenv("DRONE_PASSWORD"):
        print("Hoşgeldiniz.")
        print(f"Giriş zamanı: {formatli_tarih}")
        break

    hak -= 1
    print("Kullanıcı adı veya şifre yanlış.")
    print(f"Kalan hakkınız: {hak}")
    
    if hak == 0:
      print("Giriş hakkınız bitti.")
      exit()
while True:
   print("="*45)
   print("MENU")
   print("="*45)
   print("1-Drone işlemleri")
   print("2-Görev işlemleri")
   print("0-Çıkış")
   secim=(input("Seçiminiz:"))
   if secim=="1":
      print("Drone işlemleri seçildi")
      while True:
         print("🚁DRONE İŞLEMLERİ")
         print("1-Drone ekle")
         print("2-Drone listele")
         print("3-Drone güncelle")
         print("4-Drone sil")
         print("5-Ana menüye dön")
         secim=input("Drone işlemeni seçiniz:")
         if secim=="1":
          drone_ekle()
         elif secim=="2":
            print("Drone listele")
            drones = drone_service.list_drones()
            if not drones:
                print("Kayıtlı drone bulunamadı!")
            for drone in drones:
                print(f"ID: {drone.id}")
                print(f"MODEL:{drone.model}")
                print(f"BATARYA:{drone.batarya}")
                if isinstance(drone, CargoDrone):
                    print("TÜR:Kargo Drone")
                    print(f"Maksimum yük:{drone.max_payload} kg")
                else:
                    print("TÜR:Keşif Drone")
                    print(f"Maksimum irtifa:{drone.max_altitude_m} m")
                    

         elif secim=="3":
            print("Drone güncelle")
            drone_id=input("Güncellenicek drone id:")
            if not drone_service.get_drone_by_id(drone_id):
                   print("Drone bulunamadı!")
                   continue
            new_model=input("Yeni model:")
            drone_service.update_drone(drone_id, model=new_model)
            print(f"{new_model} başarıyla kaydedildi.")
            new_batary=int(input("Güncel batarya durumu:"))
            drone_service.update_drone(drone_id,batarya=new_batary)
         elif secim=="4":
            print("Drone sil")
            drone_id=input("Silincek drone id:")
            if not drone_service.get_drone_by_id(drone_id):
                               print("Drone bulunamadı!")
                               continue
            
            silinen= drone_service.delete_drone(drone_id)
            print(f"{silinen} başarıyla silindi.")
         elif secim=="5":
            print("Ana menüye dön")
            break 
         else:
            print("Geçersiz işlem")
   elif secim=="2":
      print("Görev işlemleri seçildi")
      while True:
          print(" 🎯GÖREV İŞLEMLERİ")
          print("1-Görev ekle")
          print("2-Görev listele")
          print("3-Görevi devam ettir")
          print("4-Görevi iptal et")
          print("5-Görevi bitir")
          print("6-Ana menüye dön")
          secim=input("Görev işlemini seçiniz:")
          if secim =="1":
              gorev_ekle()
          elif secim=="2":
              print("Görev listelesi")
              gorev=mission_service.list_mission()
              if not gorev:
                  print("Kayıtlı görev bulunamadı!")
              for mission in gorev:
                 print(f"Drone İd: {mission.drone_id}")
                 print(f"Görev İd: {mission.mission_id}")
                 print(f"Görev Türü: {mission.mission_type.value}")
                 print(f"Durum: {mission.status.value}")
          elif secim=="3":
               mission_id = input("Devam ettirilecek görev id: ")
               try:
                mission_service.continue_mission(mission_id)
                print("Görev sistemde devam ediyor")

               except MissionNotFoundError:
                   print("Görev bulunamadı!")
                 
          elif secim=="4":   
             mission_id=input("İptal ettirilicek görev id:")
             try:
                 mission_service.cancel_mission(mission_id)
                 print("Görev iptal edildi.")

             except MissionNotFoundError:
                print("Görev bulunamadı!")
          elif secim=="5":
              mission_id=input("Sonlandıracağınız görev id:")
              try:
                  mission_service.end_mission(mission_id)
                  print("İşlem başarıyla sonlandırıldı.")
              except MissionNotFoundError:
                  print("Görev bulunamadı!")
          elif secim=="6":
              print("Ana menüye dön")
              break 
              
   elif secim=="0":
      print("Çıkış yapılıyor...")
      break 
   else:
      print("Geçersiz işlem!")
