#1 Sentimental Analysis

#1.1. Importing articles and saving them as .txt
import pandas as pd
df = pd.read_csv('url.csv')

#Importing Data from multiple url (Class type 1)
def give(url,index):
 from bs4 import BeautifulSoup
 import requests

 website = url
 result = requests.get(website)
 content = result.text
 soup = BeautifulSoup(content, 'lxml')

 title = soup.find('h1', class_='entry-title').get_text()
 # textbox = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
 innerbox = soup.find('div', class_='td-post-content').get_text(strip=True, separator=' ')
 full_article = title + innerbox
 
 filename = str(index) + '.txt'
 
 with open(filename, 'w', encoding='utf-8') as file:
  file.write(full_article)

#Importing Data from multiple url (Class type 2)
import pandas as pd
df = pd.read_csv('url.csv')

def giver(url,index):
 from bs4 import BeautifulSoup
 import requests

 website = url
 result = requests.get(website)
 content = result.text
 soup = BeautifulSoup(content, 'lxml')

 title = soup.find('h1', class_='tdb-title-text').get_text()
#     textbox = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
 innerbox = soup.find('div', class_='td-post-content').get_text(strip=True, separator=' ')
 full_article = title + innerbox
 
 filename = str(index) + '.txt'
 
 with open(filename, 'w', encoding='utf-8') as file:
  file.write(full_article)

#Importing Data from multiple url (Class type 3)
def gave(url,index):
 from bs4 import BeautifulSoup
 import requests

 website = url
 result = requests.get(website)
 content = result.text
 soup = BeautifulSoup(content, 'lxml')

 title = soup.find('h1', class_='entry-title').get_text()
 # textbox = soup.find('div', class_='td_block_wrap tdb_single_content tdi_130 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
 innerbox = soup.find('div', class_='td-post-content').get_text(strip=True, separator=' ')
 full_article = title + innerbox
 
 filename = str(index) + '.txt'
 
 with open(filename, 'w', encoding='utf-8') as file:
  file.write(full_article)

#Using a loop to apply all 3 functions for the files
functions = [give, giver, gave]

i = 0
for element in df['url_id']:
    url = df['url'][i]
    index = element
    for func in functions:
        try:
            func(url, index)  
        except Exception as e:
            print(f"Error occurred for {func.__name__}: {e}")
            continue
    i = i + 1  

#7 Personal Pronouns calculation and saving in Output Data Structure.csv
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stpwrd = nltk.corpus.stopwords.words('english')
stpwrd.remove('i')
stpwrd.remove('we')
stpwrd.remove('my')
stpwrd.remove('ours')

def read_txt_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      text = file.read()
  except UnicodeDecodeError:
    # If 'utf-8-sig' fails, try with 'latin-1' encoding
    with open(file_path, 'r', encoding='latin-1') as file:
      text = file.read()
  return text

def tokenize_text(text):
  words = nltk.word_tokenize(text)
  return words

def remove_stopwords(words):
  filtered_words = [word for word in words if word.lower() not in stpwrd]
  return filtered_words

prefix = list(range(37, 151))
original_list = prefix
prefix_list = [str(element) for element in original_list]
original_list = prefix_list
suffix = ".txt"

def add_suffix_to_element(element):
    return element + suffix

filename_list = list(map(add_suffix_to_element, original_list))

filename_list.remove('44.txt')
filename_list.remove('57.txt')
filename_list.remove('144.txt')

import re

def count_personal_pronouns(word_list):
    personal_pronouns = ['I', 'we', 'We', 'my', 'My', 'ours', 'Ours', 'us', 'Us']
    word_list_lower = [word.lower() for word in word_list]
    pronoun_pattern = r'\b(?:' + '|'.join(personal_pronouns) + r')\b'
    paragraph_text = ' '.join(word_list_lower)
    pronoun_occurrences = re.findall(pronoun_pattern, paragraph_text)
    pronoun_occurrences = re.findall(pronoun_pattern, paragraph_text)
    pronoun_count = len(pronoun_occurrences)
    return pronoun_count

personal_pronoun_all_files = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    x = count_personal_pronouns(filtered_words)
    personal_pronoun_all_files.append(x)

def write_list_to_csv_column(data_list, column_name, csv_file):
    df = pd.read_csv(csv_file)
    df[column_name] = data_list
    df.to_csv(csv_file, index=False)    

write_list_to_csv_column(personal_pronoun_all_files, 'PERSONAL PRONOUNS', 'Output Data Structure.csv')

#1.1. Modifying Stopwords and Cleaning all the articles
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def import_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()  # Split the content into separate words using whitespace as the delimiter
            return words
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []

file_path = 'StopWords_Auditor.txt'
words_list = import_txt_file(file_path)
words_list_1 = words_list

file_path = 'StopWords_Currencies.txt'
words_list_2 = import_txt_file(file_path)

file_path = 'StopWords_DatesandNumbers.txt'
words_list_3 = import_txt_file(file_path)

file_path = 'StopWords_Generic.txt'
words_list_4 = import_txt_file(file_path)

file_path = 'StopWords_GenericLong.txt'
words_list_5 = import_txt_file(file_path)

file_path = 'StopWords_Geographic.txt'
words_list_6 = import_txt_file(file_path)

file_path = 'StopWords_Names.txt'
words_list_7 = import_txt_file(file_path)

words_addition = words_list_1 + words_list_2 + words_list_3 + words_list_4 + words_list_5 + words_list_6 + words_list_7

added_words = set(words_addition)

stpwrd = nltk.corpus.stopwords.words('english')
stpwrd.extend(added_words)

final_stopwords = list(map(str.lower, stpwrd))
final_set_stopwords = set(final_stopwords)

  #1 Reading content of txt file
def read_txt_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      text = file.read()
  except UnicodeDecodeError:
    # If 'utf-8-sig' fails, try with 'latin-1' encoding
    with open(file_path, 'r', encoding='latin-1') as file:
      text = file.read()
  return text

  #2 Tokenizing the text
def tokenize_text(text):
  words = nltk.word_tokenize(text)
  return words

  #3 Removing stopwords
def remove_stopwords(words):
  filtered_words = [word for word in words if word.lower() not in final_stopwords]
  return filtered_words

  #4 Saving a new file
def write_filtered_text(file_path, filtered_text):
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(' '.join(filtered_text))

  # Making a file reader for loop
import numpy as np
prefix = list(range(37, 151))

original_list = prefix
prefix_list = [str(element) for element in original_list]
# print(prefix_list)

original_list = prefix_list
suffix = ".txt"

def add_suffix_to_element(element):
    return element + suffix

filename_list = list(map(add_suffix_to_element, original_list))
# print(filename_list)

filename_list.remove('44.txt')
filename_list.remove('57.txt')
filename_list.remove('144.txt')

for filename in filename_list:
  text = read_txt_file(filename)
  words = tokenize_text(text)
  filtered_words = remove_stopwords(words)
  write_filtered_text(filename, filtered_words)

#1.2 Creating Positive and Negative Dictionary
from nltk.corpus import opinion_lexicon
from nltk.tokenize import word_tokenize

text = read_txt_file('negative-words.txt')
words = tokenize_text(text)
filtered_words = remove_stopwords(words)
write_filtered_text('new-negative-words.txt', filtered_words)

text = read_txt_file('positive-words.txt')
words = tokenize_text(text)
filtered_words = remove_stopwords(words)
write_filtered_text('new-positive-words.txt', filtered_words)

nltk.download('opinion_lexicon')

text = read_txt_file('new-positive-words.txt')
positive_words = tokenize_text(text)
def create_custom_positive_dictionary():
    positive_dictionary = positive_words
    return set(positive_dictionary)
positive_dictionary = create_custom_positive_dictionary()

text = read_txt_file('new-negative-words.txt')
negative_words = tokenize_text(text)
def create_custom_negative_dictionary():
    negative_dictionary = negative_words
    return set(negative_dictionary)
negative_dictionary = create_custom_negative_dictionary()

positive_list = list(positive_dictionary) #List containing positive words
negative_list = list(negative_dictionary) #List containing negative words

#1.3.1. Calculating and Extracting Positive and Negative Score in Output Data Structure
# Making a file reader for loop
import numpy as np
prefix = list(range(37, 151))

def find_common_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    return common_elements

common_positive_elements = find_common_elements(words, positive_list)
common_negative_elements = find_common_elements(words, negative_list)

original_list = prefix
prefix_list = [str(element) for element in original_list]
# print(prefix_list)

original_list = prefix_list
suffix = ".txt"

def add_suffix_to_element(element):
    return element + suffix

filename_list = list(map(add_suffix_to_element, original_list))
# print(filename_list)

filename_list.remove('44.txt')
filename_list.remove('57.txt')
filename_list.remove('144.txt')

# for filename in filename_list:
#     print(filename)
count_positive_words = []
count_negative_words = []

for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    common_positive_elements = find_common_elements(words, positive_list)
    x = len(common_positive_elements)
    count_positive_words.append(x)
    
    common_negative_elements = find_common_elements(words, negative_list)
    y = len(common_negative_elements)
    count_negative_words.append(y)

    #len(count_negative_words)=111 & same for positive (111 files)
    
output_csv = pd.read_csv('Output Data Structure.csv')

def write_list_to_csv_column(data_list, column_name, csv_file):
    df = pd.read_csv(csv_file)
    df[column_name] = data_list
    df.to_csv(csv_file, index=False)   
    
write_list_to_csv_column(count_positive_words, 'POSITIVE SCORE', 'Output Data Structure.csv')
write_list_to_csv_column(count_negative_words, 'NEGATIVE SCORE', 'Output Data Structure.csv')


#1.3.2. Calculating and Saving Polarity Index

def polarity_score_calculator(x,y):
  #x is Positive score and y is Negative score
    polarity_score = (0.000001) + ((x-y)/(x+y))
    return polarity_score
df = pd.read_csv('Output Data Structure.csv')

for index, row in df.iterrows():
    positive_score = row['POSITIVE SCORE']
    negative_score = row['NEGATIVE SCORE']
    result = polarity_score_calculator(positive_score, negative_score)
    df.at[index, 'POLARITY SCORE'] = result
    df.to_csv('Output Data Structure.csv', index=False) #File overwritten


#1.3.3. Calculating and Saving Subjectivity Index
import numpy as np

def read_txt_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      text = file.read()
  except UnicodeDecodeError:
    # If 'utf-8-sig' fails, try with 'latin-1' encoding
    with open(file_path, 'r', encoding='latin-1') as file:
      text = file.read()
  return text

  #2 Tokenizing the text
def tokenize_text(text):
  words = nltk.word_tokenize(text)
  return words

  #Loop to read the files
prefix = list(range(37, 151))
original_list = prefix
prefix_list = [str(element) for element in original_list]
original_list = prefix_list
suffix = ".txt"

def add_suffix_to_element(element):
    return element + suffix

filename_list = list(map(add_suffix_to_element, original_list))

filename_list.remove('44.txt')
filename_list.remove('57.txt')
filename_list.remove('144.txt')

  #Function of subjectivity_score
def subjectivity_score(positive_score, negative_score, total_words_after_cleaning):
    x = positive_score
    y = negative_score
    z = total_words_after_cleaning
    subjectivity_score = (x+y)/(z+0.000001)
    return subjectivity_score

  #Executing the loop to fill the values and save it
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    total_words_after_cleaning = len(words)
    
    for index, row in df.iterrows():
        positive_score = row['POSITIVE SCORE']
        negative_score = row['NEGATIVE SCORE']
        result = subjectivity_score(positive_score, negative_score, total_words_after_cleaning)
        df.at[index, 'SUBJECTIVITY SCORE'] = result
        df.to_csv('Output Data Structure.csv', index=False) #File overwritten

#5 Wordcount
  #Element Finder in stopwords or a list
  # element_to_find = 'you'

  # try:
  #     index = stopwords_for_word_count.index(element_to_find)
  #     print(f"Element found at index: {index}")
  # except ValueError:
  #     print("Element not found in the list.")
punctuations_list = ['“','”','’','.',',',',','(',')','?','{','}','-','/',':',';']
nltk_stpwrd = nltk.corpus.stopwords.words('english')
stopwords_for_word_count = punctuations_list + nltk_stpwrd

def read_txt_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      text = file.read()
  except UnicodeDecodeError:
    # If 'utf-8-sig' fails, try with 'latin-1' encoding
    with open(file_path, 'r', encoding='latin-1') as file:
      text = file.read()
  return text

  #2 Tokenizing the text
def tokenize_text(text):
  words = nltk.word_tokenize(text)
  return words

  #3 Removing stopwords
def remove_stopwords(words):
  filtered_words = [word for word in words if word.lower() not in stopwords_for_word_count]
  return filtered_words

word_count_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    word_count = len(filtered_words)
    word_count_list.append(word_count)

def write_list_to_csv_column(data_list, column_name, csv_file):
    df = pd.read_csv(csv_file)
    df[column_name] = data_list
    df.to_csv(csv_file, index=False)   

write_list_to_csv_column(word_count_list, 'WORD COUNT', 'Output Data Structure.csv')


#8 Average Word Length calculation and storing in csv
punctuations_list = ['?','!',',','.','"','(',')','-','“','”','’',':','%','@','#','$','^','&','*','<','>','/','{','}']
nltk_stpwrd = nltk.corpus.stopwords.words('english')
stopwords_for_word_count = punctuations_list + nltk_stpwrd

def read_txt_file(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8-sig') as file:
      text = file.read()
  except UnicodeDecodeError:
    # If 'utf-8-sig' fails, try with 'latin-1' encoding
    with open(file_path, 'r', encoding='latin-1') as file:
      text = file.read()
  return text

  #2 Tokenizing the text
def tokenize_text(text):
  words = nltk.word_tokenize(text)
  return words

  #3 Removing stopwords
def remove_stopwords(words):
  filtered_words = [word for word in words if word.lower() not in stopwords_for_word_count]
  return filtered_words

prefix = list(range(37, 151))
original_list = prefix
prefix_list = [str(element) for element in original_list]
original_list = prefix_list
suffix = ".txt"

def add_suffix_to_element(element):
    return element + suffix

filename_list = list(map(add_suffix_to_element, original_list))

filename_list.remove('44.txt')
filename_list.remove('57.txt')
filename_list.remove('144.txt')

#Using Loop to count number of words in each file and storing in a list
word_count_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    word_count = len(filtered_words)
    word_count_list.append(word_count)

#Using Loop to count number of characters in each file and storing in a list
character_count_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    character_count_individual = [len(text_item) for text_item in filtered_words]
    character_count = sum(character_count_individual)
    character_count_list.append(character_count) 
    
def write_list_to_csv_column(data_list, column_name, csv_file):
    df = pd.read_csv(csv_file)
    df[column_name] = data_list
    df.to_csv(csv_file, index=False)
    
# Perform element-wise division using list comprehension
avg_word_length_list = [a / b for a, b in zip(character_count_list, word_count_list)]
write_list_to_csv_column(avg_word_length_list, 'AVG WORD LENGTH', 'Output Data Structure.csv')


#2 & 3: Avg sentence length or Avg number of words per sentence
word_count_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    word_count = len(filtered_words)
    word_count_list.append(word_count)

sentence_count_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)
    sentence_count_list.append(num_sentences)

avg_word_length_list = [a / b for a, b in zip(word_count_list, sentence_count_list)]
write_list_to_csv_column(avg_word_length_list, 'AVG SENTENCE LENGTH', 'Output Data Structure.csv')
write_list_to_csv_column(avg_word_length_list, 'AVG NUMBER OF WORDS PER SENTENCE', 'Output Data Structure.csv')

#6 Syllable count per word (total syllables of a file / total word count of a file)    
def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

list_syllable_count_all_files = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    list_syllable_count_individual_file = []
    for element in filtered_words:
        x = syllable_count(element)
        list_syllable_count_individual_file.append(x)
    y = sum(list_syllable_count_individual_file)
    list_syllable_count_all_files.append(y)

syllable_per_word = [a / b for a, b in zip(list_syllable_count_all_files, word_count_list)]
write_list_to_csv_column(syllable_per_word, 'SYLLABLE PER WORD', 'Output Data Structure.csv')


#4 Complex Word Count of individual files and saving them in Output
complex_word_count_all_files_list = []
for filename in filename_list:
    text = read_txt_file(filename)
    words = tokenize_text(text)
    filtered_words = remove_stopwords(words)
    complex_word_count_individual_file = 0
    for element in filtered_words:
        x = syllable_count(element)
        if x > 2:
            complex_word_count_individual_file += 1
        else:
            complex_word_count_individual_file = complex_word_count_individual_file
    complex_word_count_all_files_list.append(complex_word_count_individual_file)
    
write_list_to_csv_column(complex_word_count_all_files_list, 'COMPLEX WORD COUNT', 'Output Data Structure.csv')

#2.2. Percentage Complex Words and storing them in Output Data Structure.csv
complex_word_count_all_files_list
word_count_list

complex_words_fraction_all_files = [a / b for a, b in zip(complex_word_count_all_files_list, word_count_list)]

def multiply_list_elements_with_constant(lst, constant):
    result_list = []
    for element in lst:
        result_list.append(element * constant)
    return result_list

multiply_list_elements_with_constant(complex_words_fraction_all_files, 100)

complex_words_percentage_all_files = multiply_list_elements_with_constant(complex_words_fraction_all_files, 100)

write_list_to_csv_column(complex_words_percentage_all_files, 'PERCENTAGE OF COMPLEX WORDS', 'Output Data Structure.csv')


#2.3. Gunning Fog Index for each file and saving as output in Output Data Structure.csv
def fog_index(avg_sentence_length, percentage_complex_words):
    x = avg_sentence_length
    y = percentage_complex_words
    fog_index = 0.4 * (x+y)
    return fog_index    

avg_word_length_list
complex_words_percentage_all_files

gunning_fog_index_all_files = []
i = 0
for x in avg_word_length_list:
    y = complex_words_percentage_all_files[i]
    z = fog_index(x,y)
    gunning_fog_index_all_files.append(z)
    i+=1
    
write_list_to_csv_column(gunning_fog_index_all_files, 'FOG INDEX', 'Output Data Structure.csv')
