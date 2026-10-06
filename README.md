# Эмулятор командной строки с VFS (вариант 11)

Консольный эмулятор командной строки UNIX-подобной ОС на Python 3.

## Запуск

```
run.bat [--vfs ПУТЬ] [--script ПУТЬ]   # Windows
./run.sh [--vfs ПУТЬ] [--script ПУТЬ]  # Linux
```

- `--vfs` — путь к VFS (имя файла показывается в приглашении).
- `--script` — стартовый скрипт, комментарии начинаются с `#`.

Команды: `ls`, `cd` (заглушки), `exit`.

## Тесты

```
py -m unittest discover -s tests
```

Скрипты проверки параметров: `scripts\test_basic.bat`,
`scripts\test_errors.bat`, `scripts\test_interactive.bat`.
