from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    summary="A sample test package",
    author="eagle",
    author_email="eagle@42.fr",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/eagle/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[],
    python_requires='>=3.6',
)
