import re
import urllib.request
from urllib.error import HTTPError


# Definition dictionary refactoring by CHAT GPT
def get_definition(word):
    try:
        url = f"https://www.dictionary.com/browse/{word}"
        data = urllib.request.urlopen(url).read()
        data1 = data.decode("utf-8")

        m = re.search('<meta data-react-helmet="true" content=', data1)
        start = m.end() + 1
        end = start + 300
        newString = data1[start:end]

        m1 = re.search('See more.', newString)
        end = m1.start() - 1
        definition = newString[0:end]

        return definition
    except HTTPError as e:
        if e.code == 404:
            return "Word not found in the dictionary."
        else:
            return "An error occurred while fetching the definition."


def main():
    word = input("Enter a word: ")
    definition = get_definition(word)
    print(definition)


if __name__ == "__main__":
    main()
