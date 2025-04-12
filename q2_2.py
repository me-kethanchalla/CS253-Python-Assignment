import statistics

def analyze_temperatures(temperatures):

    mean = 0
    median =0
    variance = 0
    std_dev = 0
    
    if len(temperatures) == 1:
        mean = temperatures[0]
        median = temperatures[0]

    else:
        mean = statistics.mean(temperatures)
        median = statistics.median(temperatures)
        std_dev = statistics.stdev(temperatures)
        variance = statistics.variance(temperatures)

    print("Mean Temperature:", mean)
    print("Median Temperature:", median)
    print("Standard Deviation:", std_dev)
    print("Variance:", variance)
    




if __name__ == "__main__":
    temperatures_1 = [30, 32, 31, 29.5, 32.5, 31, 31]
    analyze_temperatures(temperatures_1)


