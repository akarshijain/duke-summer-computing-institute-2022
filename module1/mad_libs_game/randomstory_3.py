import random
  

def get_num_blanks(story):
    count = 0
    blank = '_'
    for pos, char in enumerate(story):
        if(char == blank):
            count += 1
    return count


def get_blank_pos(story):
    blank = '_'
    for pos, char in enumerate(story):
        if (char == blank):
            return pos


def buildCategories(categorylist):
    category_dict = {}
    for category in categorylist:
        words_in_category = readWordList(category)
        category_dict[category] = words_in_category
    return category_dict


def readWordList(categoryname):
    words_in_category = []
    with open(categoryname + '.txt') as file:
        for line in file:
            words_in_category.append(line.rstrip())
        return words_in_category


def replace_word_blank(story, char_start_pos, char_end_pos, category_dict):
    categoryname = story[char_start_pos:char_end_pos]
    word = random.choice(category_dict[categoryname])
    return story[:char_start_pos-1] + '{}'.format(word) + story[char_end_pos:]


def replace_num_blank(story, char_start_pos, char_end_pos):
    word = story[char_start_pos:char_end_pos]
    return story[:char_start_pos-1] + '[ num {} ]'.format(word) + story[char_end_pos:]


def randomStory(storyFile, wordTypes):
    with open(storyFile) as file:
        story = file.read()

    category_dict = buildCategories(wordTypes)

    num_blanks = get_num_blanks(story)
    for num in range(num_blanks):
        blank_pos = get_blank_pos(story)

        char_start_pos = blank_pos + 1
        char_end_pos = char_start_pos

        if(story[char_end_pos].isalpha()):
            while(story[char_end_pos].isalpha()):
                char_end_pos += 1
            story = replace_word_blank(story, char_start_pos, char_end_pos, category_dict)

        elif(story[char_end_pos].isdigit()):
            while(story[char_end_pos].isdigit()):
                char_end_pos += 1
            story = replace_num_blank(story, char_start_pos, char_end_pos)

    return story


if __name__ == "__main__":
    wordTypes = ["animal", "food", "greeting", "magiccreature", "place", "said", "thing", "time"]
    print(randomStory('story.txt', wordTypes), end='')
    pass