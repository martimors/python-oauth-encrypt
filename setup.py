import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oauth-encrypt",
    version="0.0.2",
    author="Martin Morset",
    author_email="mmorset@gmail.com",
    description="A simple package to use oauth and persist tokens between runs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dingobar/python-oauth-encrypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)