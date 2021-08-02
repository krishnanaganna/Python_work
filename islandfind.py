#if __name__ == '__main__' :
#class solution(object):
A = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
    ]

print(A[0][1])

directions = [(0,1), 
              (0,-1), 
              (-1,0),
              (1,0)]

def valid_direction(A, r, c):
    row = len(A)
    col = len(A[0])
    if r < 0 or c < 0 or r >= row or c >= col:
        return False
    else:
        return True

def dfs(A, r, c):
    A[r][c] = 2
    # Up down left and right 
    for d in directions:
        nr = r +d[0]
        nc = c + d[1]
        if valid_direction(A, nr, nc) and A[nr][nc] == 1:
            dfs(A, nr, nc)


def solution(A):
    print("here")
    if not A:
        print("no data")

    row = len(A)
    col = len(A[0])
    results = 0
    print(results)
    for i in range(row):
        for j in range(col):
            if A[i][j] == 1:
                dfs(A, i, j)
                results +=1
    print(results)
        
            


    



