
import pandas as pd
"""np.array([50,125,140,10,50,1125,-55])

type(A)
numpy.nparray"""

"""np.array(["Elif",50,125,140])
array(['elif','50','125','140'], dtype='<U11')"""

"""a = np.arange(20)
np.sqrt(2)"""

"""a = pd.Series([2,3,5,7,11,13,17,19],
index=np.arange(8), dtype=np.dtype(int))
a.index
a.values"""

df= pd.DataFrame(columns= ["takmaAD", "cins", "renk"])
df= pd.concat([df, pd.DataFrame([{"takmaAd": "Safyüz", "cins": "norveç orman", "renk": "sarı-beyaz"}])],
ignore_index=True)
df

