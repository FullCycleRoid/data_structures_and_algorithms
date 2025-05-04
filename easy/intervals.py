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

# if __name__ == "__main__":
#     many_intervals = [
#         [(1, 4), (3, 6), (5, 8), (7, 10)],
#         [(1, 10), (2, 5), (6, 8), (12, 15)],
#         [(1, 2), (4, 5), (7, 9)],
#     ]
#
#     for interval in many_intervals:
#         result = non_intersection_intervals(interval)
#         print(result)


def extended_intervals(intervals: list[tuple]) -> list[tuple]:
    start_pair = intervals[0]
    result = [start_pair]

    is_refreshed = False
    left_position = 0
    right_position = 1

    while right_position <= len(intervals) - 1:
        if not is_refreshed:
            left_pair = list(intervals[left_position])

        right_pair = list(intervals[right_position])
        if left_pair[1] < right_pair[0]:
            result.append(tuple(right_pair))
            left_position = right_position
            is_refreshed = False

        if left_pair[1] > right_pair[0] and left_pair[1] < right_pair[1]:
            left_pair[1] = right_pair[1]
            result[left_position] = tuple(left_pair)

            is_refreshed = True

        right_position += 1

    return result

if __name__ == "__main__":
    many_intervals = [
        [(1, 4), (3, 6), (5, 8), (7, 10)],
        [(1, 10), (2, 5), (6, 8), (12, 15)],
        [(1, 2), (4, 5), (7, 9)],
        [(1, 5), (3, 7), (7, 9)],
    ]

    for interval in many_intervals:
        result = extended_intervals(interval)
        print(result)


