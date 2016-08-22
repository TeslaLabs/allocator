# Allocator
[![Build Status](https://travis-ci.org/kevgathuku/allocator.svg?branch=master)](https://travis-ci.org/kevgathuku/allocator)  [![Coverage Status](https://coveralls.io/repos/github/kevgathuku/allocator/badge.svg?branch=master)](https://coveralls.io/github/kevgathuku/allocator?branch=master)

This project implements a room allocation system for one of Andela's facilities called Amity.

## Constraints

Amity has rooms which can be offices or living spaces.   
- An office can occupy a maximum of 6
people.
- A living space can inhabit a maximum of 4 people.
- A person to be allocated could be a fellow or staff.
- Staff cannot be allocated living spaces.
- Fellows have a choice to choose a living space or not.

This system should automatically allocate spaces to people at random.

### Project Setup

**Prerequisites:** Make sure you have `git`, `python` and `virtualenvwrapper` installed

- Clone the project from GitHub  
`git clone git@github.com:kevgathuku/allocator.git`
- Change directory into the newly-created project directory  
`cd allocator`
- Create a virtualenv to isolate project dependencies  
 `mkvirtualenv allocator`
- Activate the virtualenv  
`workon allocator`
- Install the project dependencies  
`make install`
- Run the main project file. You should see the help menu and you should be good to go 😄  
`python allocator.py`

## Command Line Interface Usage

 - `python allocator.py` - Lists usage options and all available commands
 - `python allocator.py --help` - Lists usage options and all available commands
 - `python allocator.py create_office <room_name>...` - Create one or more offices in the Amity Facility
 - `python allocator.py create_living_space <room_name>...` - Create one or more offices in the Amity Facility
 - `python allocator.py add_fellows <fellow_name>... [--accomodation=n]` - Add one or more fellows to the Amity Facility. The `--accomodation` flag specifies whether they have chosen to take up accomodation. The default is `NO`
 - `python allocator.py add_staff <staff_name>...` - Add one or more staff members to the Amity Facility
 - `python allocator.py reallocate_person (<person_identifier> <new_room_name>)...` - Reallocate the person with `person_identifier` to `new_room_name`

- `python allocator.py load_people <people_input_file>` - Adds people to rooms from the `people_input_file` text file.
- `python allocator.py print_allocations [--output-allocations=allocations.txt]` - Prints a list of allocations onto the screen.
Specifying the optional ­`output-allocations` flag outputs the allocations to the specified text file. This flag defaults to a `allocations.txt` file in the current directory.
- `python allocator.py print_room <room_name>` - Prints the names of all the people in room_name on the screen.
- `python allocator.py --version`- Prints the version and exits
