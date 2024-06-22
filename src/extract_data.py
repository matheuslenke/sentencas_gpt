from bs4 import BeautifulSoup
import asyncio
import aiohttp
import os

# Configuring concurrency of asyncio
semaphore = asyncio.Semaphore(8)
download_url = "http://eliasdeoliveira.com.br/seminars/"


async def download_file(path, file_url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(file_url) as response:
            if response.status == 200:
                with open(path + filename, "wb") as file:
                    async for chunk in response.content.iter_chunked(1024):
                        file.write(chunk)
                print("File downloaded successfully.")
            else:
                print("Failed to download the file.")

async def download_page(name, url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                soup = BeautifulSoup(await response.text(), "html.parser")
                table = soup.find("table")
                rows = table.find_all("tr")
                for row in rows:
                    cells = row.find_all("td")
                    if len(cells) > 0:
                        link = cells[0].find("a")
                        if link:
                            href = link.get("href")
                            file_url = download_url + href[2:]
                            print(file_url)
                            await download_file(f"data/{name}/", file_url, href.split("/")[-1])
            else:
                print("Failed to retrieve the webpage.")


async def extract_data():
    urls = [
        ("roubo_simples", "http://eliasdeoliveira.com.br/seminars/pagina-rouboSimples.html"),
        ("roubo_majorado", "http://eliasdeoliveira.com.br/seminars/pagina-rouboMajorado.html"),
        ("furto_simples", "http://eliasdeoliveira.com.br/seminars/pagina-furtoSimples.html"),
        ("furto_qualificado", "http://eliasdeoliveira.com.br/seminars/pagina-furtoQualificado.html")
    ]

    for (name, url) in urls:
        # Create directory with name
        os.makedirs(f"data/{name}", exist_ok=True)
        try:
            await download_page(name, url)
        except aiohttp.ClientError as e:
            print(f"Network error: {e}")
        except Exception as e:  # Catching a broad exception for now
            print(f"Unexpected error: {e}")
