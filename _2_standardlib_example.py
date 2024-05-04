from rich.console import Console
from helpers import create_source_output_table

console = Console()
print = console.print


def path_examples():
    import os
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
    import os
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

examples = [path_examples, linesep_examples, glob_example, random_examples]
def main():
    for example in examples:
        console.clear()
        print(create_source_output_table(example, console))

        is_not_last_item = example != examples[-1]
        if is_not_last_item:
            input("Press Enter to continue to the next example...")


if __name__ == '__main__':
    main()