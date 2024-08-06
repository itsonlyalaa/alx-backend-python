#!/usr/bin/env python3
""" takes in 2 int arguments, and waits for random delay """

import asyncio
import random
from typing import List
wait_random = __import__('3-tasks').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """return the list of all the delays"""
    Delays_list: List[float] = []
    Tasks_list: List = []

    for x in range(n):
        Tasks_list.append(wait_random(max_delay))

    for task in asyncio.as_completed((Tasks_list)):
        delay = await task
        Delays_list.append(delay)

    return Delays_list
