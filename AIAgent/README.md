# AIAgent
Example implementation of AIAgent in python

# SetUp Virtual Environment

### Create

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
    python3 -m venv .venv
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