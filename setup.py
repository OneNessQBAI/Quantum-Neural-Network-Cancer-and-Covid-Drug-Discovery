from setuptools import setup, find_packages

setup(
    name="quantum_medical",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'cirq-core>=1.1.0',
        'numpy>=1.24.0',
        'flask>=2.0.1',
    ],
)
