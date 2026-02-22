from setuptools import setup, find_packages

setup(
    name="valorant.py",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.8.0"
    ],
    author="Astro",
    description="SDK para extração de dados do Valorant via scraping",
    keywords="valorant, sdk, aiohttp",
    python_requires=">=3.8",
)
