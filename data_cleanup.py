#Convert date column to yymmdd
df['col 1'] = pd.to_datetime(df['col'],format='%Y%m%d', errors='coerce')


# Get a report of all duplicate records in a dataframe, based on specific columns
dupes = df[df.duplicated(['col1', 'col2', 'col3'], keep=False)]


# Drop Duplicates
df.drop_duplicates()


#format decimals
df..style.format({'% col': '{:,.2f}'.format,})
