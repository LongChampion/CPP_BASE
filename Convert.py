#!/usr/bin/env python3


def removeSpaceAndStrip(s: str) -> str:
    """Remove all adjacent spaces and strip the line"""
    if len(s) > 0 and "  " == s[:2]:
        s = "> " + s[2:]  # Preserve nested config line
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    return s.strip()


def isConfigLine(s: str) -> str:
    """Check if the given line contains configuration"""
    if 0 == len(s):
        return False  # Ignore empty lines
    if '#' == s[0]:
        return False  # Ignore comment lines
    return True


def readConfig() -> list:
    """Read config from file and return a list"""
    with open(".clang-format") as f:
        data = f.readlines()
    data = list(map(removeSpaceAndStrip, data))
    data = list(filter(isConfigLine, data))
    return data


def toString(data: list) -> str:
    """Convert configuration to a string that can be use in VSCode"""
    # Process nested configuration
    for i in range(len(data)):
        if ':' == data[i][-1]:
            data[i] += " {"
            for j in range(i + 1, len(data)):
                if '>' != data[j][0]:
                    break
                data[i] += data[j][1:].strip() + ', '
            data[i] = data[i][:-2] + '}'

    # Remove nested configuration
    data = list(filter(lambda s: '>' != s[0], data))

    # Final result
    return '{' + ', '.join(data) + '}'


def isNumber(s: str) -> bool:
    """Check if a string is integer"""
    try:
        s = int(s)
        return True
    except:
        return False


def toJson(data: list) -> str:
    """Convert configuration to JSON representation"""
    # Process nested configuration
    for i in range(len(data)):
        if '>' == data[i][0]:
            continue
        data[i] = data[i].replace("'", '"')

        L = [x.strip() for x in data[i].split(':')]
        if "" == L[1]:
            L[1] = '{'
            for j in range(i + 1, len(data)):
                if '>' != data[j][0]:
                    break
                l = [x.strip() for x in data[j][1:].split(':')]
                if not isNumber(l[1]):
                    l[1] = '"' + l[1] + '"'
                L[1] += '"' + l[0] + '": ' + l[1] + ', '
            L[1] = L[1][:-2] + '}'
        elif L[1][0] != '[':
            if '""' != L[1] and not isNumber(L[1]):
                L[1] = '"' + L[1] + '"'

        data[i] = '"' + L[0] + '": ' + L[1]

    # Remove nested configuration
    data = list(filter(lambda s: '>' != s[0], data))

    # Final result
    return '{' + ', '.join(data) + '}'


if "__main__" == __name__:
    data = readConfig()
    print(toString(data))
    print(toJson(data))
