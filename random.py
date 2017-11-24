#inclusive of the right exclusive on the left

#triple quotes for strings expands multiple lines


#Transpose
df.T

#Filtering by something in
df[[for x in  x df.column where 'a' in x ]]


#Tag duplicates find the number of instances
df['dupicate tag '] = df.groupby('col 1').cumcount() + 1


#Filter by what is not contained in another DataFrame
df_3 = df_1[~df_1['col 1']].isin(df_2['col 2'])]


#Wrap jn
\
