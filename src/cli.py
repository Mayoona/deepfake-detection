# cli.py

import typer
from pathlib import Path

app = typer.Typer()

@app.command()
def process_dir(dir_path: Path):
    """
    Process all files in a directory.
    """
    if not dir_path.exists() or not dir_path.is_dir():
        typer.echo(f"❌ The path '{dir_path}' is not a valid directory.")
        raise typer.Exit(code=1)

    typer.echo(f"📂 Processing directory: {dir_path}")
    files = list(dir_path.glob("*"))

    if not files:
        typer.echo("⚠️ No files found.")
    else:
        for file in files:
            typer.echo(f"  - {file.name}")

if __name__ == "__main__":
    app()
