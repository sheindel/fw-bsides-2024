from rich.console import Console
from rich.text import Text
from rich.syntax import Syntax
from rich.table import Table
import os
from inspect import getsource

console = Console()
print = console.print

def string_func(string: str) -> str:
    return "Your string: " + string


def int_func(integer: int) -> int:
    return integer + 42

def ex1():
    def string_func(string: str) -> str:
        return "Your string: " + string

    def int_func(integer: int) -> int:
        return integer + 42

    print(string_func("Hello, world!"))
    print(int_func(100))
    
    # this produces an error in an IDE using a python language server because 
    # we are passing an int to a function that expects a string
    try:
        print(string_func(100))
    except Exception as e:
        print(e)
    

def ex2():
    my_string_var = "Hello, world!"
    my_explicit_string_var: str = "Hello, world!"
    print(f'Types equal? {type(my_string_var) == type(my_explicit_string_var)}')

    # This is a list[int] because all the values are integers
    int_vars = [1, 2, 3, 4, 5]

    # therefore this is an int
    my_var = int_vars[1]

    # typeing dictionaries is done like this: dict[key_type, value_type]
    # This dictionary is typed as dict[str, str] because the keys and values are all strings
    dictionary = {
        "Hello": "world!", 
        "Goodbye": "world!", 
    }

    # This value is typed as string because the dict is uniform
    any_value_from_the_dictionary = dictionary["Hello"]

    # This dictionary is typed as dict[str | int, Unknown] because the keys and values are mixed
    # The keys are more strictly known than the values
    dictionary = {
        "Hello": "world!", 
        "Goodbye": "world!", 
        "A number": 100,
        3: "Another number",
    }

    # This is typed as unknown because of the mixed values types in the dictionary
    any_value_from_the_dictionary = dictionary["Hello"]


def main():
    examples = [ex1, ex2]
    for example in examples:
        console.clear()
        lines = getsource(example)
        # remove the first line
        # dedent all other lines by 4 spaces
        lines = os.linesep.join([line[4:] for line in lines.split(os.linesep)[1:]])
        table = Table(title=example.__name__.replace("_", " "))
        table.add_column("Source")
        output = table.add_column("Output")
        with console.capture() as capture:
            example()
        output = capture.get()
        table.add_row(Syntax(lines, lexer='python'), Text.from_ansi(output))
        console.print(table)
        input("Press Enter to continue to the next example...")
    ex1()
    ex2()


if __name__ == '__main__':
    main()