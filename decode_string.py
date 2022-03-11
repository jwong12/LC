

def decode_string(s: str) -> str:
    stack = []

    for c in s:
        if c == ']':
            decoded_str = ''
            last = stack.pop()
            while last != '[':
                decoded_str += last
                last = stack.pop()

            num = stack.pop()
            num_str = num
            while num.isnumeric() and stack:
                num = stack.pop()
                if num.isnumeric():
                    num_str += num

            if not num.isnumeric():
                stack.append(num)

            new_decoded = ''
            for _ in range(int(num_str[::-1])):
                new_decoded += decoded_str

            for i in range(len(new_decoded) - 1, -1, -1):
                stack.append(new_decoded[i])
        else:
            stack.append(c)

    res = ''
    for c in stack:
        res += c

    return res


if __name__ == '__main__':
    print(decode_string('3[a2[cd]]'))

