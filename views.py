def index():
    with open("templates/index.html") as template:
        return template.read()
    
def hello():
    with open("templates/hello_page.html") as template:
        return template.read()