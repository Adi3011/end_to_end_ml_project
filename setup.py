from setuptools import find_packages, setup
from typing import List

HYPEN_E  = "-e ."

def get_requirements(filePath:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(filePath)  as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        
        if HYPEN_E in requirements:
            requirements.remove(HYPEN_E)
            
    return requirements
        
    
setup(
    name = 'end_to_end_ml_project',
    version = '0.0.1',
    author = 'Aditya',
    author_email = '19bcs1084@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
    

)