import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import ast
lst_coord = []
lst_coo1 = []
lst_lat = []
lst_long = []
sns.set(style='whitegrid', palette='pastel', color_codes=True) 
sns.mpl.rc('figure', figsize=(10,6))

shp_path = '/home/thapsat/Downloads/Gas_Detection/MAIN_AREA.shp'

sf = shp.Reader(shp_path)
map = gpd.read_file('/home/thapsat/Downloads/Gas_Detection/MAIN_AREA.shp')
map.to_csv("/home/thapsat/Downloads/Gas_Detection/Map.csv",index = False)
geodata = pd.read_csv("/home/thapsat/Downloads/Gas_Detection/Map.csv")
coord = geodata.iloc[:,0].values
coord  = str(coord).replace('POLYGON',' ')

coord  = str(coord).replace('Z',' ')
coord  = str(coord).replace("'"," ")
coord  = str(coord).replace(","," ")
coord  = str(coord).replace("("," ")
coord  = str(coord).replace(")"," ")
coord  = str(coord).replace("["," ")
coord  = str(coord).replace("]"," ")

ww = 0
e = 1


coord = coord.lstrip()
coord = coord.rstrip()
coord = coord.strip()

print(coord)
lst_coord.append(coord)
print(lst_coord)
df_coo = pd.DataFrame(lst_coord)
print(df_coo.values)
for i in df_coo.values:
	for j in i:
		print(j)
		lst_coo1.append(j)
		coo_df = pd.DataFrame(lst_coo1)
		coo_df.columns = ['VECTOR']
		coo_df1 = coo_df.VECTOR.str.split(expand= True)
		#coo_arr = np.array(coo_df1)
		#print(coo_arr)
		val = coo_df1.values
		val = val.tolist()
		print(val)
		for oo in val:
			print(len(oo))
			for w in range(0,100): 

				longitudes = oo[ww]
				ww+=3
				lst_long.append(longitudes)
				print(len(lst_long))

				print(longitudes)
				latitudes = oo[e]
				lst_lat.append(latitudes)

				e+=3
				print(latitudes)
plt.title("MAP")
plt.xlabel("latitudes")
plt.ylabel("longitudes")
plt.plot(lst_lat,lst_long)
Gas_Detection_Data = pd.read_csv("/home/thapsat/Downloads/Gas_Detection/Gas_Data.csv")
Area1 = Gas_Detection_Data.iloc[1:2,3:]
Area2 = Gas_Detection_Data.iloc[2:3,3:]
Area3 = Gas_Detection_Data.iloc[3:4,3:]
Area4 = Gas_Detection_Data.iloc[4:5,3:]
Area5 = Gas_Detection_Data.iloc[5:6,3:]
Area6 = Gas_Detection_Data.iloc[6:7,3:]
Area7 = Gas_Detection_Data.iloc[7: ,3:]
print(Area1)
A1 = np.array(Area1)
print(A1[0])


plt.savefig('MAP.png')
plt.show()



















