from setuptools import setup

py_modules = ["fourth_down_api"]

setup(
    packages=py_modules,
    name="fourth_down_api",
    author="Lee and stolen Titusz code",
    version="1.0.0",
    description="Fourth down API client",
    install_requires=[
        "requests"
    ])
