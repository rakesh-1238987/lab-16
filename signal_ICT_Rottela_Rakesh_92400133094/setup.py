from setuptools import setup, find_packages

setup(
    name="signal_ICT_Rottela_Rakesh_92400133094",   # <-- Replace with your actual student name & roll no
    version="0.1",
    author="R.Rakesh",
    author_email="rottela.rakesh124031@marwadiuniversity.ac.in",
    description="A Python package for generating and working with basic signals",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://test.pypi.org/project/signal_ICT_Rottela_Rakesh_92400133094/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib"
    ],
)
