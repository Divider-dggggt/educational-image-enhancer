from setuptools import setup, find_packages

setup(
    name="ur_material",            
    version="0.1.1",               
    packages=find_packages(where="src"), 
    package_dir={"": "src"},      
    install_requires=[        
        "numpy==1.26.4",
        "augraphy==8.2.6",
        "imgaug==0.4.0",
        "requests>=2.24.0"
    ],
    include_package_data=True,       
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=open('README.md').read(),  
    long_description_content_type="text/markdown",  
)