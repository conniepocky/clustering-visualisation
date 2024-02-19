import numpy
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def visualise_clusters(dataset, c_num, colours, name):
    for i in range(0, c_num):
        plt.scatter(dataset["x"][dataset["color"] == i], 
                dataset["y"][dataset["color"] == i], s = 100, 
                c = colours[i], label = f"Cluster {i+1}")   

    plt.title(f"{name}")  
    plt.xlabel("X")  
    plt.ylabel("Y")  
    plt.legend()  
    plt.show()

face = pd.read_csv("data/face.csv")

visualise_clusters(face, 4, ["red", "pink", "blue", "yellow"], "Face")
