import pyperclip


def tag_func():
    pass


def grodno_tag():
    make_tag(tag_func, tag="grodno{{{}}}")


def make_tag(c_func, tag="{}", f_name="answers.md"):
    task_name = pyperclip.paste()

    tag_val = tag_func()
    tag_str = tag.format(tag_val)
    print("Flag:", tag_str)

    pyperclip.copy(tag_str)

    print("Accepted?:", end=' ')

    if input():
        pyperclip.copy(task_name)
    else:
        with open(f_name, "a", encoding='utf-8') as f:
            string = f'|{task_name}|{tag_str}|'
            print(string, file=f)


if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:
        if argv[1] == "-g":
            grodno_tag()
        if argv[1] == "-p":
            make_tag(tag_func)
    else:
        print(tag_func())
