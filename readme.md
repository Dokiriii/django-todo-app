# Todo-менеджер на Django

Веб-приложение для управления задачами с авторизацией, статистикой и личным профилем.

## Функционал

- Регистрация и авторизация пользователей
- Создание, редактирование, удаление задач
- Отметка о выполнении
- Фильтрация: все / выполненные / невыполненные
- Личный профиль со статистикой
- Адаптивный дизайн

## Технологии

- Python 3.10+
- Django 4.2
- SQLite (можно заменить на PostgreSQL)
- HTML/CSS

## Документация

Подробная методичка по разработке: [docs/ToDoList_Django.pdf](docs/ToDoList_Django.pdf)

## Установка

```bash
# Клонируем репозиторий
git clone https://github.com/твой-ник/django-todo-app.git
cd django-todo-app

# Создаём виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Устанавливаем зависимости
pip install -r requirements.txt

# Применяем миграции
python manage.py migrate

# Создаём суперпользователя
python manage.py createsuperuser

# Запускаем сервер
python manage.py runserver

## Автор

Dokiriii (Eula)