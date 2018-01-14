from scipy.io import arff
import pandas as pd

data = arff.loadarff('trainingsdaten.arff')
df = pd.DataFrame(data[0])

print (type(df))
print (df.shape)
print (df)

print ()

# We'll try to predict 'Bewertung' ('evaluation') for test case 1 now:
# p_pl_rmhn = P(plus|regnerisch, mittel, hoch, nein)
# p_pl_rmhn = P(+) · P(regnerisch|+) · P(mittel|+) · P(hoch|+) · P(nein|+) · alpha
# p_pl_rmhn = p_pl * p_r_pl * p_m_pl * p_h_pl * p_n_pl * alpha

# Rename headers of given Dataframe object
df.columns = ('a','b','c','d','e')
# Record headers of the given Dataframe object in a list
headers_list = list(df.columns.values)
print (headers_list)

"""
# Convert the columns of the given Dataframe separately to Series objects
header_0_column = df.filter(items=[headers_list[0]])
header_1_column = df.filter(items=[headers_list[1]])
header_2_column = df.filter(items=[headers_list[2]])
header_3_column = df.filter(items=[headers_list[3]])
header_4_column = df.filter(items=[headers_list[4]])
"""

# Create Series objects that count the occurences of the different value categories, dependent on "+"
#   Record how many items are in df in total (needed for later probabilities calculation)
df_count = list(df.count(axis=0))[0]
#   First, filter df so that only "+" persists in df_plus
df_plus = df[df.e == b'"+"']
df_minus = df[df.e == b'"-"']
print ("df_plus: ",df_plus)

# For creating p_pl and p_mi, we need the numbers of "+" and "-" in the original df table
pl_counts_df = df_plus[headers_list[4]].value_counts()
pl_counts = pl_counts_df[0]
mi_counts_df = df_minus[headers_list[4]].value_counts()
mi_counts = mi_counts_df[0]
print ("pl_counts: ", pl_counts)
print ("mi_counts: ", mi_counts)

# For creating the counts underlying p_r_pl, p_m_pl, p_h_pl, p_n_pl
# and p_r_mi, p_m_mi, p_h_mi, p_n_mi
# we need to further filter df_plus and df_minus.
# Column headers translation:
# 'a': "Bewoelkung"
# 'b': "Temperatur"
# 'c': "Feuchtigkeit"
# 'd': "Wind"
# 'e': "Bewertung"

# Creating counts for p_r_pl and p_r_mi:
df_plus_r = df_plus[df_plus.a == b'"regnerisch"']
df_minus_r = df_minus[df_minus.a == b'"regnerisch"']
print ("df_plus_r: ",df_plus_r)
print ("df_minus_r: ",df_minus_r)
try:
    pl_r_counts_df = df_plus_r[headers_list[0]].value_counts()
    pl_r_counts = pl_r_counts_df[0]
except IndexError:
    # print ("IndexError with pl_r_counts")
    pl_r_counts = 0
try:
    mi_r_counts_df = df_minus_r[headers_list[0]].value_counts()
    mi_r_counts = mi_r_counts_df[0]
except IndexError:
    # print ("IndexError with mi_r_counts")
    mi_r_counts = 0
print ("pl_r_counts: ", pl_r_counts)
print ("mi_r_counts: ", mi_r_counts)

# Creating counts for p_m_pl and p_m_mi:
df_plus_m = df_plus[df_plus.b == b'"mittel"']
df_minus_m = df_minus[df_minus.b == b'"mittel"']
print ("df_plus_m: ",df_plus_m)
print ("df_minus_m: ",df_minus_m)
try:
    pl_m_counts_df = df_plus_m[headers_list[1]].value_counts()
    pl_m_counts = pl_m_counts_df[0]
except IndexError:
    # print ("IndexError with pl_m_counts")
    pl_m_counts = 0
try:
    mi_m_counts_df = df_minus_m[headers_list[1]].value_counts()
    mi_m_counts = mi_m_counts_df[0]
except IndexError:
    # print ("IndexError with mi_m_counts")
    mi_m_counts = 0
print ("pl_m_counts: ", pl_m_counts)
print ("mi_m_counts: ", mi_m_counts)

# Creating counts for p_h_pl and p_h_mi:
df_plus_h = df_plus[df_plus.c == b'"hoch"']
df_minus_h = df_minus[df_minus.c == b'"hoch"']
print ("df_plus_h: ",df_plus_h)
print ("df_minus_h: ",df_minus_h)
try:
    pl_h_counts_df = df_plus_h[headers_list[2]].value_counts()
    pl_h_counts = pl_h_counts_df[0]
except IndexError:
    # print ("IndexError with pl_h_counts")
    pl_h_counts = 0
try:
    mi_h_counts_df = df_minus_h[headers_list[2]].value_counts()
    mi_h_counts = mi_h_counts_df[0]
except IndexError:
    # print ("IndexError with mi_h_counts")
    mi_h_counts = 0
print ("pl_h_counts: ", pl_h_counts)
print ("mi_h_counts: ", mi_h_counts)

# Creating counts for p_n_pl and p_n_mi:
df_plus_n = df_plus[df_plus.d == b'"nein"']
df_minus_n = df_minus[df_minus.d == b'"nein"']
print ("df_plus_n: ",df_plus_n)
print ("df_minus_n: ",df_minus_n)
try:
    pl_n_counts_df = df_plus_n[headers_list[3]].value_counts()
    pl_n_counts = pl_n_counts_df[0]
except IndexError:
    # print ("IndexError with pl_n_counts")
    pl_n_counts = 0
try:
    mi_n_counts_df = df_minus_n[headers_list[3]].value_counts()
    mi_n_counts = mi_n_counts_df[0]
except IndexError:
    # print ("IndexError with mi_n_counts")
    mi_n_counts = 0
print ("pl_n_counts: ", pl_n_counts)
print ("mi_n_counts: ", mi_n_counts)

# Calculate p_pl and p_mi
p_pl = pl_counts/(pl_counts + mi_counts)
p_mi = mi_counts/(pl_counts + mi_counts)
print ("p_pl: ", p_pl)
print ("p_mi: ", p_mi)

# Calculate p_r_pl, p_m_pl, p_h_pl, p_n_pl
# and p_r_mi, p_m_mi, p_h_mi, p_n_mi:
p_r_pl = pl_r_counts/pl_counts
p_r_mi = mi_r_counts/mi_counts
p_m_pl = pl_m_counts/pl_counts
p_m_mi = mi_m_counts/mi_counts
p_h_pl = pl_h_counts/pl_counts
p_h_mi = mi_h_counts/mi_counts
p_n_pl = pl_n_counts/pl_counts
p_n_mi = mi_n_counts/mi_counts
print ("p_r_pl: ", p_r_pl)
print ("p_r_mi: ", p_r_mi)
print ("p_m_pl: ", p_m_pl)
print ("p_m_mi: ", p_m_mi)
print ("p_h_pl: ", p_h_pl)
print ("p_h_mi: ", p_h_mi)
print ("p_n_pl: ", p_n_pl)
print ("p_n_mi: ", p_n_mi)

# Calculate p_pl_rmhn = P(plus|regnerisch, mittel, hoch, nein):
p_pl_rmhn = p_pl * p_r_pl * p_m_pl * p_h_pl * p_n_pl
p_mi_rmhn = p_mi * p_r_mi * p_m_mi * p_h_mi * p_n_mi
print ("p_pl_rmhn: ", p_pl_rmhn)
print ("p_mi_rmhn: ", p_mi_rmhn)

# Calculate alpha value:
alpha = 1/(p_pl_rmhn + p_mi_rmhn)
print ("alpha: ", alpha)

# Calculate p_pl_rmhn = P(plus|regnerisch, mittel, hoch, nein)
# WITH alpha value:
p_pl_rmhn_alpha = p_pl_rmhn * alpha
p_mi_rmhn_alpha = p_mi_rmhn * alpha
print ("p_pl_rmhn_alpha: ", p_pl_rmhn_alpha)
print ("p_mi_rmhn_alpha: ", p_mi_rmhn_alpha)

"""

# prepare values from the filtered tables df_plus and df_minus
header_0_counts_plus = df_plus[headers_list[0]].value_counts()
header_1_counts_plus = df_plus[headers_list[1]].value_counts()
header_2_counts_plus = df_plus[headers_list[2]].value_counts()
header_3_counts_plus = df_plus[headers_list[3]].value_counts()
header_4_counts_plus = df_plus[headers_list[4]].value_counts()

header_0_counts_minus = df_minus[headers_list[0]].value_counts()
header_1_counts_minus = df_minus[headers_list[1]].value_counts()
header_2_counts_minus = df_minus[headers_list[2]].value_counts()
header_3_counts_minus = df_minus[headers_list[3]].value_counts()
header_4_counts_minus = df_minus[headers_list[4]].value_counts()


### print ("type(header_1_counts_plus): ", type(header_4_counts_plus))
#.sum(axis=None


header_2_counts = df[headers_list[2]].value_counts()
header_3_counts = df[headers_list[3]].value_counts()
header_4_counts = df[headers_list[4]].value_counts()
### print (header_0_counts)
header_0_counts_indices = list(header_0_counts.index)


### print ("header_0_counts_minus: ",header_0_counts_minus)
# Let's create the counts specifically for the weather case
p_pl = header_4_counts[1]/(header_4_counts[0]+header_4_counts[1])
# index_regnerisch = header_0_counts_plus[header_0_counts_plus == b'"regnerisch"'].index[0]
# index_0_regnerisch_plus = pd.Index(header_0_counts_plus).get_loc(b'"regnerisch"')
# index_0_regnerisch_minus = pd.Index(header_0_counts_minus).get_loc(b'"regnerisch"')
##### PROBLEM
index_0_regnerisch_minus = header_0_counts_minus[header_0_counts_minus == b'"regnerisch"'].index[0]
### print (index_0_regnerisch_minus)
p_r_pl = header_0_counts_plus[index_regnerisch] / (header_0_counts_plus.sum(axis=None))
### print ()
### print (header_1_counts[1])
### print (p_pl)
#header_4_counts_indices = list(header_4_counts.index)
#header_4_counts_indices = header_4_counts_indices[1]
#### print (header_4_counts_indices)
# header_4_counts_pluses = header_4_counts.loc[lambda x: x == header_4_counts_indices[1]]
#header_4_counts_pluses = header_4_counts[header_4_counts == b'"+"']
# ### print (header_4_counts_pluses)

# print(df.groupby(['Bewertung','Temperatur'])['Bewertung'].count())
# ### print (df[headers_list[4]].value_count())

# ### print (df.head())

"""

print ()