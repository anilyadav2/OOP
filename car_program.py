from datetime import date

import car_class as cc


d=cc.car('19_sx','Toyota')

print(d)


for i in range(5):
    d.accelerate()
    print('The current speed is:',d.get_speed(),'MPH')




for i in range(5):
    d.brake()
    print('The current speed is:',d.get_speed(),'MPH')
