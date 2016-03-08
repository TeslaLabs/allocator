from __future__ import print_function

import random
import sys

from allocate import Fellow, LivingSpace, Office, Staff

people_file = 'seeds/people.txt'
rooms_file = 'seeds/rooms.txt'


def allocate(people, rooms):
    """
    Parameters
    ----------
    people : list of Person-derived instances
        This is a list of instances that are derived from the Person class.
        They can be either of type Fellow or Staff
    rooms : list of Room-derived instances
        This is a list of instances that are derived from the Room class.
        They can be either of type LivingSpace or Office
    """
    if not people:
        print("No people available to allocate rooms to")
        sys.exit(0)
    available = True  # Variable to save whether rooms are still available
    for person in people:
        room = random.choice(rooms)
        room.add_person(person)


if __name__ == '__main__':
    # Populate people
    unallocated = []
    spaces = []
    with open(people_file) as people:
        for line in people:
            data = line.rstrip().split()
            name = '{} {}'.format(data[0], data[1])
            role = data[2]
            if role == 'FELLOW':
                accomodation = data[3]
                fellow = Fellow(name, accomodation)
                unallocated.append(fellow)
                print(fellow.name, fellow.living_space_choice)
            else:
                staff = Staff(name)
                unallocated.append(fellow)
                print(staff.name)

    # Populate Office and Living Spaces
    with open(rooms_file) as all_spaces:
        for space in all_spaces:
            space_data = space.rstrip().split()
            space_name = space_data[0]
            office_type = space_data[1]
            if office_type == 'OFFICE':
                office = Office(space_name)
                spaces.append(office)
            elif office_type == 'LIVING':
                living = LivingSpace(name)
                spaces.append(living)
