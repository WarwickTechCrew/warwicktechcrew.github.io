'''
Script to scrape all show data from tech crew website into yaml files, used when converting to jekyll
'''


from bs4 import BeautifulSoup
from lxml import etree
from requests import head
import yaml

# parse the html file
# soup = BeautifulSoup(open('index.html'), 'html.parser')
# print(soup.prettify())


website = etree.parse('index.html', etree.HTMLParser())
root = website.getroot()
show_block = root.find('.//div[@id="accordion"]')

years = show_block.findall('.//div[@role="tabpanel"]')
for year in years:
    heading_label = year.attrib.get('aria-labelledby')
    heading = show_block.find(f'.//div[@id="{heading_label}"]/h4/a').text.strip()
    print(heading)
    terms = year.findall('.//div[@class="col-md-4"]')

    year_terms = []
    for term in terms:
        term_name = term.find('.//h5').text.strip()
        print(f'\t{term_name}')
        shows = term.findall('./ul/li')

        shows_info = []
        for show in shows:

            show_info = {}

            show_info['name'] = show.find('./h6').text.strip()
            show_info['society'] = ' '.join(show.find('./h6/small').text.split())
            
            details = show.findall('.//li')
            venue = details[0].text.strip()
            show_info['venue'] = venue

            people = []
            links = []
            for detail in details[1:]:
                det = {}
                detail_text = detail.text.strip().split(':')
                # print(detail_text)
                link = detail.find('./a')
                if link is not None:
                    det['name'] = detail_text[0].strip()
                    det['label'] = ' '.join(link.text.split())
                    det['url'] = link.attrib.get('href')
                    links.append(det)
                else:
                    det['role'] = detail_text[0].strip()
                    det['name'] = detail_text[1].strip()
                    people.append(det)
            
            if len(people) > 0:
                show_info['people'] = people
            if len(links) > 0:
                show_info['links'] = links
                
            shows_info.append(show_info)

        # print(shows_info)
        year_terms.append({'name': term_name, 'shows': shows_info})
    # print(year_terms)

    year = {'year': heading, 'terms': year_terms}

    filename = heading[2:4] + heading[9:11] + '.yaml'
    print(filename)

    class MyDumper(yaml.SafeDumper):
    # HACK: insert blank lines between top-level objects
    # inspired by https://stackoverflow.com/a/44284819/3786245
        def write_line_break(self, data=None):
            super().write_line_break(data)

            if len(self.indents) < 3:
                super().write_line_break()


    with open(filename, 'w') as file:
        stream = yaml.dump(year, sort_keys=False, Dumper=MyDumper).replace('-   ', '  - ').replace('terms:\n', 'terms:')
        file.write(stream)
    print(stream)
