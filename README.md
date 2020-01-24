# cs-337

## Using a virtual environment
```
python3 -m venv ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running our project
Before running our project, ensure you have followed the steps to create a virtual environment and install the necessary packages.

### Get all supported information
```
python golden-globes.py
```

### Get specific information
```
python golden-globes.py [-g | --get] [hosts | awards | winners | nominees | presenters]
```