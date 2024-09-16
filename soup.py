from bs4 import BeautifulSoup

class soupTemplates():
    def parseLinks(self):
        links = []
        divs = self.soup.find_all('div', class_='SoaBEf')
        
        for div in divs:
            a_tag = div.find('a', href=True)
            heading_tag = div.find(attrs={"role": "heading"})
            
            if a_tag and heading_tag:
                link = a_tag['href']
                heading = heading_tag.get_text().replace('\n', '').strip()
                links.append({"link": link, "heading": heading})
        
        return links
        """ Example of return value
        [
            {"link": "google.com", "heading": "heading"},
            {"link": "google.com", "heading": "heading"},
        ] 
        """

    def get_title(self) -> str:
        """Get the title of the HTML page."""
        title_tag = self.soup.find('title')
        return title_tag.string if title_tag else None

class Soup(soupTemplates):
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.html = html

    def print_response(self):
        print(self.html)

if __name__ == "__main__":
    html_response = ""

    with open('result_34', 'r') as f:
        html_response = f.read()

    s = Soup(html_response)
    print(s.get_title())
    print(s.parseLinks())
    #soup.print_response()
