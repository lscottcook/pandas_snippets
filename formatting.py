#Group-By
df.groupby(['Col1', 'Col2'])

#
df_new = pd.crosstab(df['col1'], df['col2'])
