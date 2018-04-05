import re

def getLines(data):
    idx2line = {}
    for line in data:
        line = line.split(' +++$+++ ')
        idx2line[line[0]] = line[-1]
    return idx2line
    
def getConvs(data):
    convs = []
    for line in data:
        line = line.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(',','').split()
        convs.append(line)
    return convs
data = open('movie_lines.txt').read()
data = data.split('\n')
idx2line = getLines(data)
del data

data = open('movie_conversations.txt').read()
data = data.split('\n')
convs = getConvs(data)
del data

questions = []
answers = []
for conv in convs:
    for i in range(len(conv)-1):
        questions.append(idx2line[conv[i]])
        answers.append(idx2line[conv[i+1]])

def clean_text(text):
    '''Clean text by removing unnecessary characters and altering the format of words.'''

    text = text.lower()
    
    text = re.sub(r"i'm", "i am", text)
    text = re.sub(r"he's", "he is", text)
    text = re.sub(r"she's", "she is", text)
    text = re.sub(r"it's", "it is", text)
    text = re.sub(r"that's", "that is", text)
    text = re.sub(r"what's", "that is", text)
    text = re.sub(r"where's", "where is", text)
    text = re.sub(r"how's", "how is", text)
    text = re.sub(r"\'ll", " will", text)
    text = re.sub(r"\'ve", " have", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"\'d", " would", text)
    text = re.sub(r"\'re", " are", text)
    text = re.sub(r"won't", "will not", text)
    text = re.sub(r"can't", "cannot", text)
    text = re.sub(r"n't", " not", text)
    text = re.sub(r"n'", "ng", text)
    text = re.sub(r"'bout", "about", text)
    text = re.sub(r"'til", "until", text)
    text = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", text)
    
    return text

for i in range(len(questions)):
    questions[i] = clean_text(questions[i])

for i in range(len(answers)):
    answers[i] = clean_text(answers[i])


for i in range(10):
    print questions[i]
    print answers[i]
    print 
        
