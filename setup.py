from setuptools import setup, find_packages

setup(
    name='learn_python',
    packages=find_packages(),
    version='0.1',
    description='A Python GitHub repository for practicing katas.',
    author='Alexander DeJesus',
    author_email='alexander.dejesus.1985@gmail.com',
    url='https://github.com/libraryman85/learn_python',
    keywords=['libraryman85', 'python', 'kata',],
    install_requires=[
        'pytest',
        'flask',
        'flask-runner',
        'flask-script'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
)