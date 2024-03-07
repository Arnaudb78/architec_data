list_with_tuples = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (10, 11, 12),
    (13, 14, 15, 67, 89, 90),
    ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'),
    ('k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'),
    ('u', 'v', 'w', 'x', 'y', 'z')
]


def find_largest_tuple(list_with_tuples):
    if not list_with_tuples:
        return None

    largest_tuple = max(list_with_tuples, key=len)
    return largest_tuple
