from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="simple_crud",
    version="0.1.0",
    author="Vitor Domingues",
    author_email="vdmrvitor@gmail.com",
    description="Package for CRUD software prototyping.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simple_crud",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)