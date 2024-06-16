import numpy as np
import matplotlib.pyplot as plt

class DataLoader:

    def __init__(self,file_path = 'tempanomaly.csv'):
        data = self.load_csv_blocks(file_path)
        if file_path == 'tempanomaly.csv':
            
            min = np.min(data)
            max = np.max(data)
            
        
            f = open("scaling_factor.txt", "w")
            f.write(str(min)+'\n'+str(max))
            f.close()
        else:
            with open("scaling_factor.txt", "r") as f:
                max = float(f.readline())
                min = float(f.readline())
        self.data = 2*(data-min)/(max-min)-1

    def replace_nulls_with_mean(self, arr):
       
        np_arr = np.array(arr, dtype=float)
        mean_value = np.nanmean(np_arr)
        np_arr[np.isnan(np_arr)] = mean_value
        
        return np_arr
    def load_csv_blocks(self, filename):
        with open(filename, 'r') as file:
            blocks = file.read().strip().split('\n\n')  
            arrays = []
            for block in blocks:
                lines = block.strip().split('\n')  
                data = [list(map(float, line.split(','))) for line in lines] 
                arrays.append(self.replace_nulls_with_mean(np.array(data)))  

            return np.array(arrays)
    def load_data(self, batch_size = 12):
        batched_data = []
        next_months = []
        for i in range(len(self.data) - batch_size):
            end = i+batch_size
            batched_data.append(self.data[i:end])
            next_months.append( self.data[end])

        return np.array(batched_data), np.array(next_months)
        

        
        
        
if __name__ == "__main__":
    dl = DataLoader()
    X, y =dl.load_data()

    toPlot = y[-1]
    print(y[-1].shape)
    plt.figure(figsize=(12, 6))
    plt.imshow(toPlot, cmap='coolwarm', aspect='auto', origin='lower')
    plt.colorbar(label='Temperature Anomaly')
    plt.title('First Month Temperature Anomaly')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.xticks(np.linspace(0, 179, 6), labels=np.linspace(-180, 180, 6))
    plt.yticks(np.linspace(0, 89, 5), labels=np.linspace(-90, 90, 5))
    plt.show()

