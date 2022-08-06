"""This module provides the Weaviate tutorial CLI."""
# src/cli.py

from pathlib import Path
from typing import Optional
import json
import typer
import weaviate

client = weaviate.Client("http://localhost:8080")


app = typer.Typer()


@app.command()
def main():
    app()


@app.command()
def upload_schema(
    file_name: Optional[str] = typer.Option(
        default="data/schema.json",
        prompt=True,
        help="Enter the full path to your schema file",
    )
):
    typer.echo(f"Uploading schema...")
    try:
        with open(file_name, "r") as file:
            schema = json.load(file)
        client.schema.create(schema)
        typer.echo(f"Schema uploaded!")
    except Exception as e:
        print(f"An exception occured. Details: {e}")


@app.command()
def create_data():
    typer.echo("Creating data")


@app.command()
def batch_import_data(
    file_name: Optional[str] = typer.Option(
        default="data/publishing_data.csv",
        prompt=True,
        help="Enter the full path to the data file you want to populate your database with",
    )
):
    typer.echo("Batch importing data")
    try:
        data = pd.read_csv("data/publishing_data.csv", index_col=0)
    except Exception as e:
        print(f"An exception occured. Details: {e}")


@app.command()
def list_authors():
    typer.echo("Listing authors")


@app.command()
def list_posts():
    typer.echo("Listing posts")


@app.command()
def search_author():
    typer.echo("Searching for author")


@app.command()
def search_post():
    typer.echo("Searching for post")


@app.command()
def exit():
    typer.echo("Exiting the program!")
    raise typer.Exit()


if __name__ == "__main__":
    app()
