#Group-By
df.groupby(['Col1', 'Col2'])

#
df_new = pd.crosstab(df['col1'], df['col2'])

df_new = pd.concat([df_1, df_2])

#merge


#Merging multiple dfs
 df_list = [df_1, df_2, df_3]
df_combine = reduce(lambda x,y: pd.merge(x, y, on='acronym', how='outer'), df_list)


#Renaming
df_rename = df.rename(columns = {'col1':'Column 1', 'col2':'Column 2'})

 result = df1.append([df2, df3])

 #Write to df not using merged cells
 merge_cells=False
