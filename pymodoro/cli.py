"""CLI interface for pymodoro project."""
import asyncio

import click

from pymodoro.base import pomodoro_cycle


@click.command()
@click.option("--work", default=25, help="Duration of the work period in minutes")
@click.option("--break-time", default=5, help="Duration of the break time in minutes")
def pomodoro(work, break_time):
    """CLI-based Pomodoro Timer."""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(pomodoro_cycle(work, break_time))


def main():  # pragma: no cover
    """Execute main functionality.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    print("This will do something")
