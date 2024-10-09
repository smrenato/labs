from PIL import Image
from httpx import Client, AsyncClient
from parsel import Selector

sel = Selector()

# sync client
with Client() as client:
    result = client.get(url="www.google.com")
