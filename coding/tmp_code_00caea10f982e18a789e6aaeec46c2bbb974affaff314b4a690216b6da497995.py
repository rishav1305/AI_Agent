
import pandas as pd
df = pd.DataFrame([[1,2]], columns=['a', 'b'])
print(df)
df.to_csv('test.csv')
print("CSV file created successfully")
