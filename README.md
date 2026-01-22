# learnings

# Pyenv

https://github.com/pyenv/pyenv?tab=readme-ov-file

## Getting

```shell
curl -fsSL https://pyenv.run | bash
```

## Setup

Add the following in ~/.bashrc, ~/.profile and ~/.bash_profile if the file exists
```shell
for profile in ~/.bashrc, ~/.profile ~/.bash_profile
do
    if [ -f $profile ]
    then
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $profile
        echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> $profile
        echo 'eval "$(pyenv init - bash)"' >> $profile
    else
        echo $profile does not exists
    fi
done
``

## Install build env

### Ubuntu
```shell
sudo apt update; sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl git \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
````

### Mac

```shell
brew install openssl readline sqlite3 xz tcl-tk@8 libb2 zstd zlib pkgconfig
```

## Working

### Install additional Python versions

```shell
pyenv install 3.10.4
```

### See list of all available versions

```shell
pyenv install -l
```

### E.g. to install and then switch to the latest 3.10 release

```shell
pyenv install 3.10
pyenv global 3.10
```

### Switch between Python versions

pyenv shell <version> -- select just for current shell session
pyenv local <version> -- automatically select whenever you are in the current directory (or its subdirectories)
pyenv global <version> -- select globally for your user account

### Uninstall
```shell
pyenv uninstall 3.10
```


# SetUp Virtual Environment

## Create

```shell
python3 -m venv .venv
```

## Activate

```shell
source .venv/bin/activate
```

## Deactivate

```shell
deactivate
```

Add shortcuts in ~/.bashrc to create/activate/deactivate

```shell
# Function to create a new virtual environment at pwd
venvc() {
    if [ -d .venv ]
    then
        echo ".venv exists. Delete .venv and run venvc again to create a new venv."
    else
        python3 -m venv .venv
    fi
}

# Function to activate local .venv
venva() {
    if [ -f .venv/bin/activate ]; then
        source .venv/bin/activate
    else
        echo ".venv/bin/activate not found in the current directory."
    fi
}

venvd() {
  deactivate
}
```

# Code to move df row columns to global variables

```python
def run_rules_engine(df):
  def dynamic_global_variable(df):
    df_dict = df.to_dict('list')
    for name in df_dict:
      globals()[name] = df_dict[name][0]

  dynamic_global_variable(df)
```