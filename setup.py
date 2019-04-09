import setuptools
# from packagename.version import Version

setuptools.setup(name='NpSocket',
                 version='0.1.0',
                 description='Send Numpy Arrays over TCP/IP socket',
                 long_description=open('README.md').read().strip(),
                 author="Vaghawan Ojha, Bibek Chaudhary",
                 author_email='vaghawan781@gmail.com',
                 url='https://github.com/ekbanasolutions/numpy-using-socket',
                 py_modules=['npsocket.npsocket'],
                 install_requires=['numpy'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='numpy, python3, socket',
                 classifiers=[''])
