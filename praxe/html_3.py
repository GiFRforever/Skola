class HTMLElement:
    def __init__(self, tag, content="", **kwargs) -> None:
        self.tag = tag
        self.content: str = content
        self.attributes = kwargs

    def render(self) -> str:
        attribute_str: str = "".join(
            [f' {key}="{value}"' for key, value in self.attributes.items()]
        )
        return f"<{self.tag}{attribute_str}>{self.content}</{self.tag}>"


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


Input = lambda *args, **kwargs: HTMLElement("input", *args, **kwargs).render()

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
