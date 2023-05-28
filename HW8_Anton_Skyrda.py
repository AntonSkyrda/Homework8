from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    # Отримуємо поточну дату
    today = datetime.now().date()

    # Визначаємо початок і кінець тижня
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Створюємо словник для зберігання користувачів по днях тижня
    birthdays_per_week = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Проходимося по користувачам і додаємо їх до відповідних днів тижня
    for user in users:
        birthday = user["birthday"].date()
        if start_of_week <= birthday <= end_of_week:
            # Визначаємо день тижня для дня народження
            birthday_weekday = birthday.strftime("%A")
            birthdays_per_week[birthday_weekday].append(user["name"])

    # Виводимо іменинників по днях тижня
    for weekday, names in birthdays_per_week.items():
        if names:
            print(f"{weekday}: {', '.join(names)}")
