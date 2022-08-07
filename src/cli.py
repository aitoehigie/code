"""This module provides the Weaviate tutorial CLI."""
# src/cli.py
from subprocess import call

import typer
from rich import print
from rich.console import Console
from rich.table import Table

import setup_database
import tutorial

app = typer.Typer()
app.add_typer(setup_database.app, name="setup-database")
app.add_typer(tutorial.app, name="tutorial")

menu_options = {
    1: setup_database.generate_data,
    2: lambda: call(["weaviate_tutorial", "setup-database", "upload-schema"]),
    3: setup_database.add_single_data,
    4: setup_database.batch_import_data,
    5: tutorial.list_authors,
    6: tutorial.list_posts,
    7: tutorial.search_author,
    8: tutorial.search_post,
}


def print_menu_options():
    print(
        "Enter the following commands in the displayed order to set up the test database and to be able to query it"
    )
    print(f"[bold purple]{'-' *  79}[/bold purple]")
    print("[bold white]Setup database[/bold white]")
    print("Enter [bold yellow]'1'[/bold yellow]: To generate test data")
    print("Enter [bold yellow]'2'[/bold yellow]: To upload the schema")
    print("Enter [bold yellow]'3'[/bold yellow]: To import a single data record")
    print("Enter [bold yellow]'4'[/bold yellow]: To import bulk test data records")
    print(f"[bold purple]{'*' *  79}[/bold purple]")
    print("[bold white]Tutorial[/bold white]")
    print("Enter [bold yellow]'5'[/bold yellow]: To list all authors")
    print("Enter [bold yellow]'6'[/bold yellow]: To list all blog posts")
    print("Enter [bold yellow]'7'[/bold yellow]: To search for authors")
    print("Enter [bold yellow]'8'[/bold yellow]: To search for blog posts")
    print("Enter [bold yellow]0[/bold yellow]: To exit the application")
    print(f"[bold purple]{'*' *  79}[/bold purple]")


@app.command()
def menu():
    print(f"[bold purple]{'*' *  79}[/bold purple]")
    print(
        ":boom: [bold green]:partying_face: Welcome to the Getting Started with :computer: Weaviate Tutorial :book: [/bold green] :boom:"
    )
    print(f"[bold purple]{'*' *  79}[/bold purple]")
    while True:
        print_menu_options()
        try:
            option = int(input("Enter your choice: "))
        except:
            print("[bold red]Wrong input. Please enter a number...[/bold red]")
        if option == 0:
            print("[bold orange]Exiting the program now![/bold orange]")
            raise typer.Exit()
        else:
            try:
                menu_options.get(option)()
            except:
                print(
                    "[bold red]Wrong input. Please enter a number from 0 to 8[/bold red]"
                )


@app.command()
def exit():
    typer.echo("Exiting the program!")
    raise typer.Exit()


if __name__ == "__main__":
    app()
