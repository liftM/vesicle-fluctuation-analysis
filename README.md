# vesicle-fluctuation-analysis

Measures bending rigidity and tension of bio-membranes.

## Running

### With Docker

```sh
docker build -t vfa .

# Mount a folder with input files and output files.
docker run -it -v $(pwd):/home/vfa/app vfa
```

The mounted folder must be be writeable by the Docker container. See [this SO post](https://stackoverflow.com/questions/29245216/write-in-shared-volumes-docker) for advice on setting permissions (TL;DR: Docker uses the same permissions as your host - make sure the host permissions would be writeable for the user in the Docker container).

### On raw metal

#### Setting up your Python environment

See [pipenv](https://github.com/pypa/pipenv) documentation. TL;DR:

1. Install `pyenv` to install Python. ([Pyenv installation docs](https://github.com/pyenv/pyenv#installation))
2. Use `pip` to install `pipx`. ([Pipx installation docs](https://github.com/pipxproject/pipx#install-pipx))
3. Use `pipx` to install `pipenv`. ([Pipenv installation docs](https://github.com/pypa/pipenv#installation))

#### Running the project

```sh
# Install dependencies
pipenv install --deploy
pipenv run python vfa.py
```
