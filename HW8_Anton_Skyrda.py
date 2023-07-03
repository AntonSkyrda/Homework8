from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    current_date = datetime.now().date()

    # Визначаємо перший день наступного тижня
    next_week_start = current_date + timedelta(days=(7 - current_date.weekday()))

    # Створюємо словник, щоб згрупувати користувачів по днях народження
    birthdays = {}

    # Перебираємо користувачів і зберігаємо їх у відповідний день
    for user in users:
        # Отримуємо день народження поточного року
        birthday = user['birthday'].replace(year=current_date.year).date()

        # Визначаємо день привітання для користувача
        if birthday.weekday() >= 5:  # Якщо день народження вихідний
            greeting_day = next_week_start
        else:
            greeting_day = birthday

        # Додаємо користувача до списку привітань
        if greeting_day in birthdays:
            birthdays[greeting_day].append(user['name'])
        else:
            birthdays[greeting_day] = [user['name']]

    # Виводимо список привітань у форматі "День: Користувачі"
    for day, users in birthdays.items():
        day_name = day.strftime("%A")
        user_list = ', '.join(users)
        print(f"{day_name}: {user_list}")


users = [
    {'name': 'Bill', 'birthday': datetime(1990, 7, 3)},
    {'name': 'Jill', 'birthday': datetime(1985, 7, 5)},
    {'name': 'Kim', 'birthday': datetime(1998, 7, 8)},
    {'name': 'Jan', 'birthday': datetime(2000, 7, 9)}
]

get_birthdays_per_week(users)
