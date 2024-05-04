# Fort Wayne BSides 2024 - Leveling Up Your Scripting

This repository contains the presentation code for my Fort Wayne BSides 2024 presentation.

The code is broken into separate top level modules for each section. The modules are:

- `_1_language_features.py`: Python language features
- `_2_standardlib_example.py`: Python standard library examples
- `_3_dateparser_example.py`: Date parsing example
- `_4_rich_example.py`: Rich library example
- `_5_typehints_example.py`: Type hints example
- `_6_argparse_replace_example.py`: Argparse replacement example
- `_7_pyenv_pipenv.py`: Pyenv and Pipenv explanation
- `_9_end.py`: End of presentation
- `helpers.py`: Helper functions used in the presentation of the code and outputs

The dependencies for this project are in the Pipfile 

The most interesting code for the presentation and code display is in `helpers.py`. It uses the `rich` library and the python `inspect` standard library module to get function source code. It uses a `rich` `Console` object to display the code with syntax highlighting and line numbers, and capture all output. Currently this requires the console set up and a replacement of `print` in the source file in order for this to work. This could probably be improved to remove that constraint

For questions, please reach out via Github or via the FW BSides Discord server.
