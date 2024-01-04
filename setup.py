from setuptools import setup, find_packages


setup(
    name="game",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "black==23.12.1",
        "pytest==7.4.3",
        "qiskit==0.45.1",
        "qiskit-aer==0.13.1",
        "streamlit==1.29.0",
    ],
)
