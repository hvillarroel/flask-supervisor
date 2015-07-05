from setuptools import setup, find_packages


setup(name="flask-supervisor",
      version="1.0",
      description="",
      author="Héctor Villarroel",
      author_email='',
      url='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          ["Flask", "Flask-admin"]
      ],
      )
