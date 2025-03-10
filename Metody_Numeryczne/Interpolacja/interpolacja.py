import pandas as pd
import matplotlib.pyplot as plt

df_original = pd.read_csv('dane.csv', delimiter=';', index_col='i')
df = df_original.dropna()

print("Dane z pliku:")
print(df_original)

# Wyznaczenie tablicy ilorazów różnicowych
def ilorazy_roznicowe():
    a = []
    for i in df.index:
        if (i == 0):
            a.append(df['w'][0])
        if (i == 1):
            b = []
            for j in range(0,df.index.max()-i+1):
                b.append((df['w'][j] - df['w'][j+1]) / (df['x'][j] - df['x'][j+1]))
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

print("==============================")
print("Tablica ilorazów różnicowych:")
a = ilorazy_roznicowe()
print(f"a = {a}")
print("==============================")

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

df_original['F'] = df_original['x'].apply(interpolacja)

print("Dane z pliku z wartościami interpolowanymi:")
print(df_original)

df_original.plot.line(x='x', y='F', marker='o')
plt.show()
