from collections import defaultdict

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    if len(weights) <= 1:
        return None

    weight_to_ix = defaultdict(lambda: [])
    for ix, w in enumerate(weights):
        weight_to_ix[w].append(ix)

    for w in weights:
        if limit-w in weight_to_ix:
            if limit-w == w and len(weight_to_ix[w]) >= 2:
                return (weight_to_ix[w][1], weight_to_ix[w][0])
            elif limit-w != w:
                return (weight_to_ix[limit-w][0], weight_to_ix[w][0])

    return None
