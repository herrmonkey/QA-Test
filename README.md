# QA Testing Engineer Profile Test Ricardo Gonzalez

<a><img src="https://media.licdn.com/dms/image/C4E03AQFhbMXQ8bPqTw/profile-displayphoto-shrink_200_200/0/1650652503560?e=1681344000&v=beta&t=cINQ4fEcIEo9EWSru8sAj2rI1QDYBKBU-SDgYauaNTU"/></a>

This project uses Python 3.11 and the frameworks Behave(BDD) and Selenium.

This README outlines the necessary steps for setting up and running QA profile tests. It provides an introduction to Selenium, the automation testing framework, and explains how to use it to write automated tests for web applications. It also provides a walkthrough of an example test and explains the different types of tests that can be performed using Selenium. Finally, it outlines the process for using Selenium with remote WebDriver

## Page Object Model (POM)
The Page Object Model (POM) is a design pattern used in Selenium for automating the test cases. This pattern creates an object repository for web UI elements and also serves as an interface for writing the tests. It helps to reduce code duplication and makes the tests more maintainable and readable. The POM pattern also helps to separate the test data from the test code, making the tests more modular and easier to read.

The default browser is Chrome, if you want run the tests in other browser, not only you have to install the module for the web browser that you desire, but change the parameter browser with the corresponding option in the WebDriverSetup.py file. The Selenium modules are available for:  

- `chrome`
- `firefox`
- `safari`
- `edge`


Selenium's source code is made available under the [Apache 2.0 license](https://github.com/SeleniumHQ/selenium/blob/trunk/LICENSE).

## Documentation

Selenium documentation:

* [User Manual](https://selenium.dev/documentation/)

Pytest documentation:

* [User Manual](https://docs.pytest.org/en/7.1.x/contents.html)



API documentation:

* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)


This project is for execute the tests locally

## Requirements

* Install the latest version of python. See documentation https://www.python.org/
  * Insstall pip, This command should work `python3 get-pip.py`
  * Install Selenium, This command should work `pip3 install selenium`
  * Install WebDriver browser, This command should work `pip3 install webdriver-manager`
  * Install pytest, This command should work `pip3 install pytest`


## Runnig

* For run this tests: in the Root file use `pytest -v` command

