def odd_squares_sum(a):
    return sum(x*x for x in range(1,a) if x%2==1)


print(odd_squares_sum(6))
