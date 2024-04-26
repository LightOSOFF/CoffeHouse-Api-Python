from coffeehouse import NsfwClassifier

def main():
    # Defining the API Key of the user
    api_key = input('API Key: ')

    # Create Classifier instance
    classifier = NsfwClassifier(api_key)

    # Reading the Image file and sending it through the API
    with open('path/to/image.jpg', 'rb') as f:
        result = classifier.classify(f.read()).nsfw_classification

    # Output
    print('Content Hash:', result.content_hash)
    print('Content Type:', result.content_type)
    print('Safe Prediction:', result.safe_prediction)
    print('Unsafe Prediction:', result.unsafe_prediction)
    print('is NSFW:', result.is_nsfw)

if __name__ == "__main__":
    main()
