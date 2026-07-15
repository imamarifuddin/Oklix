import time
from fastapi import Request

async def log_requests(request: Request, call_next):
    start = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start

    print(
        f"{request.method} {request.url.path} {duration:.3f}s"
    )

    return response