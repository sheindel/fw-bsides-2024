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
from pathlib import Path
import typing

from helpers import create_source_output_table, get_function_source

def argparse_example():
    parser = argparse.ArgumentParser()
    parser.add_argument("square", type=int)
    parser.add_argument("--verbosity", type=int)
    args = parser.parse_args()

    main_logic(args.square, args.verbosity)

########################################
# Typer version
########################################
import typer
from typing import Annotated, Optional

def typer_example():
    app = typer.Typer()
    
    @app.command()
    def typer_square(square: int, verbosity: int = 0):
        main_logic(square, verbosity)
    
    app()



def typer_advanced():
    # Thanks to revsh3ll (Matt Raufper) for the inspiration! 
    app = typer.Typer()

    class PasswordOrHashChoice(str, Enum):
        password = "pw"
        ntlm = "ntlm"

    DEFAULT_OUTPUT_DIRECTORY = './'
    DEFAULT_WORDLIST_PATH = '/usr/share/wordlists/rockyou.txt'

    @app.command()
    def main(
        domain_controller_ip: str,
        domain_name: str, 
        target_ips: Annotated[typer.FileText, typer.Argument(exists=True, dir_okay=False)], 
        active_directory_account: str, 
        flag_password_or_ntlm: Annotated[PasswordOrHashChoice, typer.Argument()],
        password_or_ntlm_hash: str, 
        local_auth: bool = False, 
        output_directory: Annotated[Path, typer.Option(file_okay = False)] = Path(DEFAULT_OUTPUT_DIRECTORY), 
        wordlist_path: Annotated[Path, typer.Option(exists=True, dir_okay=False)] = Path(DEFAULT_WORDLIST_PATH), 
        rule_path: Annotated[Optional[typer.FileText], typer.Option(exists=True, dir_okay=False)] = None,
    ):
        # logic
        pass
    
    app()

def main():
    from rich.console import Console
    from rich.syntax import Syntax
    from rich.table import Table

    console = Console()
    print = console.print

    # typer_advanced()

    table = Table(show_lines=True)
    table.add_column("Version")
    table.add_column("Source")
    # table.add_row("argparse", Syntax(argparse_source, lexer='python'))
    # table.add_row("typer", Syntax(typer_source, lexer='python'))
    table.add_row("argparse", Syntax(get_function_source(argparse_example), lexer='python'))
    table.add_row("typer", Syntax(get_function_source(typer_example), lexer='python'))
    print(table)

    input("Press Enter to continue to the next example...")

    print(Syntax(get_function_source(typer_advanced), lexer='python'))




if __name__ == "__main__":
    main()