import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pcan_wrapper',
    version='0.0.3',
    author='igrekus',
    author_email='',
    description='Simple wrapper around PEAK-System Technik GmbH CAN SDK',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/igrekus/pcan_wrapper',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    include_package_data=True
)
