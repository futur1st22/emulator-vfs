"""Модуль эмулятора командной строки для курса конфигурационного управления."""

import sys


class ShellEmulator:
    """Класс эмулятора командной строки UNIX-подобной ОС."""

    def __init__(self, vfs_name="default_vfs"):
        """Инициализация состояния эмулятора и имени файловой системы."""
        self.vfs_name = vfs_name
        self.is_running = True

    def parse_command(self, user_input):
        """Разбиение введенной строки на имя команды и список аргументов."""
        tokens = user_input.strip().split()
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
        """Вызов соответствующего обработчика по имени команды."""
        if cmd == "ls":
            self.handle_ls(args)
        elif cmd == "cd":
            self.handle_cd(args)
        elif cmd == "exit":
            self.handle_exit(args)
        else:
            print(f"emulator: command not found: {cmd}")

    def run(self):
        """Запуск интерактивного цикла диалога с пользователем."""
        while self.is_running:
            try:
                prompt = f"{self.vfs_name}$ "
                user_input = input(prompt)
                cmd, args = self.parse_command(user_input)
                if cmd:
                    self.execute(cmd, args)
            except (EOFError, KeyboardInterrupt):
                print()
                self.is_running = False


def main():
    """Точка входа для запуска первого этапа эмулятора."""
    emulator = ShellEmulator()
    emulator.run()


if __name__ == "__main__":
    main()