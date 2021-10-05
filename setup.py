import pathlib
from setuptools import setup


ROOT = pathlib.Path(__file__).parent

README = (ROOT / "README.md").read_text()


setup(
    name="mysql-logger",
    version="0.0.1",
    description="A simple logger class for MySQL and MariaDB",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ghiandFe/MySQLLogger",
    author="ghiandFe",
    author_email="info.fgsoftware@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["mysql_logger"],
    install_requires=["asyncio", "aiomysql"],
)