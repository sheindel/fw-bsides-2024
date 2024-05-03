import random
from rich import print
from rich.tree import Tree
import inspect

def add_standard_environment(branch: Tree, version: str):
    version = ".".join(version.split(".")[:2])
    binaries = branch.add("[blue]bin[/blue] (executables)")
    binaries.add(f"[cyan]python -> python{version}[/cyan] (python.exe)")
    binaries.add(f"[cyan]python3 -> python{version}[/cyan] (python3.exe)")
    binaries.add(f"[green]python{version}[/green] (python{version}.exe)")
    binaries.add("[green]pip[/green] (pip.exe)")
    binaries.add("...binaries bundled installed related by pip packages")

    lib = branch.add("[blue]lib[/blue] (standard library, etc.)")
    lib_version = lib.add(f'[blue]python{version}[/blue]')
    site_packages = lib_version.add("[blue]site-packages[/blue]")
    site_packages.add("...everything you install with [green]pip[/green]")
    
    return [binaries, lib, site_packages]

def python_standard_environment():
    tree = Tree("standard python environment")
    add_standard_environment(tree, "3.9.5")

    return tree

def pyenv_version_management():
    tree = Tree("pyenv version management")
    versions = tree.add("versions")
    version_strings = ["3.9.5", "3.8.10", "3.7.10"]
    for version in version_strings:
        version_tree = versions.add(version)
        add_standard_environment(version_tree, version)

    global_versions = tree.add("global versions")
    global_version = global_versions.add("3.9.5")
    add_standard_environment(global_version, "3.9.5")

    return tree

def pipenv_virtualenv():
    tree = Tree("pipenv virtualenv")
    virtualenv = tree.add("virtualenv")
    add_standard_environment(virtualenv, "3.9.5")

    return tree


def pyenv_pipenv_version_management():
    tree = Tree("pyenv version management")
    versions = tree.add("versions")
    version_strings = ["3.9.5", "3.8.10", "3.7.10"]
    for version in version_strings:
        version_tree = versions.add(version)
        add_standard_environment(version_tree, version)

    global_versions = tree.add("global versions")
    version_tree = global_versions.add("3.9.5")
    add_standard_environment(version_tree, "3.9.5")


    projects = tree.add("projects")
    project_strings = ["project1", "project2", "project3"]
    for project in project_strings:
        project_tree = projects.add(project)
        version = random.choice(version_strings)
        version_tree = project_tree.add(version)
        add_standard_environment(version_tree, version)

    return tree


if __name__ == "__main__":
    from rich.panel import Panel
    from rich.table import Table
    from rich.color import ANSI_COLOR_NAMES
    examples = [python_standard_environment, pyenv_version_management, pipenv_virtualenv, pyenv_pipenv_version_management]
    for example in examples:
        lines = inspect.getsource(example)
        print("\n")
        table = Table(title=example.__name__.replace("_", " "))
        table.add_column("Source")
        table.add_column("Output")
        table.add_row(lines, Panel(example(), title=example.__name__.replace("_", " "), border_style=random.choice([*ANSI_COLOR_NAMES.keys()])))
        #print(Panel(example(), title=example.__name__.replace("_", " "), border_style=random.choice([*ANSI_COLOR_NAMES.keys()])))
        print(table)
        print("\n")
        input("Press Enter to continue...")