import os
import hashlib
import io
from rich.console import Console

from helpers import create_source_output_table, get_function_source
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

    print(f"""Hello, "{world_string}"!
          Multiple lines!
          Very easily (but its indented?)
          """)

    print(f"Hello, {world_string}!\n"
          f"Multiple lines!\n"
          "Very easily (no indents!)"
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
    for index in range(len(my_int_list)):
        print(my_int_list[index])
    
    # Better
    print("Better: Object based iteration")
    for item in my_int_list:
        print(item)
    
    # Other scenarios
    print("Advanced: Enumerated")
    for index,item in enumerate(my_int_list):
        print(f'{item} at index {index}')
    
    print("Advanced: Reversed")
    for item in reversed(my_int_list):
        print(item)
    
    print("Advanced: Slicing, all items EXCEPT the first")
    for item in my_int_list[1:]:
        print(item)

    print("Advanced: Slicing, every other item")
    for item in my_int_list[::2]:
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


def verbose_truthy_example():
    my_list = [1, 2, 3]
    if my_list:
        print("List is empty")
    
    my_list_is_empty = bool(my_list)
    my_list_is_empty = not my_list
    if my_list_is_empty:
        print("List is empty")


def main():
    examples = [string_formatting, with_statement, list_iterate_examples, dict_iterate_examples, truthiness_examples, verbose_truthy_example]
    for example in examples:
        console.clear()
        print(create_source_output_table(example, console))

        is_not_last_item = example != examples[-1]
        if is_not_last_item:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()