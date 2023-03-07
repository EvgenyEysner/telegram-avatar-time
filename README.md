### Desription
    Python 3.8
A small Python script that lets you display a digital clock as a Telegram avatar.
### Virtual environment

To avoid conflicting interpreters and package versions it is recommended to
[use a virtual environment](https://code.visualstudio.com/docs/python/tutorial-django#_create-a-project-environment-for-the-django-tutorial)

```bash
python3 -m venv .venv
```

```bash
. .venv/bin/activate
```

### Access to Telegram login from code:
    https://my.telegram.org/auth

### Create .env file in root directory
```bash
touch .env
```

### and dds the following entries from the Telegram API

    API_ID=api_id
    API_HASH=api_hash

### Run App
```bash
python3 main.py
```

### Dependencies for Linux Users

```bash
sudo apt-get -y install python3-pyqt5
```
