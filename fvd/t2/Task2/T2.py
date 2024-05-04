str1 = 'аааааааааааа'
str2 = 'ббббббббббббб'

min_len = min(len(str1), len(str2))
result = ""
str3 = 'абабабабабаб'

for i in range(min_len):
    if i % 2 == 0:
        result += str1[i]
    else:
        result += str2[i]

print("Длина первой строки:", len(str1))
print("Длина второй строки:", len(str2))
print("Длина третьей строки:", min_len)

print("Третья строка:", result)

if result == str3:
    print("Тест пройден")
else:
    print("Тест не пройден")