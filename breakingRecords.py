def breakingRecords(scores):
    s_min = 0
    s_max = 0
    s_min = scores[0]
    s_max = scores[0]

    count_min = 0
    count_max = 0
    for score in scores[1:]:
        if score > s_max:
            s_max = score
            count_max += 1 
        if score < s_min:
            s_min = score
            count_min += 1
    return count_max, count_min

scores = [3,4,21,36,10,28,35,5,24,42]
print(breakingRecords(scores))


