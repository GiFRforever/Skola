class HTMLElement:
    def __init__(self, tag, content="", *args, **kwargs) -> None:
        self.tag = tag
        self.content: str = "".join(content, *args)
        self.attributes = kwargs

    def __add__(self, other) -> str:
        if isinstance(other, str):
            return self.render() + other
        elif isinstance(other, HTMLElement):
            return self.render() + other.render()
        else:
            raise TypeError(f"Can't add HTMLElement and {type(other)} together.")

    def __radd__(self, other) -> str:
        return other + self

    def render(self) -> str:
        attribute_str: str = "".join(
            [f' {key}="{value}"' for key, value in self.attributes.items()]
        )
        return f"<{self.tag}{attribute_str}>{self.content}</{self.tag}>"


class HTMLElementClosed(HTMLElement):
    def __init__(self, tag, *args, **kwargs) -> None:
        super().__init__(tag, *args, **kwargs)

    def render(self) -> str:
        attribute_str: str = "".join(
            [f' {key}="{value}"' for key, value in self.attributes.items()]
        )
        return f"<{self.tag}{attribute_str}>"


class HTMLDocument:
    def __init__(self) -> None:
        self.head: HTMLElement = HTMLElement("head")
        self.body: HTMLElement = HTMLElement("body")

    def add_element(self, element, target="body") -> None:
        if target == "head":
            self.head.content += element.render()
        elif target == "body":
            self.body.content += element.render()

    def render(self) -> str:
        html: str = "<html>\n"
        html += self.head.render() + "\n"
        html += self.body.render() + "\n"
        html += "</html>"
        return html


class Input(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("input", *args, **kwargs)


class A(HTMLElementClosed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("a", *args, **kwargs)


class Img(HTMLElementClosed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("img", *args, **kwargs)


class Br(HTMLElementClosed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("br", *args, **kwargs)


class Meta(HTMLElementClosed):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("meta", *args, **kwargs)


class Title(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("title", *args, **kwargs)


class H1(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h1", *args, **kwargs)


class H2(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h2", *args, **kwargs)


class H3(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h3", *args, **kwargs)


class H4(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h4", *args, **kwargs)


class H5(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h5", *args, **kwargs)


class H6(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("h6", *args, **kwargs)


class P(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("p", *args, **kwargs)


class Div(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("div", *args, **kwargs)


class Label(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("label", *args, **kwargs)


class Table(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("table", *args, **kwargs)


class Form(HTMLElement):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__("form", *args, **kwargs)


doc: HTMLDocument = HTMLDocument()

# Create elements
meta: HTMLElement = HTMLElement("meta", charset="UTF-8")
title: HTMLElement = HTMLElement("title", "Formulář")
header: HTMLElement = HTMLElement("h1", "Formulář!", style="color: blue;")
paragraph: HTMLElement = HTMLElement("p", "Prosím vyplňte formulář.")
form: HTMLElement = HTMLElement(
    "form",
    HTMLElement(
        "label",
        "Popis: " + Input(type="text", name="popis"),
    ).render()
    + HTMLElement(
        "label",
        "Cena: " + Input(type="text", name="cena"),
    ).render()
    + HTMLElement(
        "label",
        "Množství: " + Input(type="text", name="množství"),
    ).render()
    + Input(type="submit", value="Odeslat"),
    action="praxe\\stuf.html",
    method="GET",
)

# Add elements to the document
doc.add_element(title, target="head")
doc.add_element(header)
doc.add_element(paragraph)
doc.add_element(form)

# Render the HTML code
html_code: str = doc.render()
# write the HTML code to a file in UTF-8 encoding
with open("form.html", "w", encoding="utf-8") as f:
    f.write(html_code)
print(html_code)
