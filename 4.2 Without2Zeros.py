def No_2Zero(N, K):
    P0 = 0
    P1 = K - 1
    P = K - 1
    #print("P0 = ", P0, "; P1 = ", P1, "; P = ", P)
    for i in range(2, N + 1):
        P0 = P1
        P1 = P * (K - 1)
        P = P0 + P1
        #print("i = ", i, "; P0 = ", P0, "; P1 = ", P1, "; P = ", P)
    return P


#print(No_2Zero(6, 3))
