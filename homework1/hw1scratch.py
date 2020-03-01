from csp import parse_neighbors

def CourseScheduling():
    """Return an example of constraint satisfaction for course scheduling"""
    Faculty = 'VanderLinden Norman Adams Plantinga'.split()
    Rooms = 'NH253 SB382'.split()
    Times = 'MWF900 MWF1200 TTH1030 TTH1200'.split()
    variables = 'CS108 CS112 CS212 CS214 CS232 CS262'.split()

    # Create all possible domain values for each variable (course)
    # arrangement is always tuples of prof, time, and room
    domains = {}
    for course in variables:
        domains[course] = []
        for prof in Faculty:
            for time in Times:
                for room in Rooms:
                    domains[course].append((prof, time, room))

    # Make sure each course is a neighbor
    neighbors = parse_neighbors("""CS108: CS112 CS212 CS214 CS232 CS262
                CS112: CS212 CS214 CS232 CS262
                CS212: CS214 CS232 CS262
                CS214: CS232 CS262
                CS232: CS262""", variables)

    def course_constraints(A, a, B, b):
        """Defines constraints for scheduling with variable courses A and B
        and their respective values a and b
        Returns true only if none of the constraints are violated"""

        # Is the course the same? (cannot be taught more than once)
        if A == B:
            return False
        # Are the assignments correct?
        if (A == 'CS108' and a[0] != 'VanderLinden') or \
           (B == 'CS108' and b[0] != 'VanderLinden'):
            return False
        elif (A == 'CS112' and a[0] != 'Norman') or \
             (B == 'CS112' and b[0] != 'Norman'):
            return False
        elif (A == 'CS212' and a[0] != 'Plantinga') or \
             (A == 'CS212' and b[0] != 'Plantinga'):
            return False
        elif (A == 'CS214' and a[0] != 'Adams') or \
             (B == 'CS214' and b[0] != 'Adams'):
            return False
        elif (A == 'CS232' and a[0] != 'Norman') or \
             (B == 'CS232' and b[0] != 'Norman'):
            return False
        elif (A == 'CS262' and a[0] != 'VanderLinden') or \
             (B == 'CS262' and b[0] != 'VanderLinden'):
            return False
        # are 
