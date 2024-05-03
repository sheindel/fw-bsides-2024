from rich.console import Console

console = Console()
print = console.print

def example_simple_console():
    # Normally you would just use this line 
    #from rich import print
    print("Hello, world!")
    print("Hello, [bold magenta]World[/bold magenta]!")
    print("Hello, 99 worlds!")
    print({"Hello": "world!", "Number": 99})
    print(["Hello", "world!", 99])
    print(["Lots of items"]*10)

def example_rich_advanced_table():
    from rich.table import Table
    user_data = [
        ["Alice", 24],
        ["Bob", 19],
        ["Charlie", 30],
        ["David", 40],
    ]
    table = Table(title="User Info")
    table.add_column("Name")
    table.add_column("Age")
    for user in user_data:
        table.add_row(user[0], str(user[1]))
    
    print(table)


def example_rich_advanced_tree():
    from rich.tree import Tree

    tree = Tree("example")
    tree.add("hello").add("world").add("!")

    foo = tree.add("foo")
    foo.add("bar")
    foo.add("baz")
    
    print(tree)


def example_inspect():
    from rich import inspect
    my_list = [1, 2, 3, 4]
    print('inspect(my_list)')
    inspect(my_list, console=console)
    print('inspect(my_list, methods=True)')
    inspect(my_list, console=console, methods=True)
    print('inspect(my_list, all=True)')
    inspect(my_list, console=console, all=True)


def example_traceback():
    my_number = 2
    my_string = "world"
    
    # This line will print the output directly if the program crashes
    #from rich.traceback import install
    #install(show_locals=True)
    #print(my_number + my_string)

    try:
        print(my_number + my_string)
    except Exception as e:
        console.print_exception(show_locals=False)
    
    try:
        print(my_number + my_string)
    except Exception as e:
        console.print_exception(show_locals=True)

def main():
    import inspect
    from rich.table import Table
    from rich.console import Console
    from rich.text import Text
    from rich.syntax import Syntax
    import os
    examples = [example_simple_console, example_rich_advanced_table, example_inspect, example_traceback]
    for example in examples:
        console.clear()
        lines = inspect.getsource(example)
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

if __name__ == '__main__':
    main()