# imgurapp

## Table of Contents

1. [Problem Statement](#probem-statement)
1. [Description](#description)
1. [Tech Stack](#tech-stack)
1. [Installation & Use](#installation--utilization)
1. [Future Plans](#future-plans)
1. [Contributing](#contributions)

## Probem Statement

When encountering an issue that needs troubleshooting, the author occasionally finds it advantageous to upload a screen capture of the issue to [Imgur](imgur.com) to assist with illustrating the problem when asking for help online. Streamlined as the Imgur website's user interface may be, the efficiency of the login and upload process could be increased by leveraging the advantages of a command-line-interface (CLI) app, with the added benefit of app portability between \*nix-like systems.

Initial research indicated that Imgur's [API](https://apidocs.imgur.com/) might be leveraged, which would be highly advantageous to development speed and code quality. Unfortunately the API seems to have been [deprecated](https://www.reddit.com/r/webdev/comments/746w44/imgur_api_cant_register_just_get_redirected_to_my/), locked down, or is otherwise broken, as when the author attempted to register an app, it was discovered that a redirect automatically sends the user to the Imgur main page.

Falling back on the flexibilty of Python, a script leveraging [Selenium](https://www.selenium.dev/) was developed.

## Description

This script in its current form needs to be run manually in terminal, then opens a web browser, logs into Imgur per the credentials entered by the user, and opens a file browser upload chooser window to allow the user to select one or more images from a single directory to upload to the active account.

## Tech Stack

Python 3, Selenium.

Please be sure that Selenium is [installed](https://www.selenium.dev/documentation/webdriver/getting_started/install_library/#install-manually) in the Python env being used.

## Installation & utilization

Download the `main.py` file from this repository. Cloning the repository isn't necessary to use the script. In the directory to which it was saved, run the script in terminal with

- `$ python main.py`
- `$ python3 main.py`

depending on your system. Input the Imgur user account credentials when prompted. When your system's file browser upload chooser appears you may select the image(s) you wish to upload. The script does no further operations after opening the file browser upload chooser, so any other operations inlcuding but not limited to logging out or posting images to Imgur (distinct from uploading images) is the responsibility of the user.

## Future plans

The author would like to expand the functionality of the script to that of a full CLI program, allowing the program to be run similar to other CLI apps. For example:

`$ imgurcli [username] [password] [path-to-file(s)]`

The author suspects this may be difficult-to-impossible without access to the Imgur API.

## Contributions

Pull requests are welcome. For major changes, please open an issue first.
