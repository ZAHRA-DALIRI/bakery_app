from model.da.da import DataAccess
from datetime import date, datetime

from model.da.da import DataAccess
from model.entity import *

from model.entity.sell import Sell

customer1 = Customer("zahraaa", "daliri", "0023359951", "09120460699", "zahradaliri3@gmail.com",
                     "تهران-شهریار", date(1379, 5, 12), True)

c_da = DataAccess(Customer)
c_da.save(customer1)
customer = c_da.find_all()
print(customer1)

employee1 = Employee("ربابه", "اشقاب", "6189839118",
                     "09124231980", "dalirizahra29@gmail.com", "تهران",
                     "د123", date(1345, 6, 3),
                     "کامپیوتر", "دیپلم", "18.88",
                     date(1360, 2, 24),
                     date(1380, 4, 5), "تهران", True)
e_da = DataAccess(Employee)
e_da.save(employee1)
employee = e_da.find_by_employee_id(1)
print(employee1)

bakery_device = Device("bakery a1000", "دستگاه تمام اتوماتیک لواش (روتاری)", date(1403, 3, 10))
d_da = DataAccess(Device)
d_da.save(bakery_device)
bakery_device = d_da.find_by_device_id(1)
print(bakery_device)

comp1 = Component("Hatron", "HMBT130SL", "HMBT-130-0302B2716",
                  "Bluetooth Silent Mouse",
                  date(1403, 2, 2), bakery_device)
comp2 = Component("هترون", "HMBT135SL", "HMBT-135-0302B2715",
                  "موس بلوتوثی سایلنت",
                  date(1403, 3, 3), bakery_device)
co_da = DataAccess(Component)
co_da.save(comp1)
print(comp1)
co_da.save(comp2)
print(comp2)

d = d_da.find_by_device_id(1)
print("DEVICE :", d)
print("COMP :", d.components)
sell = Sell(datetime.now(), "500,000,000 ریال", bakery_device, customer1, employee1)
sell_da = DataAccess(Sell)
sells = sell_da.save(sell)
