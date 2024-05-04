import hashlib
import io
from rich.console import Console


from helpers import create_source_output_table
console = Console()
print = console.print

def string_formatting_left_to_right():
    world_string = "world"

    # too many ways to format strings
    print("Hello, %s!\n" % world_string)
    print("Hello, {0}!\n".format(world_string))

    # better, but kind of long...
    # and uneeded characters
    print("Hello, " + world_string + "!\n")

    # f-strings are the best, 3.6 forward
    print(f"Hello, {world_string}!\n")

    print(f"""Hello, "{world_string}"!
          Multiple lines!
          Very easily (but its indented?)
          """)

    print(f"Hello, {world_string}!\n"
          f"Multiple lines!\n"
          "Very easily (no indents!)"
    )


def with_statement_dependency():
    def calculate_md5(file: io.BufferedReader):
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def open_close():
        file = open('_1_language_features.py', 'rb')
        print(calculate_md5(file))
        # ...
        # ...
        # ... 
        file.close()
    
    def with_close_example():
        with open('_1_language_features.py', 'rb') as file:
            print(calculate_md5(file))
            # ...
            # ...
            # ...
        
        # no file.close() needed
        
    open_close()
    with_close_example()


def list_iterate_examples():
    my_int_list = [8, 6, 7]
    
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


def less_obfuscated_code():
    my_int_list = [5, 3, 0, 9]
    
    print("Advanced: Slice based reversed")
    for item in my_int_list[::-1]:
        print(item)
    
    print("Advanced: Reversed")
    for item in reversed(my_int_list):
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
    print()
    
    print("Item based iteration")
    for key,value in my_dict.items():
        print(f'{key}: {value}')
    print()


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
        print(f"Is {item} truthy? {bool(item)}\n")


def verbose_truthy_example():
    my_list = [1, 2, 3]
    if my_list:
        print("List is NOT empty")
    if not my_list:
        print("List is empty")
    
    my_list_is_empty = bool(my_list)
    my_list_is_empty = not my_list
    if my_list_is_empty:
        print("List is empty")
    else:
        print("List is NOT empty")


examples = [string_formatting_left_to_right, with_statement_dependency, list_iterate_examples, dict_iterate_examples, truthiness_examples, verbose_truthy_example]
def main():
    for example in examples:
        console.clear()
        print(create_source_output_table(example, console))

        is_not_last_item = example != examples[-1]
        if is_not_last_item:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()
