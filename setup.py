from setuptools import setup

setup(name='funniest',
      version='0.1',
      description='The funniest joke in the world',
      url='https://github.com/Gus1616/Funniest_python_package',
      author='Gus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      entry_points = {
        'console_scripts': ['sys_info_comp30380=funniest.command_line:main'],
      }
      )