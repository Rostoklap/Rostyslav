second_total = int(input("Введите количество секунд(0-8640000): "))

days, remain = divmod(second_total, 86400)
hours, remain = divmod(remain, 3600)
minutes, remain = divmod(remain, 60)

hh = str(hours).zfill(2)
mm = str(minutes).zfill(2)
ss = str(remain).zfill(2)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not (11 <= days % 100 <= 14):
    day_word = "дни"
else:
    day_word = "дней"

print(f"{days} {day_word}, {hh}:{mm}:{ss}")

