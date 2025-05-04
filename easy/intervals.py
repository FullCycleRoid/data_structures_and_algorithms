def non_intersection_intervals(intervals: list[tuple]) -> list[tuple]:
    start_pair = intervals[0]
    non_intersect_intervals = [start_pair]

    current_position = 0
    next_position = 1

    while next_position < len(intervals):
        current_pair = intervals[current_position]
        next_pair = intervals[next_position]

        if current_pair[1] <= next_pair[0]:
            non_intersect_intervals.append(next_pair)
            current_position = next_position
            next_position += 1

        if current_pair[1] > next_pair[0]:
            next_position += 1

    return non_intersect_intervals

if __name__ == "__main__":
    many_intervals = [
        [(1, 4), (3, 6), (5, 8), (7, 10)],
        [(1, 10), (2, 5), (6, 8), (12, 15)],
        [(1, 2), (4, 5), (7, 9)],
    ]

    for interval in many_intervals:
        result = non_intersection_intervals(interval)
        print(result)


