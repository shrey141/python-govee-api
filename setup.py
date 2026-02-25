import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

INSTALL_REQUIRES = [
    "aiohttp>=3.7.1",
    "certifi>=2021.10.8",
    "dacite>=1.7.0",
    "events>=0.3",
]

setuptools.setup(
    name="govee_api",
    version="0.2.3",
    author="@shrey141",
    description="Python client for the Govee API to control LED strips and bulbs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shrey141/python-govee-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    install_requires=INSTALL_REQUIRES,
)
