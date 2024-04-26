# CoffeeHouse API Wrapper for Python

This is a simple Python wrapper for the CoffeeHouse API. The library supports only the V1IVA2.0 CoffeeHouse API, which is documented [here](https://gist.github.com/Netkas/e8977b26f482ca40911a949df7dd286f).

## Installation

You can install the library via pip:

```sh
pip install coffeehouse
```

Alternatively, you can clone the repository and install it manually:

```sh
git clone https://github.com/LightOSOFF/CoffeHouse-Api-Python
cd CoffeHouse-Api-Python
python setup.py build
python setup.py install
```

## Lydia Example

```python
from coffeehouse.lydia import LydiaAI

# Create the CoffeeHouse API instance
api_key = input("API Key: ")

# Create Lydia instance
lydia = LydiaAI(api_key)

# Create a new chat session (Like a conversation)
session = lydia.create_session()
print("Session ID: {0}".format(session.id))
print("Session Available: {0}".format(str(session.available)))
print("Session Language: {0}".format(str(session.language)))
print("Session Expires: {0}".format(str(session.expires)))

# Talk to the bot!
while True:
    output = session.think_thought(input("Input: "))
    print("Output: {0}".format(output))
```

In the case you want to save the Session ID to reuse the session, you can use the `think_thought` method directly from the `LydiaAI` instance. Here's an example:

```python
while True:
    output = lydia.think_thought(session.id, input("Input: "))
    print("Output: {0}".format(output))
```

This has the same effect as the previous example but uses the `lydia` instance directly.