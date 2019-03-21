import sys


def getreply():
    '''
    读取交互式用户的回复键，即使stdin重定向到某个文件或者管道
    '''
    if sys.stdin.isatty():
        return input('?')
    else:
        if sys.platform[:3] == 'win':
            import msvcrt
            msvcrt.putch(b'?')
            key = msvcrt.getche()
            msvcrt.putch(b'\n')
            return key
        else:
            assert False, 'Platform not supported'
            # linux?: open('/dev/tty').readline()[：-1]

def more(text, numlines=10):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:
            print(line)
        if lines and getreply() not in ['Y', 'y']:
            break


if __name__ == "__main__":
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())