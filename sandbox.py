G = ['7283455864',
     '6731158619',
     '8988242643',
     '3830589324',
     '1239503950',
     '5633845374',
     '6473530293']

P = ['3950',
     '5374',
     '0293']


def findIndex(strin, smallstrin):
    arr = []
    for i in len(strin):
        if strin[i] == smallstrin[0]:
            if strin[i] == P[0]:
                arr.append(i)

smallLen = len(P[0])
indecies = []
row = len(G)
for i in range(len(G)):
    if P[0] not in G[i]:
        if i <= len(G):
            continue
        else:
            # print("NO")
            break
    else:
        row = i
        splitted = findIndex(G[i], smallLen)
        for ind in range(len(splitted)):
            if splitted[ind] == P[0]:
                if ind == 0:
                    indecies.append(0)
                else:
                    indecies.append(ind * smallLen)
        break
        # todo iterate trhough remaining elems in G, if another elems from P have index as first elemhhhjkjkkj

# print(row, indecies)
prints = []
if len(P) - 1 >= len(G) - row:
    print("NO")
else:
    i = 1
    for inde in indecies:
        while i < len(P):
            if P[i] in G[row + i]:
                if G[row + i].index(P[i]) != inde:
                    prints.append("NO")
                    break
                else:
                    if i == len(P) - 1:
                        prints.append("YES")
                        break
                    i += 1
            else:
                prints.append("NO")
                break
# print(prints)
    if "YES" in prints:
        print("YES")
    else:
        print("NO")
