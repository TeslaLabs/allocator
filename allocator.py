#!/usr/bin/env python
"""                          ALLOCATOR

This program handles room allocation system for office and living spaces
in one of Andela's facilities called Amity.

Usage:
  allocator.py create_office <room_name>...
  allocator.py create_living_space <room_name>...
  allocator.py add_fellows <fellow_name>... [--accomodation=n]
  allocator.py add_staff <staff_name>...
  allocator.py reallocate_person (<person_identifier> <new_room_name>)...
  allocator.py print_allocations [--output-allocations=allocations.txt]
  allocator.py print_unallocated [--output-unallocated=unallocated.txt]
  allocator.py print_room <room_name>
  allocator.py load_people <people_input_file>
  allocator.py (-h | --help)
  allocator.py --version

Options:
  -h, --help                      Show this screen and exit
  -a, --accomodation=<Y|N>        Wants accomodation [default: N]
  -oa, --output-allocations FILE  Specify output file [default: ./allocations.txt]
  -ou, --output-unallocated FILE  Specify output file [default: ./unallocated.txt]
  --version                       Show version.

"""
from __future__ import print_function

from docopt import docopt

from models import Facility


__version__ = '0.1.0'
# Create Facility instance representing the Amity Facility
amity = Facility('Amity')

if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    print(args)

    if (args['create_office']):
        amity.create_rooms('office', args['<room_name>'])
    elif args['create_living_space']:
        amity.create_rooms('living_space', args['<room_name>'])
    elif args['add_fellows']:
        amity.add_fellows(args['<fellow_name>'], args['--accomodation'])
    elif args['add_staff']:
        amity.add_staff(args['<staff_name>'])
    elif args['load_people']:
        amity.load_people(args['<people_input_file>'])
