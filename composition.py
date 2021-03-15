class vehicle:
    def __init__(self, VIN, engine, tires):
        self.vin = VIN
        self.engine = engine
        self.tires = tires

class tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 2

    def get_pressure(self):
        print(f'Current pressure is {self.pressure}')
        return

    def pump(self, psi):
        self.pressure = psi
        print(f'Tire pressure changed to {self.pressure}')
        return

class engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.status = 'off'

    def start(self):
        if self.status == 'off':
            self.status = 'on'
            print(f'{self.fuel_type} engine started')
            return
        else:
            print(f'Engine already running')
            return

    def stop(self):
        if self.status == 'on':
            self.status = 'off'
            print(f'{self.fuel_type} engine switched off')
            return
        else:
            print(f'Engine already off')
            return

    def get_state(self):
        print(f'engine is {self.status}')
        return

city_tires = tires(15)
off_road_tires = tires(18)

eliectric_engine = engine('electricity')
petrol_engine = engine('petrol')

city_car = vehicle('cvin2589', eliectric_engine, city_tires)
all_terain_car = vehicle('avin1478', petrol_engine, off_road_tires)


print(city_car.vin)
city_car.tires.get_pressure()
city_car.engine.start()
city_car.engine.start()
city_car.engine.get_state()
city_car.engine.stop()

print()

print(city_car.vin)
all_terain_car.tires.get_pressure()
all_terain_car.tires.pump(2.3)
all_terain_car.tires.get_pressure()
all_terain_car.engine.start()
all_terain_car.engine.get_state()
all_terain_car.engine.stop()
all_terain_car.engine.stop()
