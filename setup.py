from distutils.core import setup


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
    package_dir={"suit_object_tools": "suit_object_tools"},
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
