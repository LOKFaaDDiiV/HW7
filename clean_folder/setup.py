from setuptools import setup

setup(name='clean_folder',
      version='1',
      description='Cleaning script',
      url='',
      classifiers=[
        "Python version :: Python :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operating System :: Windows :: Linux :: MAC"],
      author='LokFaadDiiv',
      author_email='koto.amatsukami@ukr.net',
      license='MIT',
      packages=['clean_folder'],
      python_requires=">=3.7",
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)


