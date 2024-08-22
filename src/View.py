from colorama import Fore, init

init()


class View:
    # Version: 1.1.0
    def alert(self, msg: str) -> None:
        # Prints an alert message in red and resets color.
        print("\n")
        print(Fore.RED + msg)
        self.reset()

    def info(self, msg: str) -> None:
        # Prints an informational message in blue and resets color.
        print(Fore.BLUE + msg)
        self.reset()

    def ok(self, msg: str) -> None:
        # Prints a success message in green with 'OK' appended and resets color.
        print("\n" + Fore.GREEN + msg + "...........................OK")
        self.reset()

    def reset(self) -> None:
        # Resets the color to default.
        print(Fore.RESET)

    def highlight_for_debugging(self, data: str) -> None:
        # Prints a debugging section with separators.
        self.alert("-" * 59)
        print(data)
        self.alert("-" * 59)

    def header(self, text: str) -> None:
        # Prints a header in blue with an underline.
        print("\n" + Fore.BLUE + text)
        self.info("_" * 70)
