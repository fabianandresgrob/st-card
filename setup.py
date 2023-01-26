import setuptools

with open('README.md') as readme_file:
    readme = readme_file.read()


setuptools.setup(
    name="streamlit-cardv2",
    version="1.0.0",
    author="fabianandresgrob",
    author_email="grobfab@gmail.com",
    description="A streamlit UI card component in its second version",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/fabianandresgrob/st-card",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="card streamlit streamlit-component",
    python_requires=">=3.8",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
