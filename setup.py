from setuptools import Extension, find_packages, setup


with open("README.md") as f:
    long_description = f.read()


if __name__ == "__main__":
    setup(
        name="colabcode",
        scripts=["scripts/colabcode"],
        version="0.3.0",
        description="ColabCode - Run codeserver on Colab!",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Abhishek Thakur",
        author_email="abhishek4@gmail.com",
        url="https://github.com/abhishekkrthakur/colabcode",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            "pyngrok",
            "nest_asyncio",
            "uvicorn",
            "jupyterlab==3.0.7",
        ],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )
