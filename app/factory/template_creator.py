from .html_factory import HtmlFactory


class TemplateCreator:
    """Template creator class"""
    def __init__(self, html_dict, html_file):
        self.html_dict = html_dict
        self.html_file = html_file
        self.html_factory = HtmlFactory()
        
    def get_file_full_path(self):
        return "mediafiles/generated_templates/" + self.html_file

    def start_html(self):
        content =self.html_factory.get_html_class("extend").build_html()
        content += self.html_factory.get_html_class("start_block").build_html()
        return content
    
    def end_html(self):
        return self.html_factory.get_html_class("end_block").build_html()

    def introduction_html(self):
        factory = self.html_factory
        content = factory.get_html_class("title", self.html_dict["title"], 1).build_html()
        content += '<br>'
        content += factory.get_html_class("paragraph", self.html_dict["intro"], 1).build_html() + '<br>'
        return content
    
    def content_html(self):
        factory = self.html_factory
        content = ""
        for element in self.html_dict["content"]:
            content += factory.get_html_class(element[0], element[1]).build_html() + '<br>'
        return content

    def build_html(self):
        """build html"""
        return (self.start_html() +
                self.introduction_html() +
                self.content_html() +
                self.end_html())

    def save_html(self):
        """save html"""
        with open(self.get_file_full_path(), "w") as f:
            f.write(self.build_html())
