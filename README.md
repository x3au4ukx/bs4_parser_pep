# Парсер документации Python

## Описание

Проект представляет собой CLI-утилиту для парсинга официальной документации Python. 
Она решает задачи:
- мониторинга новых возможностей в каждой версии;
- получения списка доступных версий Python;
- скачивания полной HTML-документации;
- анализа статусов PEP и проверки их соответствия.

**Польза:** автоматизация сбора информации из документации, экономия времени 
на ручном поиске и структурирование данных в отчётах (CSV, pretty-таблицы).

## Установка

1. Клонируйте репозиторий:
```bash
git clone <URL репозитория>
cd <папка проекта>
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Примеры использования
```bash
# Показать последние нововведения в Python
python main.py whats-new

"29.04.2026 10:20:37 - [INFO] - Парсер запущен!"
"29.04.2026 10:20:37 - [INFO] - Аргументы командной строки: Namespace(mode='whats-new', clear_cache=False, output=None)"
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 23/23 [00:03<00:00,  6.84it/s]
Ссылка на статью Заголовок Редактор, автор
https://docs.python.org/3/whatsnew/3.14.html What’s new in Python 3.14¶  Editors: Adam Turner and Hugo van Kemenade  
https://docs.python.org/3/whatsnew/3.13.html What’s New In Python 3.13¶  Editors: Adam Turner and Thomas Wouters  
https://docs.python.org/3/whatsnew/3.12.html What’s New In Python 3.12¶  Editor: Adam Turner
...
"29.04.2026 10:20:41 - [INFO] - Парсер завершил работу."

# Получить список доступных версий
python main.py latest-versions

"29.04.2026 10:22:48 - [INFO] - Парсер запущен!"
"29.04.2026 10:22:48 - [INFO] - Аргументы командной строки: Namespace(mode='latest-versions', clear_cache=False, output=None)"
Ссылка на документацию Версия Статус
https://docs.python.org/3.15/ 3.15 in development
https://docs.python.org/3.14/ 3.14 stable
https://docs.python.org/3.13/ 3.13 stable
...
https://www.python.org/doc/versions/ All versions 
"29.04.2026 10:22:49 - [INFO] - Парсер завершил работу."

# Скачать архив документации
python main.py download --clear-cache

"29.04.2026 10:24:13 - [INFO] - Парсер запущен!"
"29.04.2026 10:24:13 - [INFO] - Аргументы командной строки: Namespace(mode='download', clear_cache=True, output=None)"
"29.04.2026 10:24:13 - [INFO] - Clearing all items from the cache"
"29.04.2026 10:24:16 - [INFO] - Архив был загружен и сохранён: ...\bs4_parser_pep\src\downloads\python-3.14-docs-html.zip"
"29.04.2026 10:24:16 - [INFO] - Парсер завершил работу."

# Собрать статистику статусов PEP в CSV
python main.py pep --output file

"29.04.2026 10:25:58 - [INFO] - Парсер запущен!"
"29.04.2026 10:25:58 - [INFO] - Аргументы командной строки: Namespace(mode='pep', clear_cache=False, output='file')"
"29.04.2026 10:31:27 - [WARNING] - Несовпадающие статусы:"
"29.04.2026 10:31:27 - [WARNING] - https://peps.python.org/pep-0401/"
"29.04.2026 10:31:27 - [WARNING] - Статус в карточке: April Fool!"
"29.04.2026 10:31:27 - [WARNING] - Ожидаемые статусы: ['Rejected']"
"29.04.2026 10:32:39 - [INFO] - Файл с результатами был сохранён: ...\bs4_parser_pep\src\results\pep_2026-04-29_10-32-39.csv"
"29.04.2026 10:32:39 - [INFO] - Парсер завершил работу."

# Вывести результат в виде таблицы
python main.py whats-new --output pretty

```

## Использованные технологии

| Технология | Роль в проекте | Документация |
|------------|----------------|---------------|
| BeautifulSoup4 | Парсинг HTML-страниц документации | bs4 |
|requests-cache | Кеширование HTTP-запросов с повторами | requests-cache|
|tqdm | Отображение прогресса при парсинге | tqdm |
| PrettyTable | Вывод данных в виде читаемых таблиц | prettytable|
| lxml | Быстрый парсинг HTML/XML для BeautifulSoup | lxml |
| argparse | Разбор аргументов командной строки	| (встроенная библиотека) |

## Структура проекта
```main.py``` — точка входа, маршрутизация режимов;

```configs.py``` — настройка логирования и CLI-аргументов;

```outputs.py``` — управление выводам (pretty/CSV/default);

```utils.py``` — вспомогательные функции (запросы, поиск тегов);

```constants.py``` — URL, пути, маппинг статусов;

```exceptions.py``` — пользовательские исключения.