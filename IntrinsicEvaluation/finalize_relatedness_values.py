__author__ = 'kjtdi'

# We use 3 sinhala native speakers to evaluate relatedness between 2 words.
# Ater that we find the average relatedness between two words using this script and save them to a file.

import codecs

# save final scores in this file
f_w = codecs.open("./WordSim/wordsim353_sinhala_final.txt", 'w', encoding='utf-8')

# read relatedness scores given by each native speaker one by one
scores = []
j = 1
with codecs.open("./WordSim/wordsim353_sinhala.txt", encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.rstrip()
        a, b, sim = line.split("\t")
        scores.append(float(sim.strip()))
        j += 1

print(len(scores))

scores2 = []
j = 1
with codecs.open("./WordSim/wordsim353_sinhala_1.txt", encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.rstrip()
        a, b, sim = line.split("\t")
        scores2.append(float(sim.strip()))

print(len(scores2))

j = 1
with codecs.open("./WordSim/wordsim353_sinhala_2.txt", encoding='utf-8', errors='ignore') as f:
    i = 0
    for line in f:
        line = line.rstrip()
        a, b, sim = line.split("\t")
        sim = float(sim.strip())
        final_score = round((sim + scores[i] + scores2[i]) / 3.0, 2)  # find the average score
        f_w.write(a + "\t" + b + "\t" + str(final_score) + "\n")
        i += 1

f_w.close()
