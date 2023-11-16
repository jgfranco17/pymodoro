"""Pymodoro base module."""
import asyncio

import click

from .timing import async_sleep


async def pomodoro_timer(minutes):
    """
    CLI-based Pomodoro Timer.

    Args:
        work (int): Duration of the work period in minutes.
        break_time (int): Duration of the break time in minutes.
    """
    click.echo(f"Start Pomodoro Timer for {minutes} minutes.")
    await async_sleep(minutes * 60)
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
        await async_sleep(break_time * 60)
