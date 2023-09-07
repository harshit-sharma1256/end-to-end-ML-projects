from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT  = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(name="First E2E project",
      version='1.0.0',
      author="Harshit Sharma",
      author_email="harshit2531937@gmail.com",
      maintainer="Harshit Sharma",
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
      )
