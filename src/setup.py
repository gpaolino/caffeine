from setuptools import setup, find_packages

setup(
      name='caffeine',
      version='0.0.1',
      description='Caffeine App',
      author='Paolo Guglielmino',
      author_email='gp.guglielminopaolo@gmail.com',
      url='https://github.com/gpaolino/caffeine',
      packages=find_packages(),
      entry_points={
          "console_scripts": ["caffeine=caffeine:main"],
      },
)