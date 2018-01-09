from scipy.io import arff
import pandas as pd

data = arff.loadarff('trainingsdaten.arff')
df = pd.DataFrame(data[0])

df.head()
