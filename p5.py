import pandas as pd

def clean_prices(csv_file, output_file):
    # Чтение CSV файла
    df = pd.read_csv(csv_file)

    # Очистка данных в столбце 'Price'
    df['Price'] = df['Price'].str.replace('руб.', '', regex=False).str.replace(' ', '').str.replace(',', '').astype(str)

    # Сохранение очищенного DataFrame в новый CSV файл
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

# Путь к входному CSV файлу
input_csv = 'prices_from_divanru.csv'
# Путь к выходному CSV файлу
output_csv = 'cleaned_prices_from_divanru.csv'

# Очистка цен и сохранение результата
clean_prices(input_csv, output_csv)
