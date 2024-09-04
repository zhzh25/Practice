import pandas as pd



# def modify_excel_file(input_file, output_file, column_name, char):
#     # Чтение файла Excel
#     df = pd.read_excel(input_file)
#
#     # Добавление символа в начало и конец каждой строки в указанном столбце
#     df[column_name] = char + df[column_name].astype(str) + char
#
#     # Сохранение измененного DataFrame в новый файл Excel
#     df.to_excel(output_file, index=False)
#
# input_excel_file = 'E:/101internet/links.xlsx' # Имя входного файла
# output_excel_file = 'E:/101internet/links_final.xlsx'  # Имя выходного файла
# column_to_modify = "link" # Название столбца для изменения
# character_to_add = '"'  # Символ для добавления
#
# modify_excel_file(input_excel_file, output_excel_file, column_to_modify, character_to_add)
#
# print("Файл успешно изменен и сохранен.")

df = pd.read_excel('E:/101internet/links.xlsx')

# Задайте символы, которые нужно добавить
start_char = '"'  # Символ для добавления в начало
end_chars = '",'  # Символы для добавления в конец

# Применение изменений ко всем строкам в каждом столбце
for column in df.columns:
    df[column] = df[column].astype(str).apply(lambda x: f"{start_char}{x}{end_chars}")

# Сохранение измененного DataFrame в новый файл Excel
df.to_excel('E:/101internet/links_final.xlsx', index=False)

print('Файл сохранен')