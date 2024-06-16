import numpy as np
from keras import saving
from loader import DataLoader
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
rok =2050

model = saving.load_model("model.keras")
batch_len = 25 ##musi byc taki sam jak w train.py

datapath = "prediction_data.csv"
#datapath = "tempanomaly.csv"
dl = DataLoader(datapath)

X, y = dl.load_data(batch_len)

current_input = X[-1].reshape(1, batch_len, 90, 180, 1)  
future_predictions = []

for _ in range((2050-2025)*12+7):
   
    next_prediction = model.predict(current_input)
    
    
    future_predictions.append(next_prediction)
    
    next_prediction = next_prediction.reshape(1,1,90,180,1)
    current_input = np.append(current_input[:, 1:, :, :, :], next_prediction, axis=1)


data = np.array(future_predictions)
with open("scaling_factor.txt", "r") as f:
    max = float(f.readline())
    min = float(f.readline())

data = np.array(data)+1
data/=2
data*=(max-min)
data+=min

n = len(data)
res = np.squeeze(data[-12:])

print("Ocieplenie(wzgledem sredniej z 1951-1980) dla roku: "+str(rok)+", "+str(np.average(res))+" stopni C")
yearly_avg = np.mean(res,axis=0)
print(yearly_avg.shape)

fig = plt.figure(figsize=(12, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

ax.set_extent([-180, 180, -90, 90], crs=ccrs.PlateCarree())
ax.coastlines()

latitudes = np.linspace(-90, 90, yearly_avg.shape[0])
longitudes = np.linspace(-180, 180, yearly_avg.shape[1])
lon, lat = np.meshgrid(longitudes, latitudes)

mesh = ax.pcolormesh(lon, lat, yearly_avg, transform=ccrs.PlateCarree(), cmap='viridis')

plt.colorbar(mesh, ax=ax, orientation='horizontal', pad=0.05, label='Ocieplenie względem średniej obszarowej z lat 1951-1980 dla roku: '+str(rok))
ax.gridlines(draw_labels=True)


plt.show()