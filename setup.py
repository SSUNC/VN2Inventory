#responsible to install required packages
#helps to build our application as a package

from setuptools import find_packages,setup
#setup will provide information about the project

Hypen_E_Dot='-e .' 
#function to extract the packages from the requirement.txt
def get_requirements(file):
    '''
    function should return a list because the install_requires required list of packages 
    which needs to be installed

    
    '''
    requirements=[]

    with open(file) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('/n','')for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
            
    return requirements
    



setup(
    name='VN2 Inventory',
    version='1.0',
    author='sundar',
    author_email='sunc91@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
