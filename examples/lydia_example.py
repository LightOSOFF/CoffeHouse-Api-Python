from datetime import datetime

from coffeehouse import LydiaAI

# Create the CoffeeHouse API instance
api_key = input('API Key: ')

# Create Lydia instance
lydia = LydiaAI(api_key)

# Create a new chat session (Like a conversation)
# Optional: langiage parameter, defaults to "en"
session = lydia.create_session(language='en')
print(f'Session ID: {session.id}')
print('Session Available: {}'.format(str(session.available)))
print('Session Language: {}'.format(str(session.language)))
print(
    'Session Expires: {}'.format(
        str(datetime.fromtimestamp(session.expires)),
    ),
)

# Talk to the bot!
while True:
    output = session.think_thought(input('Input: '))
    print(f'Output: {output}')

# In the case you want to save the Session ID to reuse the session
# Use lydia to invoke think_thought instead, for example;
#
# while(True):
#     output = lydia.think_thought(session.id, input("Input: "))
#     print("Output: {0}".format(output))
#
# This is the same effect as above but uses the lydia instance directly.
