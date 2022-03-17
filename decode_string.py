

def decode_string(s):
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


def decode_string_2stacks(s):
    count_stack = []
    string_stack = []
    num_str = decoded_str = ""
    i = 0

    while i < len(s):
        if s[i].isdigit():
            while s[i].isnumeric():
                num_str += s[i]
                i += 1
            continue

        elif s[i] == '[':
            count_stack.append(int(num_str))
            string_stack.append(decoded_str)
            num_str = decoded_str = ""

        elif s[i] == ']':
            if count_stack:
                k = count_stack.pop()
                temp_str = decoded_str
                for _ in range(k-1):
                    decoded_str += temp_str

            if string_stack:
                last_str = string_stack.pop()
                decoded_str = last_str + decoded_str

        else:
            decoded_str += s[i]

        i += 1

    return decoded_str


def decoded_string_rec(s):
    index = 0

    def recursion():
        nonlocal index
        result = ''
        while index < len(s) and s[index] != ']':
            if not s[index].isdigit():
                result += s[index]
                index += 1
            else:
                num_str = ''
                while s[index].isdigit():
                    num_str += s[index]
                    index += 1

                k = int(num_str)
                index += 1
                decoded_str = recursion()
                index += 1

                while k > 0:
                    result += decoded_str
                    k -= 1

        return result

    return recursion()


if __name__ == '__main__':
    print(decode_string_2stacks('3[a2[cd]]4[b]'))
    print(decoded_string_rec('3[a2[cd]]4[b]'))

