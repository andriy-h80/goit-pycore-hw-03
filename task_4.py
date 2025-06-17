
'''
У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження.
Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays,
яка допоможе вам визначати, кого з колег потрібно привітати.
Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.
У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження.
Оскільки дні народження колег можуть припадати на вихідні,
ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.
'''

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year = today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year = today.year + 1)
    
        difference_days = (birthday_this_year - today).days
        if 0 <= difference_days <= 7:
            congratulation_date = birthday_this_year
            if birthday_this_year.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.06.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# Список привітань на цьому тижні: [{'name': 'John Doe', 'congratulation_date': '2025.06.23'}]
