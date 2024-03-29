import re

set_of_signs = ("+", "-", "*", "/", "^", "!")
brackets = [["(", ")"], ["{", "}"], ["[", "]"], ["|", "|"]]


def findLastIndex(str, x):
    index = -1
    for i in range(0, len(str)):
        if str[i] == x:
            index = i
    return index


def prev_next_chars(entry, main_index, include_space):
    # assuming spaces exist
    # format: >>aa<< +/*- >>bb<<
    prevSpaceNotFound = True
    nextSpaceNotFound = True
    prev_char = ""
    next_char = ""
    if include_space:
        temp_i = main_index - 1
    else:
        temp_i = main_index
    bracket_skip = 0
    while prevSpaceNotFound:
        temp_i -= 1
        if temp_i <= 0:
            prev_index = 0
            break
        for bracket in brackets:
            if entry[temp_i] == bracket[1]:
                bracket_skip += 1
            if entry[temp_i] == bracket[0]:
                prev_index = temp_i + 1
                prevSpaceNotFound = False
            elif (
                entry[temp_i] == " "
                or entry[temp_i] == ":"
                or entry[temp_i - 1 : temp_i + 1] == " - "
                or entry[temp_i - 1 : temp_i + 1] == " + "
                or entry[temp_i - 1 : temp_i + 1] == " * "
                or entry[temp_i - 1 : temp_i + 1] == " / "
                or entry[temp_i - 1 : temp_i + 1] == " ^ "
            ):
                prev_index = temp_i + 1
                prevSpaceNotFound = False

    if include_space:
        temp_i = main_index + 1
    else:
        temp_i = main_index
    bracket_skip = 0
    while nextSpaceNotFound:
        if temp_i >= len(entry) - 1:
            next_index = len(entry)
            break
        for bracket in brackets:
            # print(
            #     f'''{main_index} Characters: length:{len(entry)}, tempi:{temp_i}''')
            if entry[temp_i] == bracket[0]:
                bracket_skip += 1
            if entry[temp_i - 1] == "j":
                if entry[temp_i] == " " or entry[temp_i] == bracket[1] or entry[temp_i] == ":":
                    next_index = temp_i
                    nextSpaceNotFound = False
            elif (
                entry[temp_i] == " "
                or entry[temp_i - 1 : temp_i + 1] == " - "
                or entry[temp_i - 1 : temp_i + 1] == " + "
                or entry[temp_i - 1 : temp_i + 1] == " * "
                or entry[temp_i - 1 : temp_i + 1] == " / "
                or entry[temp_i - 1 : temp_i + 1] == " ^ "
            ):
                next_index = temp_i + 1
                nextSpaceNotFound = False
            elif entry[temp_i] == bracket[1] or entry[temp_i] == ":":
                next_index = temp_i
                nextSpaceNotFound = False
        temp_i += 1
    prev_char = entry[prev_index:main_index].strip()
    next_char = entry[main_index:next_index].strip()
    return [prev_char, next_char, entry]


def plus_minus_combo_check(entry):
    if "-  +" in entry or " +  - " in entry:
        entry = entry.replace(" +  - ", " - ")
        entry = entry.replace(" -  + ", " - ")
    elif "-  -" in entry:
        entry = entry.replace(" -  - ", " + ")
    return entry


def CenterOf_bracket_from_in(bracket, initI, endI, entry):
    value_indexes = []
    us_entry = entry[initI:endI]
    if bracket[0] == bracket[1]:
        half_amt = len(re.findall(f"\{bracket[0]}", us_entry)) / 2
        for i, a in enumerate(us_entry, start=0):
            left_str = us_entry[:i]
            right_str = us_entry[i:]
            left_amt = len(re.findall(f"\{bracket[0]}", left_str))
            right_amt = len(re.findall(f"\{bracket[0]}", right_str))
            if left_amt == right_amt:
                value_indexes.append(i)
        if value_indexes[0] and value_indexes[-1]:
            return [value_indexes[0], value_indexes[-1], bracket]
    else:
        brac0End = findLastIndex(us_entry, bracket[0])
        brac1Start = us_entry.find(bracket[1], brac0End)
        if brac0End != -1 and brac1Start != -1:
            return [brac0End + 1, brac1Start, bracket]
