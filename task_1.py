import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv(r"C:\Users\satya\OneDrive\Desktop\inten\API_SP.POP.TOTL_DS2_en_csv_v2_85220.csv",skiprows=4)
print(df.head(5))
print(df.isnull().sum())

