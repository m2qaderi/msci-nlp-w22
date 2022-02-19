import re
import sys
from gensim.models import Word2Vec

if __name__ == "__main__":
    file_path = sys.argv[1]

    print("Opening file at path: {}".format(file_path))
    with open(file_path) as f: 
        word_text = f.readlines()
    
    # Output top 20 most similiar words
    new_text2 = [re.sub('[!"#$%&()*+/:;<=>@,[\\]^`{|}~\t\n\-]', '', string) for string in word_text]

    model = Word2Vec.load('data/w2v.model')

    for key in new_text2:
        print("Finding similarity for ({})".format(key))
        print("{:15s} Similarities".format("Words"))
        for word in model.wv.most_similar([key], topn=20):
            print("{:15s} {}".format(word[0], word[1]))
        print("")