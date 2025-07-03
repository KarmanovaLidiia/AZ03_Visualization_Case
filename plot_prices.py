import pandas as pd
import matplotlib.pyplot as plt

file_path = 'cleaned_prices.csv'
data = pd.read_csv(file_path)

prices = data['Price']

plt.hist(prices, bins=10, edgecolor='black')
plt.title('Гистограмма цен на квартиры')
plt.xlabel('Цена (в рублях)')
plt.ylabel('Частота')
plt.savefig("hist_prices.png")  # сохраняем как картинку
print("✅ График сохранён в файл hist_prices.png")
