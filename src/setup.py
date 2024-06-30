from setuptools import setup

setup(
      name='caffeine',
      version='1.0',
      description='Caffeine App',
      author='Paolo Guglielmino',
      author_email='gp.guglielminopaolo@gmail.com',
      url='https://github.com/gpaolino/caffeine',
      packages=["caffeine"],
      entry_points={
          "console_scripts": ["caffeine=caffeine:main"],
      },
)