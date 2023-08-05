homework = """homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

# replace extra lines between sentences
stage_1 = homework.replace('\n', '')

# split all sentences by dot
stage_2  = stage_1.split('.')

# remove whitespaces at the ends of sentences and filter out blank strings
stage_3 = [row.strip() for row in stage_2 if len(row)>0]

# add whitespace after colon
stage_4 = [row.replace(':', ': ') for row in stage_3]

# create sentence from the last words of each sentence
last_sentence = []
for row in stage_4:
    last_sentence.append(row.split()[-1])

last_sentence = ' '.join(last_sentence)
stage_4.append(last_sentence)

# make words at lower case to process mistakes iz->is
stage_5 = [row.lower() for row in stage_4]

# fix mistakes iz->is
stage_6 = [row.replace(' iz ', ' is ') for row in stage_5]
# fix whitespace at fix“iZ”
stage_6 = [row.replace('“iz”', ' “iz”') for row in stage_6]

# capitalize all sentences
stage_7 = [row.capitalize() for row in stage_6]

# add dot to all sentences
stage_8 = [f'{row}.' for row in stage_7]

# create final string by joining all sentences at one place
final_result = ' '.join(stage_8)

print(f"Number of whitespaces: {final_result.count(' ')}")
