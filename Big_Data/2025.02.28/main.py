import pandas as pd
import matplotlib.pyplot as plt

columns = ['timestamp', 'id', 'time_data_1', 'time_data_2', 'discreet_data', 'name_surname', 'data1', 'data2', 'data3', 'data4', 'x', 'y', 'z' ]

df = pd.read_csv('data_01.dat', header=None, delimiter=',', names=columns)

print(df)

# 1. Posortowanie po czasie
df.sort_values(by='timestamp')

# 2. Walidacja identyfikatora

# x = df['id'].apply(str).str.match(r'(1|...|9)(0{0,10})(1|...|9)(0|...|9){1,4}(0|1)')

# x = df['id'].apply(str).str.match(r'(1|...|9)(0{0,10})(1|...|9)(0|...|9){1,4}(0|1)')
# .str.match(r'(1|...|9)(0{0-10})(Rand(100-10000))(($1+$3)%2)').astype(bool)
# print(x)

# 3. Przesunięcie w fazie

# print(df['time_data_1'])

df['time_data_1'].plot.line(x='timestamp', y='time_data_1')
plt.show()


# 6. Nazwiska

# print(df['name_surname'].describe())
