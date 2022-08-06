# src/setup_database.py

# src/cli.py

from enum import Enum
from pathlib import Path
from typing import Optional
import json
import typer
import weaviate
import pandas as pd
from faker import Faker

from data_generator import generate_data as gd

client = weaviate.Client("http://localhost:8080")

fake = Faker()

app = typer.Typer()


@app.command()
def generate_data():
    typer.echo("Status: Generating data...")
    gd()
    typer.echo("Status: Generated data successfully!")


@app.command()
def upload_schema(
    file_name: Optional[str] = typer.Option(
        default="data/schema.json",
        prompt=True,
        help="Enter the full path to your schema file",
    )
):
    typer.echo(f"Status:Uploading schema...")
    try:
        with open(file_name, "r") as file:
            schema = json.load(file)
        client.schema.create(schema)
        typer.echo(f"Status: Schema uploaded!")
    except Exception as e:
        print(f"An exception occured. Details: {e}")


@app.command()
def add_single_data():
    typer.echo("Status: importing a single record...")
    blog_post_data = {
        "title": fake.sentence(),
        "body": fake.paragraph(50).replace("\n", ", "),
    }
    blog_post_uuid = client.data_object.create(
        data_object=blog_post_data, class_name="BlogPost"
    )
    author_data = {"name": fake.name()}
    author_uuid = client.data_object.create(
        data_object=author_data, class_name="Author"
    )
    client.data_object.reference.add(
        from_uuid=author_uuid,
        from_class_name="Author",
        from_property_name="wrotePosts",
        to_uuid=blog_post_uuid,
        to_class_name="BlogPost",
    )
    client.data_object.reference.add(
        from_uuid=blog_post_uuid,
        from_class_name="BlogPost",
        from_property_name="authoredBy",
        to_uuid=author_uuid,
        to_class_name="Author",
    )
    typer.echo("Status: Single record imported successfully!")


@app.command()
def batch_import_data(
    file_name: Optional[str] = typer.Option(
        default="data/publishing_data.csv",
        prompt=True,
        help="Enter the full path to the data file you want to populate your database with",
    )
):
    typer.echo("Batch importing data...")
    try:
        data = pd.read_csv("data/publishing_data.csv", index_col=0)
        typer.echo("Data imported!")
    except Exception as e:
        print(f"An exception occured. Details: {e}")


if __name__ == "__main__":
    app()
