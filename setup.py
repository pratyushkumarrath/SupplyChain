from setuptools import setup, find_packages

setup(
    name="supply_chain_ml",
    version="1.0.0",
    author="Pratyush Kumar Rath",
    description="ETA and Delay Prediction using Supply Chain Data",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "xgboost",
        "catboost",
        "matplotlib",
        "seaborn"
    ],
)