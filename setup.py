# Import setup() and find_packages() from setuptools
# setup() is used to package the project
# find_packages() automatically finds all Python packages

from setuptools import setup, find_packages

# Import List for type hinting
from typing import List

# This line is present inside requirements.txt
# We don't want to install "-e ." as a dependency
HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements.txt file
    and returns a list of required packages.
    """

    requirements = []

    # Open requirements.txt
    with open(file_path) as file_obj:

        # Read all lines
        requirements = file_obj.readlines()

        # Remove newline characters (\n)
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove "-e ." if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# Package information
setup(

    # Name of the package
    name="MLproject",

    # Package version
    version="0.0.1",

    # Author name
    author="Rahul",

    # Author email
    author_email="rahulverma96259@gmail.com",

    # Automatically find all packages
    packages=find_packages(),

    # Install all dependencies from requirements.txt
    install_requires=get_requirements("requirements.txt")
)