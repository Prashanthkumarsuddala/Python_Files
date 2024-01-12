import numpy as np

def printMaxSubSquare(M):
    R = len(M)
    C = len(M[0])
    S = np.zeros((R, C), dtype=int)
    max_of_s = 0
    max_i = 0
    max_j = 0

    # Set first column of S[][]
    for i in range(R):
        S[i][0] = M[i][0]

    # Set first row of S[][]
    for j in range(C):
        S[0][j] = M[0][j]

    # Construct other entries of S[][]
    for i in range(1, R):
        for j in range(1, C):
            if M[i][j] == 1:
                S[i][j] = min(S[i][j - 1], S[i - 1][j], S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0

    # Find the maximum entry, and indexes of maximum entry in S[][]
    for i in range(R):
        for j in range(C):
            if max_of_s < S[i][j]:
                max_of_s = S[i][j]
                max_i = i
                max_j = j

    print("Maximum size sub-matrix is:")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j], end=" ")
        print()

# Utility function to get minimum of three values
def min(a, b, c):
    m = a
    if m > b:
        m = b
    if m > c:
        m = c
    return m

# Driver function to test above functions
if __name__ == "__main__":
    M = [[0, 1, 1, 0, 1],
         [1, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1],
         [0, 0, 0, 0, 0]]
    printMaxSubSquare(M)
