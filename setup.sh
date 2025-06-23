# Install pyenv
curl https://pyenv.run | bash

# Add pyenv to shell (append to ~/.bashrc or ~/.bash_profile)
export PATH="$HOME/.pyenv/bin:$PATH"
export PATH="$PATH:$(pwd)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Reload shell
source ~/.bashrc

# Install desired Python version
pyenv install 3.11.7
pyenv global 3.11.7

python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt