#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # avoid potential headaches for small input size
    if len(tickets) == 0:
        return []

    if len(tickets) == 1:
        return [tickets[0].source]

    # construct a dict of source-to-destinations
    s2d = {}
    for ticket in tickets:
        s2d[ticket.source] = ticket.destination

    # first is labeled "NONE"
    source = s2d["NONE"]

    # final will be labeled "NONE" for dest
    route = []
    while source != "NONE":
        route.append(source)
        source = s2d[source]
    route.append(source)

    return route
