from setuptools import setup


setup(
     name='discord_poebot',
     version='0.1',
     description='Search gems and translation for any language. ',
     author='Koji Kiriake',
     author_email='kiriake@gmail.com',
     url='https://github.com/kiriake/discord_poebot',
     install_requires=open('requirements.txt').read().splitline(),
)
