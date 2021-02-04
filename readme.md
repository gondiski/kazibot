# Kazybott

Kazybott uses the twitter API to display related tweets on a single timeline. Check out the project on [kazybott](https://twitter.com/kazybott)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install kazybott dependencies.

```bash
pip install -r requirements.txt
```

## Usage
Ensure to include the required credentials in the credentials.py file and import it in the bot.py document
```python
import tweepy
import time
import random
from time import sleep
import math

from credentials import *
```
Execute the application by executing the below command
```bash
python bot.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE](http://www.apache.org/licenses/)