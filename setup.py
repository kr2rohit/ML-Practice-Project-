from setuptools import find_packages, setup
from typing import List
hyp_e_dot = '-e .' 
def get_requirements(file_path:str) -> List[str]:

    """this function will return a list of requriemnents"""
    requirements = []
    with open (file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [r.replace("\n"," ") for r in requirements]

        if hyp_e_dot in requirements:
            requirements.remove(hyp_e_dot)

        return requirements


setup(
name= 'mlproject',
version='0.0.1',
author= 'Kumar',
author_email='kumar6feb6639@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')


)