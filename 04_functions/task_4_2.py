from typing import List

homework = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""


def replace_blank_lines(str_in: str) -> str:
    # replace extra lines between sentences
    return str_in.replace('\n', '')


stage_1 = replace_blank_lines(homework)


def split_string_dot(str_in: str) -> List:
    # split all sentences by dot
    return str_in.split('.')


stage_2 = split_string_dot(stage_1)


def remove_whitespace(str_in: List) -> List:
    # remove whitespaces at the ends of sentences and filter out blank strings
    return [row.strip() for row in str_in if len(row) > 0]


stage_3 = remove_whitespace(stage_2)


def add_colon(str_in: List) -> List:
    # add whitespace after colon
    return [row.replace(':', ': ') for row in str_in]


stage_4 = add_colon(stage_3)


def sentence_last_words(str_in: List) -> List:
    # create sentence from the last words of each sentence
    last_sentence = []
    for row in str_in:
        last_sentence.append(row.split()[-1])

    last_sentence = ' '.join(last_sentence)
    str_in.append(last_sentence)
    return str_in


stage_5 = sentence_last_words(stage_4)


def correct_mistake(str_in: List) -> List:
    # make words at lower case to process mistakes iz->is
    str_in = [row.lower() for row in str_in]

    # fix mistakes iz->is
    str_in = [row.replace(' iz ', ' is ') for row in str_in]

    # fix whitespace at fix“iZ”
    return [row.replace('“iz”', ' “iz”') for row in str_in]


stage_6 = correct_mistake(stage_5)


def capitalize_sentence(str_in: List) -> List:
    # capitalize all sentences
    return [row.capitalize() for row in str_in]


stage_7 = capitalize_sentence(stage_6)


def add_dot(str_in: List) -> List:
    # add dot to all sentences
    return [f'{row}.' for row in str_in]


stage_8 = add_dot(stage_7)


def create_str(str_in: List) -> str:
    # create final string by joining all sentences at one place
    return ' '.join(str_in)


final_result = create_str(stage_8)

print(f"Number of whitespaces: {final_result.count(' ')}")
