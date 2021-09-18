import pyperclip


def tag_func():
    

def make_tag(c_func, tag="{}", md=True, f_name="answers.md"):
    task_name = pyperclip.paste()

    tag_val = tag_func()
    tag_str = tag.format(tag_val)

    with open(f_name, "a", encoding='utf-8') as f:
        string = f'|{task_name}|{tag_str}|'
        print(string, file=f)
    pyperclip.copy(tag_str)

make_tag(tag_func)
