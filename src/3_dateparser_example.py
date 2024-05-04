from inspect import getsource

from rich.console import Console
console = Console()
def print(*args, **kwargs):
    console.print(*args, **kwargs)


def dateparser_example():
    import dateparser
    def parse_test(date_str: str, settings=None):
        formatted_date_str = date_str.ljust(12, ' ')
        parsed_data = dateparser.parse(date_str, settings=settings)
        print(f"{formatted_date_str} {parsed_data}")
        
    parse_test('2024-05-04')
    parse_test('5/4/2024')
    parse_test('05-04-2024')
    parse_test('04 May 2024')
    parse_test('today')
    parse_test('today 7AM')
    parse_test('yesterday')
    parse_test('1 hour ago')
    parse_test('now')
    parse_test('2 days', settings={'PREFER_DATES_FROM': 'future'})
    parse_test('+1 year', settings={'PREFER_DATES_FROM': 'future'})


def main():
    import os
    from rich.table import Table
    from rich.syntax import Syntax
    from rich.text import Text
    lines = getsource(dateparser_example)
    lines = os.linesep.join([line[4:] for line in lines.split(os.linesep)[1:]])
    # print(lines)
    with console.capture() as capture:
        dateparser_example()
    output = capture.get()
    # add 5 newlines at the beginning
    output = '\n' * 3 + output
    table = Table()
    table.add_column("Source")
    table.add_column("Output")
    table.add_row(Syntax(lines, lexer='python', line_numbers=True), Text.from_ansi(output))
    print(table)


if __name__ == '__main__':
    main()