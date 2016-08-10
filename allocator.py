#!/usr/bin/env python
"""                         Allocator

This program handles room allocation system for office and living spaces
in one of Andela's facilities called Amity.

Usage:
  allocator.py create_rooms (living|office) <room_name>...
  allocator.py add_person (fellow|staff) <name>... [--accomodation=n]
  allocator.py reallocate_person ((fellow|staff) <person_identifier> <new_room_name>)...
  allocator.py print_allocations [--output-allocations=allocations.txt]
  allocator.py print_unallocated [--output-unallocated=unallocated.txt]
  allocator.py print_room <room_name>
  allocator.py load_people <people_input_file>
  allocator.py load_state <sqlite_database>
  allocator.py (-i | --interactive)
  allocator.py (-h | --help)
  allocator.py --version

Options:
  -h, --help                      Show this screen and exit.
  -i, --interactive               Interactive Mode.
  -a, --accomodation=(Y|N)        Wants accomodation [default: N].
  -oa, --output-allocations FILE  Specify output file [default: ./allocations.txt]
  -ou, --output-unallocated FILE  Specify output file [default: ./unallocated.txt]
  --version                       Show version.

"""
from __future__ import print_function

__version__ = '0.1.0'

import random
import sys

from docopt import docopt

from models import Fellow, LivingSpace, Office, Staff


if __name__ == '__main__':
    args = docopt(__doc__, version=__version__)
    print(args)
