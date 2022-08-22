def replace_blank(story, char_start_pos, char_end_pos):
    word = story[char_start_pos:char_end_pos]
    return story[:char_start_pos-1] + '[ {} ]'.format(word) + story[char_end_pos:]


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


def randomStory(storyFile, wordTypes):
    with open(storyFile) as file:
        story = file.read()

    num_blanks = get_num_blanks(story)
    for num in range(num_blanks):
        blank_pos = get_blank_pos(story)

        char_start_pos = blank_pos + 1
        char_end_pos = char_start_pos

        while(story[char_end_pos].isalnum()):
            char_end_pos += 1

        story = replace_blank(story, char_start_pos, char_end_pos)

    return story


if __name__ == "__main__":
    print(randomStory('story.txt', []), end='')
    pass