import pandas as pd


def remove_every_second_row(input_file, output_file):
    # Читаем файл Excel
    df = pd.read_excel(input_file)

    # Удаляем каждую вторую строку
    df_filtered = df.iloc[::2].reset_index(drop=True)

    # Сохраняем новый файл Excel
    df_filtered.to_excel(output_file, index=False)


# Замените на путь к вашему файлу
input_excel_file = 'E:/101internet/delite_links.xlsx'  # Входной файл
output_excel_file = 'E:/101internet/delite_links_final.xlsx'  # Выходной файл

remove_every_second_row(input_excel_file, output_excel_file)

print("Каждая вторая строка успешно удалена и файл сохранен.")