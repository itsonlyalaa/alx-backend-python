#!/usr/bin/env python3
"""takes in an integer argument, and waits for random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Waits for random delay between 0 and max_delay"""
    Delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(Delay)
    return Delay
