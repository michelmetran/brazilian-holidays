"""
Setup
"""

from setuptools import find_packages, setup
from brazilian_holidays import __version__

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

requirements = []
with open('requirements.txt', 'r', encoding='utf-8') as f:
    for line in f:
        li = line.strip()
        if not li.startswith('#'):
            requirements.append(line.rstrip())
            print('6666' * 100)
            print(requirements)


setup(
    name='brazilian_holidays',
    version=__version__,
    author='Michel Metran',
    author_email='michelmetran@gmail.com',
    description='Brazilian Holidays',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/michelmetran/brazilian-holidays',
    keywords='python, dates, holidays, brazil, feriados',
    # Python and Packages
    python_requires='>=3.10',
    install_requires=requirements,
    # Classificação
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese',
        'Intended Audience :: Developers',
    ],
    # Entry
    # Quando são diversos módulos...
    packages=find_packages(where='.'),
    # Dados
    # include_package_data=True,
    # package_data={'': ['data/output/geo/*.7z']},
)
