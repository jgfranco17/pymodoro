"""Python setup.py for api package."""
import io
import os

from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Safely read file content."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    """Read requirements file."""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="home-api",
    version=read("api", "VERSION"),
    description="Awesome api created by jgfranco17",
    url="https://github.com/jgfranco17/home-api/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jgfranco17",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={"console_scripts": ["api = api.__main__:main"]},
    extras_require={"test": read_requirements("requirements-test.txt")},
)
