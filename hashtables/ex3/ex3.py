from collections import defaultdict

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # construct dictionary of numbers to count
    n2c = defaultdict(lambda: 0)

    for array in arrays:
        for n in array:
            n2c[n] += 1

    result = [k for k, v in n2c.items() if v == len(arrays)]

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
