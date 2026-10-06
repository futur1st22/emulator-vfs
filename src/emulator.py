"""Модуль эмулятора командной строки для курса конфигурационного управления."""

import argparse
import sys
from pathlib import Path

DEFAULT_VFS_NAME = "default_vfs"
COMMENT_CHAR = "#"


def make_vfs_name(vfs_path):
    """Получение имени VFS для приглашения к вводу из пути к ней."""
    if not vfs_path:
        return DEFAULT_VFS_NAME
    return Path(vfs_path).stem or DEFAULT_VFS_NAME


def read_script(script_path):
    """Чтение строк стартового скрипта, при ошибке возвращает None."""
    try:
        with open(script_path, encoding="utf-8") as script_file:
            return script_file.readlines()
    except (OSError, UnicodeDecodeError) as error:
        print(f"emulator: cannot read script '{script_path}': {error}")
        return None


class ShellEmulator:
    """Класс эмулятора командной строки UNIX-подобной ОС."""

    def __init__(self, vfs_path=None):
        """Инициализация состояния эмулятора и имени файловой системы."""
        self.vfs_path = vfs_path
        self.vfs_name = make_vfs_name(vfs_path)
        self.is_running = True

    def get_prompt(self):
        """Формирование строки приглашения к вводу с именем VFS."""
        return f"{self.vfs_name}$ "

    def parse_command(self, user_input):
        """Разбиение строки на команду и аргументы без учета комментария."""
        line = user_input.split(COMMENT_CHAR, 1)[0]
        tokens = line.split()
        if not tokens:
            return "", []
        return tokens[0], tokens[1:]

    def handle_ls(self, args):
        """Обработчик-заглушка для команды ls."""
        args_str = " ".join(args)
        if args_str:
            print(f"ls: {args_str}")
        else:
            print("ls")

    def handle_cd(self, args):
        """Обработчик-заглушка для команды cd."""
        args_str = " ".join(args)
        if args_str:
            print(f"cd: {args_str}")
        else:
            print("cd")

    def handle_exit(self, args):
        """Остановка бесконечного цикла и завершение работы."""
        self.is_running = False

    def execute(self, cmd, args):
        """Вызов обработчика по имени команды.

        Возвращает True при успешном выполнении и False при ошибке.
        """
        if cmd == "ls":
            self.handle_ls(args)
        elif cmd == "cd":
            self.handle_cd(args)
        elif cmd == "exit":
            self.handle_exit(args)
        else:
            print(f"emulator: command not found: {cmd}")
            return False
        return True

    def run_script(self, script_path):
        """Выполнение стартового скрипта с выводом ввода и результата.

        Ошибка в команде не прерывает скрипт, а выводится с номером строки.
        Возвращает False, если файл скрипта не удалось прочитать.
        """
        lines = read_script(script_path)
        if lines is None:
            return False
        for line_number, line in enumerate(lines, start=1):
            cmd, args = self.parse_command(line)
            if not cmd:
                continue
            print(f"{self.get_prompt()}{line.strip()}")
            if not self.execute(cmd, args):
                print(f"emulator: error in {script_path}, line {line_number}")
            if not self.is_running:
                break
        return True

    def run(self):
        """Запуск интерактивного цикла диалога с пользователем."""
        while self.is_running:
            try:
                user_input = input(self.get_prompt())
                cmd, args = self.parse_command(user_input)
                if cmd:
                    self.execute(cmd, args)
            except (EOFError, KeyboardInterrupt):
                print()
                self.is_running = False


def parse_args(argv=None):
    """Разбор параметров командной строки эмулятора."""
    parser = argparse.ArgumentParser(
        description="Эмулятор командной строки UNIX-подобной ОС с VFS."
    )
    parser.add_argument("--vfs", help="путь к физическому расположению VFS")
    parser.add_argument("--script", help="путь к стартовому скрипту")
    return parser.parse_args(argv)


def print_debug_config(args):
    """Отладочный вывод всех заданных параметров запуска."""
    print("[debug] startup parameters:")
    print(f"[debug]   vfs    = {args.vfs or '(not set)'}")
    print(f"[debug]   script = {args.script or '(not set)'}")


def main(argv=None):
    """Точка входа: разбор параметров, стартовый скрипт и диалог."""
    args = parse_args(argv)
    print_debug_config(args)
    emulator = ShellEmulator(args.vfs)
    if args.script and not emulator.run_script(args.script):
        return 1
    emulator.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
