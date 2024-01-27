from setuptools import setup, find_packages

setup(
    name='GrammarHelper',  # Replace with your desired package name
    version='0.1.0',  # Update with your version number
    packages=find_packages(),  # Automatically discover packages
    install_requires=[
        'rpy2==3.5.15',
        'numpy==1.22.0',
        'pandas',
        'scipy',
        'xgboost',
        'scikit-learn',  # Combines multiple scikit-learn imports
    ],  # List dependencies for automatic installation
    entry_points={
        'console_scripts': [
            'GrammarHelper=GrammarHelper.Predict:predict',
            # Replace with your script name, main module, and function
        ],
    },  # Enables running scripts directly (if applicable)
)