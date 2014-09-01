from distutils.core import setup
# from setuptools import find_packages

setup(
    name="suit_object_tools",
    version=__import__("suit_object_tools").__version__,
    description="Adds single object actions to suit sidebar",
    long_description='',
    author="Yuji Tomita",
    author_email="yuji@studioparadise.com",
    url="https://github.com/yuchant/suit_object_tools",
    packages=[
        "suit_object_tools",
    ],
    # data_files=[('', '*.html')],
    package_data={
        'suit_object_tools': [
            'templates/admin/*.html',
        ],
    },
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
)
