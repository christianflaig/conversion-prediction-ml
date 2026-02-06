import numpy as np
import pandas as pd


n = 10000

base = 0.05


age = np.random.randint(18, 76, size=10000)
time_on_site = np.random.randint(0, 16, size=10000)
pages_visited = np.random.randint(0, 6, size=10000)
is_returning = np.random.randint(0, 2, size=10000)

time_norm = time_on_site / 15
pages_norm = pages_visited / 5

p_buy = base + 0.25*is_returning + 0.30*time_norm + 0.20*pages_norm
p_buy = np.clip(p_buy, 0, 0.95)

buy = (np.random.rand(n) < p_buy).astype(int)

df = pd.DataFrame({
    'age': age,
    'time_on_site': time_on_site,
    'pages_visited': pages_visited,
    'is_returning': is_returning,
    'buy': buy
})
print(df['buy'].value_counts(normalize=True))
print(df.groupby('buy')[['time_on_site', 'pages_visited', 'is_returning', 'age']].mean())