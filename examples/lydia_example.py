from datetime import datetime
from coffeehouse import LydiaAI

def main():
    # Create the CoffeeHouse API instance
    api_key = input('API Key: ')

    # Create Lydia instance
    lydia = LydiaAI(api_key)

    # Create a new chat session (Like a conversation)
    # Optional: language parameter, defaults to "en"
    session = lydia.create_session(language='en')
    print(f'Session ID: {session.id}')
    print('Session Available: {}'.format(session.available))
    print('Session Language: {}'.format(session.language))
    print(
        'Session Expires: {}'.format(
            datetime.fromtimestamp(session.expires),
        ),
    )

    # Talk to the bot!
    while True:
        output = session.think_thought(input('Input: '))
        print(f'Output: {output}')

if __name__ == "__main__":
    main()
