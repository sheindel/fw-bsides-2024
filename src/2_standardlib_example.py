import os
from rich.console import Console
from inspect import getsource
from rich.table import Table
from rich.syntax import Syntax
from rich.text import Text

console = Console()
print = console.print


def path_examples():
    def path_functions(path: str, file: str):
        print(os.path.join(path, file))
    
    path_functions("C:/Users", "example.txt")
    path_functions("C:", "example.txt")
    path_functions("/home/stephenheindel", "example.txt")
    path_functions("/home/stephenheindel/", "example.txt")
    path_functions("/", "example.txt")
    path_functions("./", "example.txt")
    path_functions("/home/stephenheindel", "relative/example2.txt")


def linesep_examples():
    print("This is a line")
    print("This is another line")
    print(f"Line 1 {os.linesep}Line 2 {os.linesep}Line 3")


def random_examples():
    import random

    print(random.random())
    print(random.randint(1, 10))
    print(random.uniform(1, 10))

    my_list = [1, 2, 3, 4, 5]
    print(random.choice(my_list))

    random.shuffle(my_list)
    print(my_list)


def glob_example():
    import glob
    print(glob.glob("*.py"))

    search = "parse"
    print(glob.glob(f"*{search}*.py"))

def main():
    examples = [path_examples, linesep_examples, glob_example, random_examples]
    for example in examples:
        console.clear()
        source = getsource(example)
        # remove the first line
        # dedent all other lines by 4 spaces
        source = os.linesep.join([line[4:] for line in source.split(os.linesep)[1:]])

        table = Table(title=example.__name__.replace("_", " "))
        table.add_column("Source")
        output = table.add_column("Output")
        with console.capture() as capture:
            example()
        output = capture.get()
        table.add_row(Syntax(source, lexer='python'), Text.from_ansi(output))
        console.print(table)
        # if not last item, wait for next
        if example != examples[-1]:
            input("Press Enter to continue to the next example...")

    # for example in examples:
    #     print(f"Running example: {example.__name__}")
    #     example()
    #     print("\n")
    #     input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()