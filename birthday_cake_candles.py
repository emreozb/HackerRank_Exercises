def birthdayCakeCandles(candles):
    counter = 0
    max_h = max(candles)
    for c in candles:
        if c == max_h:
            counter += 1
    return counter

candles = [2,21,53,12,12,12,3,2,53]
print(birthdayCakeCandles(candles))