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

for i in range(10):
    print questions[i]
    print answers[i]
    print 
        
