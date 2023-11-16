import asyncio
from typing import Any, Coroutine


def async_sleep(seconds: int) -> Coroutine[Any, Any, None]:
    return asyncio.sleep(seconds)
