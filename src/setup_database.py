# src/setup_database.py

# src/cli.py

from enum import Enum
from pathlib import Path
from typing import Optional
import json
import typer
import weaviate
from weaviate.util import generate_uuid5
import pandas as pd
import csv
from faker import Faker
from rich.progress import track

from data_generator import generate_data as gd

client = weaviate.Client("http://localhost:8080")
client.batch.configure(batch_size=100, dynamic=False, timeout_retries=3, callback=None)

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


def add_blog_post(batch, blog_post_data):
    blog_post_object = {
        "title": blog_post_data.title,
        "body": blog_post_data.body.replace("\n", ""),
    }
    blog_post_uuid = blog_post_data.uuid
    # add article to the object batch request
    batch.add_data_object(
        data_object=blog_post_object, class_name="BlogPost", uuid=blog_post_uuid
    )
    return blog_post_uuid


def add_author(batch, name, created_authors):
    if name in created_authors:
        return created_authors[name]
    author_uuid = generate_uuid5(name)
    batch.add_data_object(
        data_object={"name": name}, uuid=author_uuid, class_name="Author"
    )
    created_authors[name] = author_uuid
    return author_uuid


def add_cross_references(batch, blog_post_uuid, author_uuid):
    batch.add_reference(
        from_object_uuid=author_uuid,
        from_object_class_name="Author",
        from_property_name="wrotePosts",
        to_object_uuid=blog_post_uuid,
        to_object_class_name="BlogPost",
    )
    batch.add_reference(
        from_object_uuid=blog_post_uuid,
        from_object_class_name="BlogPost",
        from_property_name="authoredBy",
        to_object_uuid=author_uuid,
        to_object_class_name="Author",
    )


@app.command()
def batch_import_data(
    file_name: Optional[str] = typer.Option(
        default="data/publishing_data.csv",
        prompt=True,
        help="Enter the full path to the data file you want to populate your database with",
    )
):
    typer.echo("Status: Batch importing data...")
    created_authors = {}
    count = 0
    try:
        bulk_data = pd.read_csv("data/publishing_data.csv")
        with client.batch as batch:
            for index, row in track(bulk_data.iterrows()):
                blog_post_uuid = add_blog_post(batch, blog_post_data=row)
                author_uuid = add_author(batch, row.author, created_authors)
                add_cross_references(
                    batch, blog_post_uuid=blog_post_uuid, author_uuid=author_uuid
                )
                count += 1
                if index % 50 == 0:
                    batch.create_objects()
                    batch.create_references()
        typer.echo(f"Status: {count} Data data records were imported!")
    except Exception as e:
        print(f"An exception occured. Details: {e}")


if __name__ == "__main__":
    app()
