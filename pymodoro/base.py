"""project_template base module.

This is the principal module of the project_template project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""
import asyncio

import click


async def pomodoro_timer(minutes):
    """
    CLI-based Pomodoro Timer.

    Args:
        work (int): Duration of the work period in minutes.
        break_time (int): Duration of the break time in minutes.
    """
    click.echo(f"Start Pomodoro Timer for {minutes} minutes.")
    await asyncio.sleep(minutes * 60)
    click.echo(f"Pomodoro Timer for {minutes} minutes is complete!")


async def pomodoro_cycle(work, break_time):
    """
    Asynchronous function representing a cycle of Pomodoro timer and break time.

    Args:
        work (int): Duration of the work period in minutes.
        break_time (int): Duration of the break time in minutes.
    """
    while True:
        await pomodoro_timer(work)
        click.echo(f"Take a {break_time}-minute break.")
        await asyncio.sleep(break_time * 60)
