from coffeehouse import NsfwClassifier

# Defining the API Key of the user
api_key = input('API Key: ')

# Create Classifier instance
classifier = NsfwClassifier(api_key)

# Reading the Image file and sending it through the API
with open('path/to/image.jpg', 'rb') as f:
    result = classifier.classify(f.read()).nsfw_classification

# Output
print('Content Hash: {}'.format(str(result.content_hash)))
print('Content Type: {}'.format(str(result.content_type)))
print('Safe Prediction: {}'.format(str(result.safe_prediction)))
print('Unsafe Prediction: {}'.format(str(result.unsafe_prediction)))
print('is NSFW: {}'.format(str(result.is_nsfw)))
