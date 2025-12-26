import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)


def print_tree(path: Path, prefix: str = "") -> None:
    try:
        items = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "┗━ [Permission denied]" + Style.RESET_ALL)
        return

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        branch = "┗━ " if is_last else "┣━ "
        next_prefix = prefix + ("   " if is_last else "┃  ")

        if item.is_dir():
            print(f"{prefix}{branch}{Fore.CYAN}{item.name}{Style.RESET_ALL}/")
            print_tree(item, next_prefix)
        else:
            print(f"{prefix}{branch}{Fore.YELLOW}{item.name}{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python three_task.py <path_to_directory>")
        return

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} path does not exist -> {dir_path}")
        return

    if not dir_path.is_dir():
        print(f"{Fore.RED}Error:{Style.RESET_ALL} path is not a directory -> {dir_path}")
        return

    print(f"{Fore.GREEN}{dir_path.name}{Style.RESET_ALL}/")
    print_tree(dir_path)


if __name__ == "__main__":
    main()
