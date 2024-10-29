import datetime

class Booking:
    # constructor
    def __init__(self, room, start, hours, title, contact):
        self.room = room
        self.start = start
        self.hours = hours
        self.title = title
        self.contact = contact

    # getters
    def get_room(self):
        return self.room

    def get_start(self):
        return self.start

    def get_hours(self):
        return self.hours

    def get_title(self):
        return self.title

    def get_contact(self):
        return self.contact


    def __str__(self):
        return (f"Room {self.room} booked on {self.start} for {self.hours} hours by {self.title} ({self.contact}).")

    def __repr__(self):
        return f"Booking({self.room}, {self.start}, {self.hours}, {self.title}, {self.contact})"

    def __hash__(self):
        return hash(self)

    def __eq__(self, other):
        # print equality check
        print("Checking for equal values")
        # return false if 'other' is not a Booking object
        if not isinstance(other, Booking):
            return False
        # return results of equality check
        else:
            return hash(self) == hash(other)

    def overlaps_with(self, other):
        if self.start.date == other.start.date:
            try:
                return (self.start.time.hour + self.hours > other.start.time.hour or other.start.time.hour +
                        other.hours > self.start.time.hour)
            except ValueError:
                return (self.start.time.hour + (self.hours - 24) > other.start.time.hour or other.start.time.hour +
                        (other.hours - 24) > self.start.time.hour)