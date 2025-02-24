import pathlib

from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="didcomm",
    version="0.1.0",
    description="DIDComm for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sicpa-dlab/didcomm-python",
    author="",
    author_email="",
    license="Apache-2.0",
    python_requires=">=3.7",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["didcomm"],
    install_requires=[
        "Authlib@git+https://github.com/sicpa-dlab/authlib.git@json-serialization-and-multi-recipient",
        "pycryptodomex>=3.10,<4"
    ],
    extras_require={"tests": ["pytest", "pytest-asyncio"]}
)
