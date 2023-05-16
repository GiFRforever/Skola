class Element:
    id = None
    name = None
    class_ = None

    def __init__(self, id, name, class_):
        self.id = id
        self.name = name
        self.class_ = class_


class a(Element):
    href = None
    target = None

    def __init__(self, id, name, class_, href, target):
        super().__init__(id, name, class_)
        self.href = href
        self.target = target


class div(Element):
    def __init__(self, id, name, class_):
        super().__init__(id, name, class_)


class form(Element):
    action = None
    method = None

    def __init__(self, id, name, class_, action, method):
        super().__init__(id, name, class_)
        self.action = action
        self.method = method


class select(Element):
    def __init__(self, id, name, class_):
        super().__init__(id, name, class_)


class image(Element):
    src = None
    alt = None

    def __init__(self, id, name, class_, src, alt):
        super().__init__(id, name, class_)
        self.src = src
        self.alt = alt


class input(Element):
    type = None
    value = None
    placeholder = None

    def __init__(self, id, name, class_, type, value, placeholder):
        super().__init__(id, name, class_)
        self.type = type
        self.value = value
        self.placeholder = placeholder


class button(Element):
    type = None
    value = None

    def __init__(self, id, name, class_, type, value):
        super().__init__(id, name, class_)
        self.type = type
        self.value = value


class label(Element):
    def __init__(self, id, name, class_):
        super().__init__(id, name, class_)


class html(Element):
    lang = None

    def __init__(self, id, name, class_, lang):
        super().__init__(id, name, class_)
        self.lang = lang


class head(Element):
    def __init__(self, id, name, class_):
        super().__init__(id, name, class_)


class body(Element):
    def __init__(self, id, name, class_):
        super().__init__(id, name, class_)


def new_id():
    id: int = 0
    while True:
        yield id
        id += 1


id_gen = new_id()

template: str = """
<html lang="cs">

<head>
    <meta charset="UTF-8">
    <title>Formulář</title>
</head>

<body>
    <form action="clean.py" method="get">
        <div>
            <label> Popis: <input type="text" name="popis" /> </label>
        </div>
        <div>
            <label> Cena: <input type="text" name="cena" /> </label>
        </div>
        <div>
            <label> Množství: <input type="text" name="množství" /> </label>
        </div>
        <input type="submit" value="Odeslat" />
    </form>
</body>

</html>
"""
