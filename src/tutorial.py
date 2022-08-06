# src/tutorial.py

from enum import Enum
from pathlib import Path
from typing import Optional
import json
import typer
import weaviate
import pandas as pd
from rich import print_json
from pprint import pprint

client = weaviate.Client("http://localhost:8080")

app = typer.Typer()


@app.command()
def list_authors():
    query = """
    {
       Get {

         Author {

           name
           wrotePosts {
  	     ... on BlogPost {
	     title
	     body
	   }
        }

      }
     }
    }"""
    result = client.query.raw(query)
    print_json(data=result)


@app.command()
def list_posts():
    query = """

   {

      Get {

        BlogPost {

          title

          body

          authoredBy {

            ... on Author {

              name

            }

          }

        }

      }

    }

    """
    result = client.query.raw(query)
    print_json(data=result)


@app.command()
def search_post():
    post = typer.prompt("Enter the blog post search term: ")
    query = f"""
        {{
        Get {{
          BlogPost (where: {{
            operator: Like,
            valueText: "{post}",
            path: ["body"]
          }}) {{
            title
            body
            authoredBy {{
              ... on Author {{
                name
              }}
            }}
          }}
        }}
      }}
    """
    typer.echo(f"Status: Searching for {post!r} in blog posts")
    result = client.query.raw(query)
    print_json(data=result)


@app.command()
def search_author():
    author = typer.prompt("Enter the author's name")
    query = f"""
        {{
        Get {{
          Author (where: {{
            operator: Like,
            valueString: "{author}",
            path: ["name"]
          }}) {{
            name
            wrotePosts {{
              ... on BlogPost {{
                title
	        body
              }}
            }}
          }}
        }}
      }}
    """
    typer.echo(f"Status: Searching for {author!r} in authors")
    result = client.query.raw(query)
    print_json(data=result)


if __name__ == "__main__":
    app()
