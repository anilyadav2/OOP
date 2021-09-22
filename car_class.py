class car:
    def __init__(self,year_model,make):
        self.year_model=year_model
        self.make=make
        self.speed=0
    def accelerate(self):
        self.speed=self.speed+5
        
    def brake(self):
        if self.speed==0:
            print("car is standing already")
        elif self.speed<5:
            self.speed=0
        else:
            self.speed=self.speed-5
    
    def get_speed(self):
        return(self.speed)

        
