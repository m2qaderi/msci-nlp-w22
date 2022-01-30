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

    import sklearn.model_selection

    new_string3 = new_string2.replace("]", '')
    new_string4 = new_string3.replace("[", '')
    print(new_string4[0:100])

    a = list(new_string4.split(" "))
    b = random.shuffle(a)
    train_dataset, test_dataset = sklearn.model_selection.train_test_split(a, train_size=.8, test_size=.2)
    test2_dataset, valid_dataset = sklearn.model_selection.train_test_split(test_dataset, train_size=.5, test_size=.5)


    print(train_dataset[0:100])
    print(len(train_dataset))

    print(test2_dataset[0:100])
    print(len(test2_dataset))

    print(valid_dataset[0:100])
    print(len(valid_dataset))

    train = open("train.csv", "w")
    for element in train_dataset:
        train.write(element + " ")
    train.close()

    test = open("test.csv", "w")
    for element in test2_dataset:
        test.write(element + " ")
    test.close()

    val = open("val.csv", "w")
    for element in valid_dataset:
        val.write(element + " ")
    val.close()

    with open(file_path) as f: 
        text2 = f.read()

    # Removing stopwords
    from gensim.parsing.preprocessing import remove_stopwords

    lowercase = text2.lower()
    filtered_text = remove_stopwords(lowercase)
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

    import sklearn.model_selection

    c = list(new_string7.split(" "))
    d = random.shuffle(c)
    train_dataset_ns, test_dataset_ns = sklearn.model_selection.train_test_split(a, train_size=.8, test_size=.2)
    test2_dataset_ns, valid_dataset_ns = sklearn.model_selection.train_test_split(test_dataset_ns, train_size=.5, test_size=.5)


    print(train_dataset_ns[0:100])
    print(len(train_dataset_ns))

    print(test2_dataset_ns[0:100])
    print(len(test2_dataset_ns))

    print(valid_dataset_ns[0:100])
    print(len(valid_dataset_ns))

    train_ns = open("train_ns.csv", "w")
    for element in train_dataset_ns:
        train_ns.write(element + " ")
    train_ns.close()

    test_ns = open("test_ns.csv", "w")
    for element in test2_dataset_ns:
        test_ns.write(element + " ")
    test_ns.close()

    val_ns = open("val_ns.csv", "w")
    for element in valid_dataset_ns:
        val_ns.write(element + " ")
    val_ns.close()