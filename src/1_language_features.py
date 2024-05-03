import os
import hashlib
import io
from rich.console import Console
console = Console()
print = console.print

def string_formatting():
    world_string = "world"

    # too many ways to format strings
    print("Hello, %s!" % world_string)
    print("Hello, {0}!".format(world_string))

    # better, but kind of long...
    # and uneeded characters
    print("Hello, " + world_string + "!")

    # f-strings are the best, 3.6 forward
    print(f"Hello, {world_string}!")

    print(f"Hello, '{world_string}'!")
    print(f'Hello, "{world_string}"!')
    print(f"Hello, \"{world_string}\"!")

    print(f"""Hello, "{world_string}"!
          Multiple lines!
          Very easily (but its indented?)
          """)

    print(f"Hello, {world_string}!\n"
          f"Multiple lines!\n"
          f"Very easily (no indents!)"
    )


def with_statement():
    def calculate_md5(file: io.BufferedReader):
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def open_close():
        file = open('1_language_features.py', 'rb')
        print(calculate_md5(file))
        file.close()
    
    def with_close_example():
        with open('1_language_features.py', 'rb') as file:
            print(calculate_md5(file))
        # File is automatically closed after with block
        
    open_close()
    with_close_example()


def list_iterate_examples():
    my_int_list = [1, 2, 3, 4, 5]
    
    # Okay
    print("Okay: Range based iteration")
    for i in range(len(my_int_list)):
        print(my_int_list[i])
    
    # Better
    print("Better: Object based iteration")
    for item in my_int_list:
        print(item)
    
    # Other scenarios
    print("Advanced: Enumerated")
    for i,item in enumerate(my_int_list):
        print(f'{item} at index {i}')
    
    print("Advanced: Reversed")
    for item in reversed(my_int_list):
        print(item)

    print("Advanced: Slicing, every other item")
    for item in my_int_list[::2]:
        print(item)
    
    print("Advanced: Slicing, all items EXCEPT the first")
    for item in my_int_list[1:]:
        print(item)

    print("Advanced: Slice based reversed")
    for item in my_int_list[::-1]:
        print(item)
    

def dict_iterate_examples():
    my_dict = {
        "Hello": "world!",
        "Goodbye": "world!",
        "A number": 100,
        3: "Another number",
    }
    
    print("Key based iteration")
    # equivalent to `for key in my_dict.keys()`
    for key in my_dict:
        print(f'{key}: {my_dict[key]}')
    
    print("Item based iteration")
    for key,value in my_dict.items():
        print(f'{key}: {value}')


def truthiness_examples():
    items = [
        "Hello, world!",
        "",
        [1, 2, 3],
        [],
        {"Hello": "world!"},
        {},
    ]
    
    for item in items:
        print(f"Is {item} truthy? {bool(item)}")


def main():
    import os
    import inspect
    from rich.table import Table
    from rich.syntax import Syntax
    from rich.text import Text
    examples = [string_formatting, with_statement, list_iterate_examples, dict_iterate_examples, truthiness_examples]
    for example in examples:
        with console.capture() as capture:
            example()
        output = capture.get()

        source = inspect.getsource(example)
        source = os.linesep.join([line[4:] for line in source.split(os.linesep)[1:]])

        table = Table(title=example.__name__.replace("_", " "))
        table.add_column("Source")
        table.add_column("Output")
        table.add_row(Syntax(source, lexer='python'), Text.from_ansi(output))

        print(table)

        if example != examples[-1]:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()
