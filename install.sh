# test if python is installed
if [ -z "$(which python)" ]; then
    # if not installed then install python
    echo "Python is not installed. Installing python..."
    sudo apt-get install python
    echo "Python installed successfully."
fi

# test if homebrew is installed
if [ -z "$(which brew)" ]; then
    # if not installed then install homebrew
    echo "Homebrew is not installed. Installing homebrew..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    echo "Homebrew installed successfully."
fi

# test if pyenv is installed
if [ -z "$(which pyenv)" ]; then
    # if not installed then install pyenv
    echo "Pyenv is not installed. Installing pyenv..."
    brew install pyenv
    echo "Pyenv installed successfully."
fi

# install python 3.11 using pyenv
echo "Installing python 3.11..."
pyenv install 3.11
echo "Python 3.11 installed successfully."

# add pyenv root to zshrc
echo "Adding pyenv root to zshrc..."
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init --path)"' >> ~/.zshrc
echo "Pyenv root added successfully."

# load new zshrc
echo "Loading new zshrc..."
source ~/.zshrc
echo "New zshrc loaded successfully."

# test if pip is installed
if [ -z "$(which pip)" ]; then
    # if not installed then install pip
    echo "Pip is not installed. Installing pip..."
    sudo apt-get install python-pip
    echo "Pip installed successfully."
fi

# test if tensorflow is installed
if [ -z "$(pip list | grep tensorflow)" ]; then
    # if not installed then install tensorflow
    echo "Tensorflow is not installed. Installing tensorflow..."
    pip install tensorflow
    echo "Tensorflow installed successfully."
fi

# display success message
echo "Installation complete."