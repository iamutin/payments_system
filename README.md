# Payments System
Проект представляет собой бэкенд-сервис для приема и обработки платежей, реализованный на Django.

**Оригинальное ТЗ**: [Ссылка](https://gist.github.com/an1creator/312d0b7cb68da921e725f9929accc971)

## 📌 Функционал (по ТЗ)
- **Создание платежа**
- **Проверка статуса платежа**

## 🛠 Технологии
- Python 3.9
- Django 4.2.17
- Django REST Framework (DRF)
- MySQL
- Docker-compose

## 🚀 Установка

### 1. Клонировать репозиторий:
```shell
git clone git@github.com:iamutin/payments_system.git
cd payments_system
```
### 2. Создать и активировать виртуальное окружение.
### 3. Установить зависимости:
```shell
poetry install
```
### 4. Создать файл `.env` на основе примера: 
```shell
cp .env.example .env
```
### 5. Поднять базу данных, используя docker:
```shell
docker compose up -d
```
### 6. Создать и применить миграции:
```shell
python manage.py makemigrations
```
```shell
python manage.py migrate
```
### 7. Запустить приложение
```shell
python manage.py runserver
```