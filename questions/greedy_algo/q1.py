"""
Activitivty problem
Find the max number of actitiies a person can perform
given N number of activities with the start and end times
"""


def printMaxActicitives(activities: list[tuple[str, int, int]]):
    max_activities = activities[:1]
    for i in range(1, len(activities)):
        if activities[i][1] > max_activities[-1][2]:
            max_activities.append(activities[i])

    print(max_activities)


activities: list[tuple[str, int, int]] = [
    ("A1", 0, 6),
    ("A2", 3, 4),
    ("A3", 1, 2),
    ("A4", 5, 6),
    ("A5", 5, 7),
    ("A6", 8, 9),
]
sorted_activites = sorted(activities, key=lambda item: item[2])
printMaxActicitives(sorted_activites)
