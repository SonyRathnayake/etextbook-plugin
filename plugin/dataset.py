import pandas as pd
df = pd.read_excel (r'dataset/dataset.xlsx')
cd = pd.DataFrame(df, columns= ['Summary','Phrase'])
print (cd)