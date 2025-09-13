'''
This setup.py file is an essential part of packaging and 
distributing python projects. It is use by setuptools (or disutils 
in older Python versions) to define the configuration of your project,
such as its metadata, dependancies and more.
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    req_list:List[str] = []
    try:
        with open('req.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                req = line.strip()  ## .strip() remove every empty spaces from every line
                #ignore empty lines and -e .
                if req and req != "-e .":
                    req_list.append(req)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return req_list

setup(
    name = "NetworkSecurity",
    version="0.0.1",
    author= "Tusar Debnath",
    author_email= "tushardebnath2000@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)
# print(get_requirements())