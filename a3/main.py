import re
import sys
from gensim.models import Word2Vec

if __name__ == "__main__":
    file_path = sys.argv[1]

    print("Opening file at path: {}".format(file_path))

    with open(file_path) as f: 
        full_text = f.readlines()

    # Removing special characters
    new_text = [re.sub('[!"#$%&()*+/:;<=>@,[\\]^`{|}~\t\n\-]', '', string) for string in full_text]

    # Tockenizing
    split_list =[i.split(" ") for i in new_text]

    # Train and save model
    print("Training model")
    model = Word2Vec(split_list, min_count=1)
    print("Saving model")
    model.save('data/w2v.model')