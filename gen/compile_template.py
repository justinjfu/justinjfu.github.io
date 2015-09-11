from bs4 import BeautifulSoup
import sys

LOREM_IPSUM = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

def hello_world():
    new_soup = BeautifulSoup('<div> Hello World! </div>', "html.parser")
    return new_soup

def project_template(title="Title", description="Description", authors=None, links=None):
    # Build links
    link_str = '<div class="project-links"> <ul>'
    for link_name, link_url in links:
        link_str += '<li> <a href="%s">%s</a></li>' % (link_url, link_name)
    link_str += '</ul> </div> <!-- end project-links -->'

    # Build authors
    author_str = '<div class="project-authors"> <ul>'
    for author in authors:
        author_str += '<li>%s</li>' % (author)
    author_str += '</ul> </div> <!-- end project-authors -->'

    proj_str = """
        <div class="project-item">
            %(title)s
            <div class="row">
                <div class="col-md-6">
                    Hello
                </div>
                <div class="col-md-6">
                    %(authors)s
                    %(description)s
                    %(links)s
                </div>
            </div> <!-- end row -->
        </div> <!-- end project-item -->
        """ % {'title':title, 'description':description, 'links': link_str, 'authors':author_str}
    return BeautifulSoup(proj_str, 'html.parser')

def main():
    args = lambda : 0
    args.fname = sys.argv[1]
    with open(args.fname, 'r') as f:
        contents = f.read()
    soup = BeautifulSoup(contents)
    templates = soup.find_all(class_="pyp-template")
    for templ in templates:
        txt = templ.text.strip()
        res = eval(txt)
        if not isinstance(res, BeautifulSoup):
            #newtxt = "<div>%s</div>" % res
            newtxt = res
            new_soup = BeautifulSoup(newtxt, "html.parser")
        else:
            new_soup = res
        templ.replaceWith(new_soup)
    print soup.prettify()
 
if __name__ == "__main__":
    main()

