from setuptools import setup, find_packages
from os.path import exists  # Add this import

setup(
    name="unittesting",
    version="0.1.0",
    packages=find_packages(),
    
    # Dependencies
    install_requires=[
        "pytest>=7.0.0",
    ],
    
    # Metadata
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple person management package",
    long_description=open("README.md").read() if exists("README.md") else "",
    long_description_content_type="text/markdown",
    
    # Package Discovery
    package_dir={"": "src"} if exists("src") else {},  # If using src layout
    
    # Python version requirement
    python_requires=">=3.7",
)