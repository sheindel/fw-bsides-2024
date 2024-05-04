import typer
import os

app = typer.Typer()

@app.command()
def ping_basic(destination: str):
    typer.echo(f"Pinging {destination}")
    os.system(f"ping {destination}")


@app.command()
def ping_count(destination: str, count: int = 4):
    typer.echo(f"Pinging {destination} {count} times")
    os.system(f"ping -c {count} {destination}")


@app.command()
def ping_continuous(destination: str, continuous: bool = True):
    typer.echo(f"Pinging {destination} continuously")
    os.system(f"ping {'' if continuous else '-c 4'} {destination}")


if __name__ == "__main__":
    app()

