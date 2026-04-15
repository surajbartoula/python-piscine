import os


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    Prints dynamically updating progress bar every time a value is requested.
    """
    total = len(lst)
    # Get terminal width
    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80  # fallback if terminal size not available
    for i, item in enumerate(lst, 1):
        # Calculate progress stats
        percent = (i / total) * 100

        # Build the bar components
        # Reserve space for the prefix and suffix text
        prefix = f"{int(percent):3}%|["
        suffix = f"]| {i}/{total}"

        # Calculate how many '=' can fit in the remaining terminal space
        max_bar_width = 96
        bar_width = min(max_bar_width, terminal_width
                        - len(prefix) - len(suffix) - 2)
        # Floor division 5 // 2 = 2(int)
        filled_len = int(bar_width * i // total)

        # Construct the bar string
        bar = '=' * (filled_len - 1) + '>' if filled_len > 0 else ''
        bar = bar.ljust(bar_width)

        # Print using \r to overwrite the current line
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
        yield item


def main():
    """
    Empty main function to satisfy the project requirement
    without exectuting additional test logic
    """
    pass


if __name__ == "__main__":
    main()
