
#   Write a program that creates gramatically valid English sentences.
#   Here, we consider a sentence to be gramatically correct when it follows the simple English grammar of the form: Article Adjective Noun Verb. That is, even the sentence A insect fly. is, for the moment, considered correct. Use the files inside the data folder: nouns, verbs and adjectives. HINT: read them at put content into 3 lists.
#   Extend the above program to generate all possible sentences with the given words.

with open('C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/data/verbs') as verbs_file:
    verbs = verbs_file.read().split('\n')

with open('C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/data/nouns') as nouns_file:
    nouns = nouns_file.read().split('\n')

with open('C:/Users/23300/IdeaProjects/docker_notebooks/notebooks/data/adjectives') as adjectives_file:
    adjectives = adjectives_file.read().split('\n')

print(set([a + ' ' + n + ' ' + v for a in adjectives for n in nouns for v in verbs]))