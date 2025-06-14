
'''
Створіть функцію get_days_from_today(date), 
яка розраховує кількість днів між заданою датою і поточною датою.
'''
# Спосіб 1 - timedelta
from datetime import datetime, timedelta

def get_days_from_today(date: str) -> int:
    date_object = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    difference = today - date_object
    return difference.days

# Приклад. Дата в минулому 2020-10-09 - різниця +1709 днів
day_in_past = get_days_from_today("2020-10-09")
# Приклад. Дата в майбутньому 2025-10-09 - різниця -117 днів
day_in_future = get_days_from_today("2025-10-09")
# Приклад. Сьогоднішня дата - різниця 0 днів
today_day = get_days_from_today("2025-06-14")

print(f"Кількість днів складає: {day_in_past}")
print(f"Кількість днів складає: {day_in_future}")
print(f"Кількість днів складає: {today_day}")
