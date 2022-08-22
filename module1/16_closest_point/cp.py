from point import Point
import math


def calculate_distance(s, p):
    return math.sqrt((p.x - s.x)**2 + (p.y - s.y)**2)


def closestPoint(s, p):
    distance_list = []
    point_list = list(s)
    min_dist_points = set()

    if (len(s) == 0):
        return min_dist_points

    for i in s:
        distance = calculate_distance(i, p)
        distance_list.append(distance)

    min_distance = min(distance_list)

    for i in range(len(distance_list)):
        if distance_list[i] == min_distance:
            min_dist_points.add(point_list[i])

    return min_dist_points