import numpy as np
from loader import DataLoader

with open('tempanomaly.csv', 'r') as file:
    blocks = file.read().strip().split('\n\n')  
    arrays = []
    for block in blocks:
        lines = block.strip().split('\n')  
        data = [list(line.split(',')) for line in lines] 
        arrays.append(np.array(data))  


arrays = arrays[-26:]
data_string = ""


for i in range(len(arrays)):
    for j in range(90):
        
        data_string += ",".join( arrays[i][j]) + "\n"
    data_string += "\n"


with open("prediction_data.csv", "w") as file:
    file.write(data_string[:-2])





