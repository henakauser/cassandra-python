# Install


## Install Python dependencies (one-time setup)

```bash
sudo apt-get install gcc python-dev python-virtualenv libev4 libev-dev
```


## Create new Git repo on GitHub

1. https://github.com/
2. Click `New repository`
3. In `Repository name`, enter **cassandra-python**.
4. In `Description`, enter **Access Cassandra from Python**.
5. Check `Initialize this repository with a README`.
6. Select the `Add .gitignore` drop-down list, select **Python**.
7. Select the `Add a license` drop-down list, select **MIT**. 
8. Click `Create repository`.


## Clone the new repository

```bash
cd

git clone git@github.com:henakauser/cassandra-python.git

cd cassandra-python
```


## Setup virtualenv

```bash
virtualenv venv
```


## Activate / deactivate virtualenv

```bash
# Activate virtualenv
. venv/bin/activate

# Exit virtualenv (when you need to later)
deactivate
```


# Install the Cassandra Python driver

```bash
pip install cassandra-driver

pip install scales blist 
```

