from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'bbox'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude = "test"),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('rviz/*.rviz'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='splion360',
    maintainer_email='splion360@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bounding_box=bbox.detect:main',
            'video=bbox.camera:main',

        ],
    },
)
