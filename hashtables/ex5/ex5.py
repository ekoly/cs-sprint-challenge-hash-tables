# Your code here
from collections import defaultdict

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # construct a dict of filenames to paths
    filed = defaultdict(lambda: [])
    for file in files:
        filed[file.split("/")[-1]].append(file)

    # determine if each query is in the dict
    result = []
    for query in queries:
        if query in filed:
            result.extend(filed[query])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
