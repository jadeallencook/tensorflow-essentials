# test if python is installed
if [ -z "$(which python)" ]; then
    # if not installed then install python
    echo "Python is not installed. Installing python..."
    sudo apt-get install python
    echo "Python installed successfully."
fi

