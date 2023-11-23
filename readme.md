# TensorFlow Essentials

## Setting Up Python 3.11 on macOS for TensorFlow Installation

This guide is specifically designed for macOS users to set up Python 3.11 for TensorFlow installation. While some instructions may be applicable to other operating systems, they are primarily intended for macOS.

### Verify Python Installation

1. **Check Existing Python Version**:
   - Open the Terminal.
   - Run `python --version` or `python3 --version`.
   - If a version number appears and it's between 3.9 and 3.11, you're set. Otherwise, follow the installation steps below.

### Install Python (if necessary)

1. **Download Python**:
   - If Python is not installed or not within the required version range (3.9–3.11), download it from [Python Downloads](https://www.python.org/downloads/).

## Installing Python 3.11

### Install Homebrew

1. **Check Homebrew Installation**:
   - Homebrew is essential for installing Python 3.11. To install or verify Homebrew, visit [Homebrew's website](https://brew.sh).

### Use pyenv for Python Installation

1. **Update and Install pyenv**:

   - In the Terminal, execute:
     ```
     brew update
     brew install pyenv
     ```

2. **Configure pyenv in Terminal**:

   - Add the following lines to your `~/.zshrc` file:
     ```
     export PYENV_ROOT="$HOME/.pyenv"
     export PATH="$PYENV_ROOT/bin:$PATH"
     eval "$(pyenv init --path)"
     ```

3. **Install Python 3.11 Using pyenv**:

   - Run `pyenv install 3.11.0`.
   - Set it as the default version: `pyenv global 3.11.0`.

4. **Restart Terminal & Verify Installation**:
   - Restart your Terminal.
   - Confirm the installation with `python3 --version`.

## Installing pip

1. **Check pip Installation**:

   - Execute `pip --version` or `pip3 --version` in the Terminal.

2. **Install pip (if necessary)**:
   - If pip is not installed, download it from [pip Installation](https://pip.pypa.io/en/stable/installation/).

## Install TensorFlow

1. **Install TensorFlow via pip**:
   - Run `pip3 install tensorflow` in the Terminal.

Follow each step in this guide for a smooth setup process in preparing your macOS environment for TensorFlow development.
