from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words

def print_words(words):
    for word in words:
        print(word)

def main():
    words = fetch_words()
    print_words(words)

# execute if not imported into module
if __name__ == "__main__":
    main()
