
from rich.console import Console
from helpers import create_source_output_table

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


examples = [dateparser_example]
def main():
    for example in examples:
        console.clear()
        print(create_source_output_table(example, console))

        is_not_last_item = example != examples[-1]
        if is_not_last_item:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()