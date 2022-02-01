import gensim as gensim
import numpy as numpy
import sklearn as sklearn

import re
import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    args = parser.parse_args()
    path = args.path
    file_path = f"{path}/posneg.txt"
    print(file_path)

    with open(file_path) as f: 
        text = f.readlines()

    # Removing special characters
    new_string = [re.sub('[!"#$%&()*+/:;<=>@,[\\]^`{|}~\t\n\-]', '', string) for string in text]

    # Tockenizing with stop words
    split_list =[i.split(" ") for i in new_string]
    print(split_list[1:100])

    # Converting list to string
    listToString = '\r\n'.join(map(str, split_list)) + '\r\n'
    new_string2 = re.sub('[\']', '', listToString)
    print(new_string2[1:1000])

    # Exporting as csv file
    out = open("out.csv", "w")
    for element in new_string2:
        out.write(element)
    out.close()

    # Splitting data into train test and validation sets
    new_string3 = new_string2.replace("]", '')
    new_string4 = new_string3.replace("[", '')
    print(new_string4[0:100])

    a = list(new_string4.split(" "))
    b = random.sample(a, len(a))
    c = round(len(a)*.8)
    d = round(len(a)*.9)


    train_dataset = b[:c]
    test_dataset = b[c:d]
    valid_dataset = b[d:len(a)]


    print(train_dataset[0:100])
    print(len(train_dataset))

    print(test_dataset[0:100])
    print(len(test_dataset))

    print(valid_dataset[0:100])
    print(len(valid_dataset))

    train = open("train.csv", "w")
    for element in train_dataset:
        train.write(element + " ")
    train.close()

    test = open("test.csv", "w")
    for element in test_dataset:
        test.write(element + " ")
    test.close()

    val = open("val.csv", "w")
    for element in valid_dataset:
        val.write(element + " ")
    val.close()

    with open(file_path) as f: 
        text2 = f.read()

    # Removing stopwords

    stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours','ourselves', 'you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','s','t','can','will','just','don','should','now']
    querywords = text2.split()

    removed = [word for word in querywords if word.lower() not in stopwords]
    filtered_text = ' '.join(removed)

    print(filtered_text[0:100])

    ns = open("no_stopwords.csv", "w")
    for element in filtered_text:
        ns.write(element)
    ns.close()

    with open(file_path) as f: 
        text3 = f.readlines()

    # Removing special characters
    new_string5 = [re.sub('[!"#$%&()*+/:;<=>@,[\\]^`{|}~\t\n\-]', '', string) for string in text3]

    # Tockenizing with stop words
    split_list2 =[i.split(" ") for i in new_string5]
    print(split_list2[1:100])

    # Converting list to string
    listToString2 = '\r\n'.join(map(str, split_list2))
    new_string6 = re.sub('[\']', '', listToString2)
    new_string7 = new_string6.replace(".", '\n')
    print(new_string7[1:1000])

    # Exporting as csv file
    out_ns = open("out_ns.csv", "w")
    for element in new_string7:
        out_ns.write(element)
    out_ns.close()

    # Splitting data into train test and validation sets
    e = list(new_string7.split(" "))
    f = random.sample(e, len(e))
    g = round(len(f)*.8)
    h = round(len(f)*.9)

    train_dataset_ns = f[:g]
    test_dataset_ns = f[g:h]
    valid_dataset_ns = f[h:len(e)]

    print(train_dataset_ns[0:100])
    print(len(train_dataset_ns))

    print(test_dataset_ns[0:100])
    print(len(test_dataset_ns))

    print(valid_dataset_ns[0:100])
    print(len(valid_dataset_ns))

    train_ns = open("train_ns.csv", "w")
    for element in train_dataset_ns:
        train_ns.write(element + " ")
    train_ns.close()

    test_ns = open("test_ns.csv", "w")
    for element in test_dataset_ns:
        test_ns.write(element + " ")
    test_ns.close()

    val_ns = open("val_ns.csv", "w")
    for element in valid_dataset_ns:
        val_ns.write(element + " ")
    val_ns.close()