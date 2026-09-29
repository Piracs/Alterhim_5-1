"""Модуль конфигурации приложения."""
import os

EXCEL_FILE: str = "Mark_fail.xlsx"
COLUMN: str = "A"

# Начальные настройки для инкрементирования сессий коробки
DEFAULT_BATCH_PREFIX: str = "Партия"
try:
    from android.storage import primary_external_storage_path
except ImportError:
    def primary_external_storage_path() -> str:
        return "/storage/emulated/0"


DEFAULT_SAVE_DIR: str = os.path.join(
    primary_external_storage_path(),
    "Download",
    "Alterhim",
)

