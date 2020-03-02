from csp import CSP, parse_neighbors

def CourseScheduler():
    """Return an example of constraint satisfaction for course scheduling"""
    Faculty = 'VanderLinden Norman Adams Plantinga'.split()
    Rooms = 'NH253 SB382'.split()
    Times = 'MWF900 MWF1200 MWF300 TTH1030 TTH1200'.split()
    variables = 'CS108 CS112 CS212 CS214 CS232 CS262'.split()

    # Course/Prof assignments for pruning domain before constraints
    assignments = [('CS108', 'VanderLinden'), ('CS112', 'Norman'), \
                  ('CS212', 'Plantinga'), ('CS214', 'Adams'), \
                  ('CS232', 'Norman'), ('CS262', 'VanderLinden')]

    # Create all possible domain values for each variable (course)
    # arrangement is always tuples of prof, time, and room
    domains = {}
    for course in variables:
        # Create a list for each course in the domains
        domains[course] = []
        for prof in Faculty:
            for a in assignments:
                # Only add if course and prof are assigned
                if a[0] == course and a[1] == prof:
                    for time in Times:
                        for room in Rooms:
                            domains[course.append((prof, time, room))]

    # Make sure each course is a neighbor
    neighbors = parse_neighbors("""CS108: CS112 CS212 CS214 CS232 CS262;
                CS112: CS212 CS214 CS232 CS262;
                CS212: CS214 CS232 CS262;
                CS214: CS232 CS262;
                CS232: CS262""", variables)

    def course_constraints(A, a, B, b):
        """Defines constraints for scheduling with variable courses A and B
        and their respective values a and b
        Returns true only if none of the constraints are violated"""

        # Is the course offered more than once?
        if A == B:
            return False
        # Is the teacher assigned twice to one time?
        elif a[0] == b[0] and a[1] == b[1]:
            return False
        # Is the room double-booked?
        elif a[1] == b[1] and a[2] == b[2]:
            return False
        # Else, constraints are satisfied
        else:
            return True
    return CSP(variables, domains, neighbors, course_constraints)

import time
from csp import AC3, min_conflicts, backtracking_search
from search import depth_first_graph_search

scheduler = CourseScheduler()

time1 = time.time()
result = backtracking_search(scheduler)
time2 = time.time()

if scheduler.goal_test(scheduler.infer_assignment()):
    print("Solution:\n")
    print(result)
    print("\nTime: " + str(time2 - time1))
else:
    print("failed...")
    print(scheduler.curr_domains)
    scheduler.display(scheduler.infer_assignment())
