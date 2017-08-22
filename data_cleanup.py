#Convert date column to yymmdd
df['col 1'] = pd.to_datetime(df['col'],format='%Y%m%d', errors='coerce')
