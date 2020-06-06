from distutils.core import setup, Extension

module1=Extension('exmod',
	include_dirs= ['/Users/Lenovo/AppData/Local/Programs/Python/Python38-32/include'],
	sources= ['exmodmodule.cpp'])

setup (name= 'exmod',
	version= '1.0try',
	description= 'test',
	author= 'Sanyam Singhal',
	url='https://www.google.com/',
	ext_modules=[module1])