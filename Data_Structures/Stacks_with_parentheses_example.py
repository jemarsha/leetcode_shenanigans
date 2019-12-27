# is empty

class Stack:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return ' '.join([str(i) for i in self.items])

    def push(self, value):
        return self.items.append(value)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items is not None:
            return self.items[-1]

    def is_empty(self):
        return self.items == []

    def print(self):
        return self.items

        # for i in self.items:

        # print(self.items.pop())


def is_paran_balanced(paren_string):
    if paren_string is None:
        return False

    s = Stack()

    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]

        if paren in "({[":
            s.push(paren)  # if it's an open paren then push it
        else:
            if s.is_empty():  # otherwise if it's a close paren while the stack is empty then no match
                is_balanced = False  # so the function is false
                return is_balanced
            else:
                top = s.pop()  # if there is something in the stack then pop it but if not match still return false
                if not is_match(top, paren):
                    is_balanced = False
                    return is_balanced
        index += 1

    if s.is_empty() and is_balanced:
        return True

    return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True

    if p1 == "[" and p2 == "]":
        return True

    if p1 == "{" and p2 == "}":
        return True

    else:
        return False




if __name__ == '__main__':

    g= Stack()
    g.push(5)
    g.push(11)
    g.push('pie')
    g.push('w')
    g.pop()

    print(g)