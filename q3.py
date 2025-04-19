import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': np.tan,
    'log': lambda x: np.log(x), # this lambda format is for initialising a small function within here.
    'square': lambda x: x**2,
    'cube': lambda x: x**3
}

def set_random_seed(seed) :
    np.random.seed(seed)

def generate_dataset(N, x_min, x_max):
    
    func_keys = list(functions.keys())
    if x_min < 0:
        # Exclude log if your X is negative
        if 'log' in func_keys : 
            func_keys.remove('log')

    
    chosen = np.random.choice(func_keys, size=3, replace=True)
    X = np.random.uniform(low=x_min, high=x_max, size=N)

    A, B, C, D, E, F = np.random.rand(6) #any 6 random values

    Y = (
        A * functions[chosen[0]](B * X) +
        C * functions[chosen[1]](D * X) +
        E * functions[chosen[2]](F * X)
    )

    print("Randomly Chosen Functions are:" ,chosen[0] , chosen[1] , chosen[2] )

    return X.tolist(), Y.tolist()



def plot_scatter(X, Y) :
    plt.figure(figsize=(8,6))
    plt.scatter(X, Y , color='blue', label='Generated Data' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter Plot")
    plt.legend()
    plt.show()


def plot_histogram(X): 
    plt.figure(figsize=(8,6))
    plt.hist(X, bins='auto', color='red', label='Data')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Histogram")
    plt.legend()
    plt.show()

def box_plot(Y) :
    plt.figure(figsize=(8,6))
    plt.boxplot(Y, label='Y values')
    plt.title("Box Plot")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

def line_plot(X,Y) :
        
    df = pd.DataFrame({'X': X, 'Y': Y})
    df_sorted = df.sort_values('X')
    X_sorted = df_sorted['X'].values
    Y_sorted = df_sorted['Y'].values

    plt.figure(figsize=(8,6))
    plt.plot(X_sorted, Y_sorted, color= 'green', label='Sorted Generated Data')
    plt.title("Line Plot")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()



if __name__ == "__main__":

    set_random_seed(42) # this will make sure that everytime the same 3 functions are selected
    # if different functions set needed, we can either change or remove this feature. 

    N = input("Enter number of data points: ")
    N = int(N)

    x_min = input("Enter min X :")  
    x_min = float(x_min)
    x_max = input("Enter max X :")
    x_max = float(x_max)
    if (x_min >= x_max) : 
        raise ValueError("Minimum of x should be less than maximum of x ")
    X, Y = generate_dataset(N, x_min, x_max)
    plot_scatter(X, Y)
    plot_histogram(X)
    box_plot(Y)
    line_plot(X, Y)
