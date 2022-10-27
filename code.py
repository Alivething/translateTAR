n = 4
tag = [2, 2, 2, 2] 
que = [[1, 4]]

pairs = []
for q in que:
    pair = 0
    for j in range(n):
        if j == q[0]-1:
            continue
        if tag[q[0]-1] == tag[j]:
            pair+=1

    pairs.append(pair)
    
print(pairs)