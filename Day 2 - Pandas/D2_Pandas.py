import pandas as pd
import numpy as np

# Creating a table
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20,'c':30}

# Making into a data series
print(pd.Series(data=my_data,index=labels))

# Creating a data series in 1 line
ser1 = pd.Series([1,2,3,4],['USA','Germany','Russia','Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])
print(ser2)

ser3=pd.Series(data=labels)
print(ser3)

# Obtain an individual value of the data series -> a
print(ser3[0])

# Data Frames
from numpy.random import randn
np.random.seed(101)
df=pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

# View a single column of data
print(df['W'])
print(type(df['W']))

print('It is the same as doing this')
print(df.W)

# Getting 2 columns
print(df[['W', 'Z']])

# Mathematical operations can be applied to multiple columns and appended as a new column
df['New Column'] = df['W'] + df['Y']
print(df)

# Dropping a column
df.drop('New Column', axis=1,inplace=True)
print(df)

# Dropping a row
df.drop('E',axis=0,inplace=True)
print(df)

# Working with location of Data in the Data Frame
print(df.loc['A'])
print(df.iloc[2])

print( df.loc['B','Y']) # Specific value and row, column

# Conditional Statements in Dataframes
booldf = df > 0
print(df[booldf])

print(df['W']>0)

# Displaying dataframe after executing condition
print(df[df['W']>0])

print(df[df['Z']<0])

print(df[df['W']>0][['Y','X']]) #Get DataFrame of Y,X when W >0

print(df[(df['W']>0) & (df['Y']>1)]) # Get data frame when W>0, Y>1

# Using Split to break a string
newind = "CA NY WY OR".split()
df['States'] = newind
print(df)
df.set_index('States')
print(df)

# Working with multiple Index Levels
# index levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1'])

print(df.loc['G1'].loc[1]) # Get column A of G1

df.index.names=['Groups','Num']

print(df)

print(df.loc['G2'])

# Obtain specific values
print(df.loc['G1'].loc[2]['A'])

# Working with missing data
# Let's declare some arbitrary rows and columns with data and missing data
d = {'A':[1,2,np.nan], 'B':[5,np.nan, np.nan], 'C':[1,2,3]}

df = pd.DataFrame(d)

print(df)
# Drops rows with NaN as the value
print(df.dropna())
# Drops columns with Nan as value
print(df.dropna(axis=1))
# Drops row with 2 NaNs
print(df.dropna(thresh=2))
# Fills NaN with a value 'Fill Value', usually it is done with 0 or 999999 as these are considered outliers
print(df.fillna(value='Fill Value'))
# Fill NaN with Average value of the row
print(df['A'].fillna(value=df['A'].mean()))

# Using groupby
data = {'Company': ['GOOG','GOOG','MSFT','MFST','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}
df = pd.DataFrame(data)
print(df)

byComp=df.groupby('Company')
print(byComp)

#Some operations that can be done
print(byComp.mean())
print(byComp.sum())
print(byComp.std())
print(byComp.sum().loc['FB'])
print(df.groupby('Company').max())
print(df.groupby('Company').min())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7]) 
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# Merge and Join Data
print(df1, df2, df3)
# Join all data downwards
print(pd.concat([df1,df2,df3]))
 # Concat along columns
print(pd.concat([df1,df2,df3],axis=1))


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left,right,how='inner',on='key'))

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

print(pd.merge(left, right, on=['key1', 'key2']))
print(pd.merge(left, right, how='outer', on=['key1', 'key2']))

# Running Operations on Data Frame
df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
print(df.head())

print(len(df['col2'].unique()))
print(df['col2'].nunique())
print(df['col2'].value_counts())
print(df[(df['col1']>2)& (df['col2']==444)])
# Multiply by 2 using function, and lambda
def times2(x):
    return x*2
print(df['col3'].apply(times2))
print(df['col2'].apply(lambda x: x*2))
print(df.sort_values(by='col2'))
print(df.isnull())






