from rich.console import Console

from helpers import create_source_output_table

console = Console()
print = console.print

def string_func(string: str) -> str:
    return "Your string: " + string


def int_func(integer: int) -> int:
    return integer + 42

def ex1():
    def my_string_func(my_string: str) -> str:
        return "Your string: " + my_string

    def my_int_func(my_number: int) -> int:
        return my_number + 42

    print(my_string_func("Hello, world!"))
    print(my_int_func(100))
    
    # this produces an error in an IDE using a python language server because 
    # we are passing an int to a function that expects a string
    try:
        print(my_string_func(100))
    except Exception as e:
        print(e)
    

def ex2():
    my_string_var = "Hello, world!"
    my_explicit_string_var: str = "Hello, typed world!"
    are_types_equal = type(my_string_var) == type(my_explicit_string_var)
    print(f'Types equal? {are_types_equal}')

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
    dictionary: dict[str | int, str | int] = {
        "Hello": "world!", 
        "Goodbye": "world!", 
        "A number": 100,
        3: "Another number",
    }

    # This is typed as unknown because of the mixed values types in the dictionary
    any_value_from_the_dictionary = dictionary["Hello"]


def main():
    examples = [
        ex1, 
        # ex2
    ]
    for example in examples:
        console.clear()
        print(create_source_output_table(example, console))

        is_not_last_item = example != examples[-1]
        if is_not_last_item:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()