# Builder pattern is used for piecewise construction of an object
# Builder component provides an API for constructing an object step by step

# text = "hello"
# parts = ["<p>", text, "</p>"]
# print("".join(parts))
#
# words = ["hello", "world"]
# parts = ["<ul>"]
# for w in words:
#     parts.append(f" <li>{w}</li>")
# parts.append("</ul>")
# print("\n".join(parts))

class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def append_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )

    def append_child_fluent(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
        return self  # used for chaining of calls

    def __str__(self):
        return str(self.__root)


builder = HtmlBuilder('ul')
builder.append_child('li', 'hello')
builder.append_child('li', 'world')
print("Ordinary builder:")
print(builder)
print("----")

# using builder with chain of calls
builder = HtmlBuilder('ul')
builder.append_child_fluent('li', 'hello').append_child_fluent('li', 'world')
print("Chained builder:")
print(builder)
print("----")

# creating builder instance through main class and then using it
builder = HtmlElement.create('ul')
builder.append_child_fluent('li', 'hello').append_child_fluent('li', 'world')
print(builder)
