import httpx
timeout = httpx.Timeout(None, read_timeout=5.0, connect_timeout=5.0)
