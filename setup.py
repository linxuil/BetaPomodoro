from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='<!prj_name!>',
     version='0.1',
     scripts=['<!prj_name!>.py'],
     author="linxuil",
     author_email="linxuil.g@gmail.com",
     description="Implementation <!prj_name!> function for python",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/linxuil/<!prj_name!>",
     packages=find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
    entry_points={
        'console_scripts': [
            '<!prj_name!>=console_scripts.main:main',
        ],
    },
 )
