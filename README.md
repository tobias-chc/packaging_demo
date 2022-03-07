# Password Package

Password is a simple Python package for generate a random password for of a length given by the user.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install password-package.

```bash
python -m pip install -i https://test.pypi.org/simple/ password-package-tobias-chc
```

## Usage

```python
# Simple script
from password_package import pass_generator
password = pass_generator.create_password()
print(password)
```

```bash
#The console will display the following message: 
Enter the length of your password:
# Example of a return after type 13
G}r3]Y5#ln1Q2
```

## Goal

I have created this simple package just for my personal use and to get an idea of how a Continuous Integration & Continuous Delivery (Deployment) (CI/CD)
pipeline works. In this project I have applied the following topics:

- [Python Packaging.](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Write and run unit tests using pytest library.](https://docs.pytest.org/en/7.0.x/getting-started.html)
- [Create an automated testing pipeline with GithHub Actions.](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
- [Publish a Python distribution package in the dist/ directory to Test PyPI.](https://github.com/marketplace/actions/pypi-publish)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)




