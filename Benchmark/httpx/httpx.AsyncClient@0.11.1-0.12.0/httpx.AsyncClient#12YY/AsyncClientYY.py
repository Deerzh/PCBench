import httpx
from httpx import Auth, Timeout, PoolLimits, URL
client = httpx.AsyncClient(max_redirects=5)
