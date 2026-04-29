from pathlib import Path

MAIN_DOC_URL = 'https://docs.python.org/3/'
"""URL главной документации Python 3."""

BASE_DIR = Path(__file__).parent
"""Корневая директория проекта, вычисленная из расположения файла."""

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
"""Формат даты-времени для именования файлов с результатами."""

PEP_DOC_URL = 'https://peps.python.org/'
"""Базовый URL для всех PEP (Python Enhancement Proposals)."""

EXPECTED_STATUS = {
     'A': ('Active', 'Accepted'),
     'D': ('Deferred',),
     'F': ('Final',),
     'P': ('Provisional',),
     'R': ('Rejected',),
     'S': ('Superseded',),
     'W': ('Withdrawn',),
     '': ('Draft', 'Active'),
 }
"""Маппинг ключа статуса PEP в ожидаемые строковые значения статусов."""
