import pandas as pd
import matplotlib.pyplot as plt

df_original = pd.read_csv('dane3.csv', delimiter=';')
df = df_original.dropna()

print("Dane z pliku:")
print(df_original)

# Wyznaczenie tablicy ilorazów różnicowych
def ilorazy_roznicowe():
    a = []
    for i in df.index:
        if (i == 0):
            a.append(df['y'][0])
        if (i == 1):
            b = []
            for j in range(0,df.index.max()-i+1):
                b.append((df['y'][j] - df['y'][j+1]) / (df['x'][j] - df['x'][j+1]))
                if (j == 0):
                    a.append(b[0])
        if (i > 1):
            c = []
            for j in range(0,df.index.max()-i+1):
                c.append((b[j] - b[j+1]) / (df['x'][j] - df['x'][j+i]))
                if (j == 0):
                    a.append(c[0])
            b = c
    return a

print("\nTablica ilorazów różnicowych:")
a = ilorazy_roznicowe()
print(f"a = {a}")

# Funkcja interpolacyjna (wzór interpolacyjny Newtona)
def interpolacja(x):
    y = a[0]
    length = len(a)
    for i in range(1,length):
        element = a[i]
        for j in range(0,i):
            element *= (x - df['x'][j])
        y += element
    return y

df_original['F(x)'] = df_original['x'].apply(interpolacja)

print("\nDane z pliku z wartościami interpolowanymi:")
print(df_original)

# plt.plot(df_original['x'], df_original['F(x)'], '-', label="F(x)")
# plt.plot(df_original['x'], df_original['y'], 'o', label="y")
# plt.legend(loc='best')
# plt.show()

# =====================================

print("\nRysowanie wykresu (interpolacja)...")

# precision = 1

# x_values = []
# x_i = df_original['x'].min()

# while x_i < df_original['x'].max():
#     x_values.append(x_i)
#     x_i += precision

# x_values.append(df_original['x'].max())

# df_interpolate = pd.DataFrame({'x': x_values})
# df_interpolate['F(x)'] = df_interpolate['x'].apply(interpolacja)

plt.plot(df_original['x'], df_original['F(x)'], '-', label="F(x)")
plt.plot(df_original['x'], df_original['y'], 'o', label="y")
plt.legend(loc='best')

# plt.plot(df_interpolate['x'], df_interpolate['F(x)'], '-', label="F2(x)")
# plt.plot(df_original['x'], df_original['y'], 'o', label="y2")
# plt.legend(loc='best')
plt.show()