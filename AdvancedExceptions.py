class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError('Crew is incomplete') from e


def fuel_check():
    try:
        print('Fuel tank is full in {}%'.format(100/0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError('Problem with fuel gauge') from e

def batteries_check():
    try:
        for battery in batteries:
            assert battery == True, "AssertionError"
    except AssertionError as e:
        raise RocketNotReadyError('All batteries not connected') from e

def circuits_check():
    try:
        deviation = 0
        for line in circuit_volts:
            deviation += int(circuit_volts[line])/line
        print(f'circuits running at voltrage deviation of {deviation}')
    except TypeError as e:
        raise RocketNotReadyError('All circuits not connected') from e


crew = ['John', 'Mary', 'Mike']
fuel = 100
batteries = [True, True, True, False]
circuit_volts = {'220':220, '220':210, '220':215, '220':None}
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print('Final check procedure')

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))
