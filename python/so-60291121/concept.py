TEXT=""",,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
Location:,,,ADDRESS_HERE_THAT I WANT
BUT IT CAN ALSO BE ACROSS,
MULTIPLE LINES, BUT NOT A SPECIFIC SET OF LINES,
AND IT ENDS AS ABRUPTLY,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
Location:,,,ADDRESS,IS,IN,ONE,LINE,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,
"""

in_location = False
tmp_location = None

def extract_location(l):
    global in_location
    global tmp_location
    if l.startswith("Location:"):
        in_location = True
        tmp_location = []
        tmp_location.append(l[13: -1]) # Don't need 'Location:,,,'
    else:
        if in_location:
            tmp_location.append(l)
            if l.endswith(',,,,,,,,,,,,,'):
                # The end
                in_location = False
                res =  " ".join(tmp_location)
                print(res[0:-13])  # Remove trailing commas


def main():
    for line in TEXT.split("\n"):
        # print(line)
        extract_location(line)


if __name__ == "__main__":
    main()
