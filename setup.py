""" 
This is basically representing configuration, requirements and metadata of the whole project.
"""

from setuptools import find_packages, setup
from typing import List

def get_requirements()-> List[str]:
    """
    This file defines the configuration, metadata, and dependencies
    for the entire project.
    """
    requirements:List[str] = []
    
    with open("requirements.txt", 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            require = line.strip()
            if require and require!="-e .":
                requirements.append(require)
    
    return requirements

setup(
    name= "Network_Security",
    version= "0.0.1",
    author= "Amber_Khan",
    packages= find_packages(),
    install_requires= get_requirements()
)
