class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []

    def add_field(self, name, value):
        self.fields.append(
            (name, value)
        )
        return self

    def __str__(self):
        lines = list()
        lines.append("class {root_name}:".format(root_name=self.root_name))
        if len(self.fields) > 0:
            lines.append("  def __init__(self):")
            for f in self.fields:
                lines.append("    self.{name} = {value}".format(name=f[0], value=f[1]))
        else:
            lines.append("  pass")
        return "\n".join(lines)


cb = CodeBuilder('Person')
print(cb)
