import os

FILL_CHAR = "█"
EMPTY_CHAR = " "

def format_percentage(num: float) -> str:
    return f"{int(num * 100):3}%|"

def format_bar(num: float, limit: float) -> str:
    fill_count = int(limit * num)
    empty_count = limit - fill_count
    return (FILL_CHAR * fill_count) + (EMPTY_CHAR * empty_count)

def format_count(count: int, total: int) -> str:
    width = len(str(total))
    return f"| {count:>{width}}/{total} "

def ft_tqdm(lst: range):
    total = len(lst)
    size = os.get_terminal_size()

    for i, item in enumerate(lst, start=1):
        percent = i / total
        percentage = format_percentage(percent)
        count = format_count(i, total)
        total_len = len(percentage) + len(count) + 25
        bar = format_bar(percent, (size.columns - total_len))
        print(f"""\r{percentage}{bar}{count}""", end="", flush=True)
        yield item

    print()
