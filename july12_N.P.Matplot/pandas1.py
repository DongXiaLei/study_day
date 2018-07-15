import numpy as np
import pandas as pd
import tensorflow
import keras


df = pd.DataFrame(np.arange(12).reshape((3,4)),index=list(range(3,6)),columns=list(range(1,5)))
print(df.dtypes)
print(df.index,df.columns)
print(df.sort_index(axis=1,ascending=False))
