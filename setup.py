from setuptools import setup, find_packages

setup(
    name='my-ai-module',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'fastapi',
        'uvicorn',
        'joblib'
    ],
)
