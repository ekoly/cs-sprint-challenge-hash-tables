def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # construct a dict with the keys being numbers in a
    d = {}
    res = []
    for n in a:
        if -n in d:
            res.append(abs(n))
        d[n] = None

    return res


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
