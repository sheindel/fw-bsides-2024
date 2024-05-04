########################################
# Main logic
########################################
def main_logic(square: int, verbosity: int):
    answer = square**2
    if verbosity == 2:
        print(f"the square of {square} equals {answer}")
    elif verbosity == 1:
        print(f"{square}^2 == {answer}")
    else:
        print(answer)


########################################
# Argparse version
########################################
import argparse
from enum import Enum

def argprase_square():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int)
    parser.add_argument("--verbosity", type=int)
    args = parser.parse_args()

    main_logic(args.square, args.verbosity)

########################################
# Typer version
########################################
import typer
from typing import Annotated

def typer_example():
    app = typer.Typer()
    
    @app.command()
    def typer_square(square: int, verbosity: int = 0):
        main_logic(square, verbosity)
    
    app()


def main():
    import os
    import inspect
    from rich import print
    from rich.syntax import Syntax
    from rich.table import Table

    argparse_source = inspect.getsource(argprase_square)
    argparse_source = os.linesep.join([line[4:] for line in argparse_source.split(os.linesep)[1:]])
    
    typer_source = inspect.getsource(typer_example)
    typer_source = os.linesep.join([line[4:] for line in typer_source.split(os.linesep)[1:]])

    table = Table(show_lines=True)
    table.add_column("Version")
    table.add_column("Source")
    table.add_row("argparse", Syntax(argparse_source, lexer='python'))
    table.add_row("typer", Syntax(typer_source, lexer='python'))
    print(table)

if __name__ == "__main__":
    main()