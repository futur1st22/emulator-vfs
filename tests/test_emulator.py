"""Тесты эмулятора командной строки."""

import io
import unittest
from contextlib import redirect_stdout

from src.emulator import ShellEmulator, main


class TestEmulator(unittest.TestCase):
    """Тесты парсера, команд и стартового скрипта."""

    def setUp(self):
        """Создание эмулятора для каждого теста."""
        self.emulator = ShellEmulator()

    def test_parse_command(self):
        """Команда отделяется от аргументов, комментарий отбрасывается."""
        result = self.emulator.parse_command("cd  docs # go")
        self.assertEqual(result, ("cd", ["docs"]))

    def test_unknown_command(self):
        """Неизвестная команда возвращает ошибку."""
        with redirect_stdout(io.StringIO()):
            self.assertFalse(self.emulator.execute("foo", []))

    def test_exit(self):
        """Команда exit останавливает эмулятор."""
        self.emulator.execute("exit", [])
        self.assertFalse(self.emulator.is_running)

    def test_missing_script(self):
        """Отсутствующий стартовый скрипт дает код возврата 1."""
        with redirect_stdout(io.StringIO()):
            code = main(["--script", "no_such_file.txt"])
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
