import aiohttp
connector = aiohttp.BaseConnector(reuse_timeout=30, share_cookies=False, conn_timeout=None)
