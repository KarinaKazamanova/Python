a = input("Введите текст, который нужно архивировать: ")  
symbols = []
s_count = []
count = 1
for i in range(1, len(a)):
    if a[i - 1] == a[i]:
        count += 1
        continue
    symbols.append(a[i-1])
    s_count.append(count)
    count = 1
symbols.append(a[i])
s_count.append(count)
zip_a = list(map(lambda x, y: str(x) + str(y),s_count, symbols))
print(f"Архивированная строка: {''.join(zip_a)}")
unzip_a = list(map(lambda x, y: int(x) * str(y), s_count, symbols))
print(f"Разархивированная строка: {''.join(unzip_a)}")
