def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    for _ in range(3):
        top_three.append(max(scores))
        scores.remove(max(scores))
        if len(scores) == 0:
            break
    return top_three
        
def ordered(scores):
    scores.sort()
    return scores

