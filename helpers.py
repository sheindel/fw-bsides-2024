import os

from inspect import getsource
from typing import Callable

from rich import get_console
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.text import Text

def get_function_source(function: Callable, dedent: bool = True):
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

def capture_function_output(function: Callable, console: Console):
    with console.capture() as capture:
        function()
    return capture.get()

def create_source_output_table(function: Callable, console: Console):
    source = get_function_source(function)
    output = capture_function_output(function, console)
    table = Table(title=function.__name__.replace("_", " "))
    table.add_column("Source")
    table.add_column("Output")
    formatted_source = Syntax(source, lexer='python', line_numbers=True)
    output_text = Text.from_ansi(output)
    table.add_row(formatted_source, output_text)
    return table