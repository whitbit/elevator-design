from operator import attrgetter

class Elevator(object):

    def __init__(self, identity, floor=1, direction='up'):
        self.id = identity
        self.floor = floor
        self.direction = direction

    floor = property(attrgetter('_floor'))

    @floor.setter
    def floor(self, num):
        if not (num > 0 and num < 51): raise Exception("Floor number is invalid.")
        self._floor = num

    def __repr__(self):
        return '<id={}, floor={}, direction={}>'.format(self.id, self.floor, self.direction)


one = Elevator(1, floor=10)
one.floor = 10
two = Elevator(2, floor=10, direction='down')
three = Elevator(3)
four = Elevator(4)

class Building(object):

    def __init__(self):
        self.elevators = []

    def make_request(self, flr, direction):

        elevators_to_check = []

        valid_elevators = []
        
        for elevator in self.elevators:
            if direction == elevator.direction:
                elevators_to_check.append(elevator)

        if len(elevators_to_check) < 1: 
            return None

        for elevator in elevators_to_check:
            if elevator.direction == 'up' and elevator.floor <= flr:
                elevator.distance = elevator.floor - flr
                valid_elevators.append(elevator)
            elif elevator.direction == 'down' and elevator.floor >= flr:
                elevator.distance = flr - elevator.floor
                valid_elevators.append(elevator)
            else:
                elevator.distance = abs(elevator.floor - flr)
                valid_elevators.append(elevator)

        # closest_elevator = min(valid_elevators, key=attrgetter('distance'))

        min_distance = valid_elevators[0].distance
        closest_elevator = valid_elevators[0]

        for ele in valid_elevators:
            if ele.distance < min_distance:
                min_distance = ele.distance
                closest_elevator = ele

        return closest_elevator


    def __repr__(self):
        return '<elevators={}>'.format(self.elevators)


building = Building()
building.elevators.extend([one, two, three, four])
print building.make_request(61, 'down')
