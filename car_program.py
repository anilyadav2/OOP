from datetime import date

import car_class as cc


d=cc.car('2019_carmy','Toyota')

print(d)


for i in range(5):
    d.accelerate()
    print('The current speed is:',d.get_speed(),'MPH')




for i in range(5):
    d.brake()
    print('The current speed is:',d.get_speed(),'MPH')
