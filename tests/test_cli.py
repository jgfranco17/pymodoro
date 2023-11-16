import pytest

from pymodoro.base import pomodoro_cycle, pomodoro_timer
from pymodoro.cli import pomodoro


@pytest.mark.asyncio
async def test_pomodoro_timer(capfd, mocker):
    minutes = 1
    mocker.patch("pymodoro.timing.async_sleep")
    await pomodoro_timer(minutes)
    out, _ = capfd.readouterr()
    assert f"Start Pomodoro Timer for {minutes} minutes." in out
    assert f"Pomodoro Timer for {minutes} minutes is complete!" in out


@pytest.mark.asyncio
async def test_pomodoro_cycle(capfd):
    minutes_work = 1
    minutes_break = 1
    await pomodoro_cycle(minutes_work, minutes_break)
    out, _ = capfd.readouterr()
    assert f"Start Pomodoro Timer for {minutes_work} minutes." in out
    assert f"Take a {minutes_break}-minute break." in out


@pytest.mark.asyncio
async def test_pomodoro_command_default_settings(runner, capfd):
    result = runner.invoke(pomodoro)
    out, _ = capfd.readouterr()
    assert "Start Pomodoro Timer for 25 minutes." in out
    assert "Take a 5-minute break." in out
    assert result.exit_code == 0


@pytest.mark.asyncio
async def test_pomodoro_command_custom_durations(runner, capfd):
    result = runner.invoke(pomodoro, ["--work", "30", "--break-time", "10"])
    out, _ = capfd.readouterr()
    assert "Start Pomodoro Timer for 30 minutes." in out
    assert "Take a 10-minute break." in out
    assert result.exit_code == 0
