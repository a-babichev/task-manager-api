# Task Manager API

REST API для управления задачами (CRUD) на **Flask** с использованием **PostgreSQL** через Docker.

---

## 🛠 Технологии

- Python 3.11
- Flask
- Flask-SQLAlchemy
- Flask-Migrate (Alembic)
- PostgreSQL 16
- Docker & Docker Compose
- python-dotenv
- psycopg2-binary

---

## 🚀 Возможности

- Создание, чтение, обновление и удаление задач (CRUD)
- Время создания хранится в UTC, при выводе можно конвертировать в любой часовой пояс
- Готов к запуску через Docker
- Структура проекта с Factory Pattern и Blueprints

---

## 📦 Структура проекта

```text
task-manager-api/
│
├── app/
│   ├── __init__.py       # Factory и регистрация Blueprint
│   ├── config.py         # Конфигурация
│   ├── extensions.py     # SQLAlchemy и Migrate
│   ├── models.py         # Модель Task
│   ├── routes.py         # CRUD маршруты
│   └── errors.py         # Обработчики ошибок
│
├── migrations/           # Alembic миграции
├── Dockerfile
├── docker-compose.yml
├── .env                  # Настройки окружения
├── requirements.txt
└── run.py                # Точка входа
```

## ⚡ Быстрый старт (Docker)

1. Склонируй репозиторий:

```bash
git clone https://github.com/a-babichev/task-manager-api.git
cd task-manager-api
```
2. Создай .env файл (пример):

```.env
SECRET_KEY=supersecretkey
DATABASE_URL=postgresql+psycopg2://task_user:strong_password@db:5432/task_manager
```
3. Подними контейнеры:
```bash
docker compose up -d
```
4. Инициализация базы и миграции:
```bash
docker compose exec backend flask db init
docker compose exec backend flask db migrate -m "Initial migration"
docker compose exec backend flask db upgrade
```
**API доступно на:**

http://localhost:5000/api/tasks/ 
```bash
📌 Примеры запросов
# Создать задачу
curl -X POST http://localhost:5000/api/tasks \
 -H "Content-Type: application/json" \
 -d '{"title":"Buy milk","description":"2L"}'

# Получить все задачи
curl http://localhost:5000/api/tasks

# Обновить задачу
curl -X PATCH http://localhost:5000/api/tasks/1 \
 -H "Content-Type: application/json" \
 -d '{"completed":true}'

# Удалить задачу
curl -X DELETE http://localhost:5000/api/tasks/1
```
## 🌍 Временные зоны

В базе хранится UTC (created_at)

В API можно конвертировать в любой часовой пояс (например, Europe/Moscow)

## 🧩 Рекомендации

Для продакшена используйте gunicorn вместо встроенного Flask-сервера

Переменные окружения (.env) не коммитить

Использовать Docker Volume для постоянного хранения данных PostgreSQL

## 📝 Лицензия

MIT License


---

## 👨‍💻 Автор
#### GitHub: [Alexey Babichev](https://github.com/a-babichev)
#### Telegram: [@alx_babichev](https://t.me/alx_babichev)
#### Email: [me@a-babichev.ru]()