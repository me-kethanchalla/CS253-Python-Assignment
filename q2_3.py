import numpy as np

def solve_linear_system(A, B) :

    #convert into numpy arrays to use shape function 
    A = np.array(A, dtype=float)
    B = np.array(B, dtype=float)

    rows_A = A.shape[0]
    cols_A = A.shape[1]
    rows_B = B.shape[0]
    cols_B = len(B.shape)

    if rows_A != cols_A :
        raise ValueError("Matrix A should be a squared matrix")
    
    elif rows_A != rows_B :
        raise ValueError("Number of rows is both Matrices should be same.")
    
    elif cols_B != 1 :
        raise ValueError("Matrix B should be a column matrix (1 columned only)")

    else :
        X = np.linalg.solve(A,B)
    return X




if __name__ == "__main__":
    A = [[1, 2], [2, 1]]
    B = [5, 5]
    try:
        solution = solve_linear_system(A, B)
        print("Solution X:", solution)
    except ValueError as e:
        print("Error:", e)