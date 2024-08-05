from uni import *

class Data():
    def __init__(self):
        # create rooms
        room1 = Room(number="R1", seating_capacity=25)
        room2 = Room(number="R2", seating_capacity=45)
        room3 = Room(number="R3", seating_capacity=35)
        self.rooms = [room1, room2, room3]

        # create meeting times
        meeting_time1 = MeetingTime(id="MT1", time="MWF 09:00 - 10:00")
        meeting_time2 = MeetingTime(id="MT2", time="MWF 10:00 - 11:00")
        meeting_time3 = MeetingTime(id="MT3", time="TTH 09:00 - 10:00")
        meeting_time4 = MeetingTime(id="MT4", time="TTH 10:00 - 11:00")

        self.meeting_times = [
            meeting_time1,
            meeting_time2,
            meeting_time3,
            meeting_time4
        ]

        # creating instructors
        instructor1 = Instructor(id="I1", name="Teacher1")
        instructor2 = Instructor(id="I2", name="Teacher2")
        instructor3 = Instructor(id="I3", name="Teacher3")
        instructor4 = Instructor(id="I4", name="Teacher4")

        self.instructors = [instructor1, instructor2, instructor3, instructor4]

        # create courses
        course1 = Course(number="C1", name="Algorithmics",         max_number_of_students=25, instructors=[instructor1, instructor2])
        course2 = Course(number="C2", name="Software enginnering", max_number_of_students=35, instructors=[instructor1, instructor2, instructor3])
        course3 = Course(number="C3", name="Databases",            max_number_of_students=25, instructors=[instructor1, instructor2])
        course4 = Course(number="C4", name="Python Programming",   max_number_of_students=30, instructors=[instructor3, instructor4])
        course5 = Course(number="C5", name="Machine Learning",     max_number_of_students=35, instructors=[instructor4])
        course6 = Course(number="C6", name="Data Mining",          max_number_of_students=45, instructors=[instructor1, instructor3])
        course7 = Course(number="C7", name="Computer Networks",    max_number_of_students=45, instructors=[instructor2, instructor4])

        self.courses = [course1, course2, course3, course4, course5, course6, course7]

        # create departments
        department1 = Department(name="Computer Science", courses=[course1, course3])
        department2 = Department(name="Applied Comp Sci", courses=[course2, course4, course7])
        department3 = Department(name="Masters",          courses=[course5, course6])

        self.depts = [department1, department2, department3]

        # define the number of classes
        self.number_of_classes = sum([len(x.courses) for x in self.depts])
