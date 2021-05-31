def minmax(data):
    terkecil = terbesar = data[0]
    for i in data:
        if terkecil > i:
            terkecil = i
        if terbesar < i:
            terbesar = i
    return (terkecil, terbesar)


print(minmax([1,5,10]))
