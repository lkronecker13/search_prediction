import numpy as np
from keras.models import model_from_json
import json


def decode_vectors(binary_matrix):
    tokens = []
    for vect in binary_matrix:
        tokens.append(np.argmax(vect)+1)
    return tokens;
    
def decode_sequence(sequence, city_list):
    citys = []
    for token in sequence:
        citys.append(city_list[token-1])
    return citys
    
def extract_most_relevant_predictions(test_predict, number_of_most_relevant_predictions, verbose=False):
    # Get the 5 most relevant predictions (the classes with probabilities closest to one)
    highest_predictions = np.argpartition(test_predict, -number_of_most_relevant_predictions)[-number_of_most_relevant_predictions:]
    # Get the probability scores for each one of the most relevant predictions
    scores_preds = test_predict[highest_predictions]
    # Sort the predicted values by the most relevant first (the ones with probability closest to the leftmost side of the list)
    # Note that we are adding + 1 to realign the predicted value with the city token (class)
    ordered_predictions = highest_predictions[np.argsort(test_predict[highest_predictions])][::-1] + 1
    
    if verbose:
        print('Indexes of predictions with highest scores: ' + str(highest_predictions))
        print('Probability distributions: ' + str(scores_preds))
        print( str(number_of_most_relevant_predictions) + ' most probable cities: ' + str(ordered_predictions))
        

    return ordered_predictions
    
def strings_to_list(sequences_str):
    sequences_str = sequences_str.replace('[', '')
    sequences_str = sequences_str.replace(']', '')
    return np.asarray([int(token) for token in sequences_str.split(",")])
    
# Tokenize function used to transform city names into tokens with respect of the alphabetically ordered city list.
def tokenize_city_sequence(cities, city_list):
    tokens = []
    for city in cities:
        tokens.append(city_list.index(city)+1)
    return tokens
    
def load_model(path):
    with open(path + '/model_architecture.json', 'r') as f:
        model = model_from_json(json.load(f))
        model.load_weights(path + '/model_weights.hdf5')
        return model
    
def load_loss(path):
    with open(path + '/loss.json', 'r') as f:
        return json.load(f)