#!/usr/bin/env python3
"""measures the total execution time """


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """Returns float measure time """
    time1 = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed_time = time.perf_counter() - time1
    total_time = elapsed_time / n

    return total_time
