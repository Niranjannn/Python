#Group 12: Niranjan Naik, Anurag Patil, Dhaval Metre
#3.3 Code to plot the scatter matrix and describe() function results
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix
dataframe=pd.read_csv(r'data.tsv',sep='\t', index_col=0)

dataframe.head()
#finding the count/mean/std/min/25%/50%75%
dataframe.describe()
print(dataframe.describe().transpose())
#scatter_matrix() method to find pairs of variables with high correlation

plt.style.use('ggplot')
scatter_matrix(dataframe,figsize=(10,10))
plt.show()
#calculate the Pearon’s correlation coefficients.
print np.corrcoef(dataframe)
#create time series graphs for each of the 11 variables
dataframe.plot()
plt.show()



