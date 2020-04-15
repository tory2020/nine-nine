a = list(map(lambda x : x[1],filter(lambda x : x[0],[(i*100+j*10+k == i**3+j**3+k**3, i**3+j**3+k**3) for i in range(1, 10) for j in range(0, 10) for k in range(0, 10)])))

print(a)
