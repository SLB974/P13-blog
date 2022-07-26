from .html_factory import HtmlProcessor


class TemplateCreator:
    """Template creator class"""
    def __init__(self, html_dict, html_file):
        self.html_dict = html_dict
        self.html_file = html_file
        
    def get_file_full_path(self):
        return "mediafiles/generated_templates/" + self.html_file

    def start_html(self):
        content =HtmlProcessor("gabarit_tag", "extends").build_html()
        content +=HtmlProcessor("gabarit_tag", "static").build_html()
        content += HtmlProcessor("gabarit_tag", "startblock").build_html()
        return content
    
    def end_html(self):
        return HtmlProcessor("gabarit_tag","endblock").build_html()

    def introduction_html(self):
        content = HtmlProcessor("title", (self.html_dict["title"][0], 1)).build_html()
        content += HtmlProcessor("br", 1).build_html()
        content += HtmlProcessor("paragraph", self.html_dict["intro"]).build_html()
        content += HtmlProcessor("br", 1).build_html()
        return content
    
    def content_html(self):
        content = ""
        for element in self.html_dict["content"]:
            content += HtmlProcessor(element[0], element[1]).build_html()
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
