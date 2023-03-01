pas = input("Введите пароль:   ")
if len(pas) < 5:
    print("Пароль короткий")
elif pas[0:6] == "qwerty":
    print("Ненадежный")
else:
    print('OK')