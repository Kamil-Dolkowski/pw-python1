import pandas as pd
import matplotlib.pyplot as plt

columns = ['timestamp', 'id', 'time_data_1', 'time_data_2', 'discreet_data', 'name_surname', 'data1', 'data2', 'data3', 'data4', 'x', 'y', 'z' ]

df = pd.read_csv('data_01.dat', header=None, delimiter=',', names=columns)

print(df)

# 1. Posortowanie po czasie
df = df.sort_values(by='timestamp')

# 2. Walidacja identyfikatora

print("\n===Błędy z identyfikatorem:")

x = df['id'].apply(str).str.match(r'(1|...|9)(0{0,10})(1|...|9)(0|...|9){1,4}(0|1)')

# x = df['id'].apply(str).str.match(r'(1|...|9)(0{0,10})(1|...|9)(0|...|9){1,4}(0|1)')
# .str.match(r'(1|...|9)(0{0-10})(Rand(100-10000))(($1+$3)%2)').astype(bool)
print(x)

# 3. Przesunięcie w fazie

print("\n===Błędy z fazą:")

differences = df[['timestamp','time_data_1']].copy()
differences['różnica'] = differences['time_data_1'].diff()

print(differences[abs(differences['różnica']) > 0.1])

# 4. Amplituda

print("\n===Błędy z amplitudą:")

print(df['time_data_2'].describe())

differences = df[['timestamp','time_data_2']].copy()
differences['różnica'] = differences['time_data_2'].diff()

print(differences[abs(differences['różnica']) > 0.05])

# 5. Dane dyskretne

print("\n===Dane dyskretne:")

print(df['discreet_data'].value_counts())

# 6. Nazwiska

print("\n===Nazwiska:")

differences = df['name_surname'].value_counts().copy()

print(differences[differences < 20000])
print("/nMniej niż 10 powtórzeń:")
print(differences[differences < 10])

# 7. Wartości ciągłe


# df.plot.line(x='timestamp', y='time_data_1')
# plt.show()

# df.plot.line(x='timestamp', y='time_data_2')
# plt.show()