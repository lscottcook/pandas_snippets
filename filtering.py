
#filter using and/or operators
df = df[((df['col1']=='apples') | (df['col2']=='grapes')) &
(df['col4']=='female') | (df[col5]='pink')]

#listing duplicates 
match_columns = ['ColumnA', 'ColumnB']
duplicates=  df.loc[df.duplicated(match_columns)]
