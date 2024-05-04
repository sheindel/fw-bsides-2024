import os

from inspect import getsource
from typing import Callable

from rich import get_console
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.text import Text

def get_function_source(function: Callable, dedent: bool = True) -> str:
    # get the function text and split into lines
    lines = getsource(function).split(os.linesep)
    if dedent:
        # if we are dedenting, we are also removing the function definition
        lines = lines[1:]

        def dedent_line(line):
            if len(line) == 0:
                return line
            
            if line[0] == '\t':
                return line[1:]
            return line[4:]
        lines = map(dedent_line, lines)
                
    return os.linesep.join(lines)

def capture_function_output(function: Callable, console: Console) -> str:
    with console.capture() as capture:
        function()
    return capture.get()

def create_source_output_table(
        function: Callable, 
        console: Console, 
        space_output_lines: bool = False,
        print_source: bool = True,
        print_output: bool = True
) -> Table:
    source = get_function_source(function)
    output = capture_function_output(function, console)
    table = Table(title=function.__name__.replace("_", " "))
    if print_source:
        table.add_column("Source")
    if print_output:
        table.add_column("Output")
    if space_output_lines:
        output = os.linesep.join([f"{line}{os.linesep}" for line in output.split(os.linesep)])
    formatted_source = Syntax(source, lexer='python', line_numbers=True)
    output_text = Text.from_ansi(output)
    row = []
    if print_source:
        row.append(formatted_source)
    
    if print_output:
        row.append(output_text)

    table.add_row(*row)
    return table