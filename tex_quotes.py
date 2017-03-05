import sys
def replace_quotes(text):
    flag = False
    new_text = ''
    for char in text:
        if char == '\"':
            if flag:
                char = "''"
                flag = False
            else:
                char = '``'
                flag = True
        new_text += char
    return new_text

def main():
    print replace_quotes(sys.stdin.readlines())
    return 0
if __name__ == '__main__':
    main()
    
