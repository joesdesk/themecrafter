# https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-the-tree

# Using anchors, id vs name
# https://stackoverflow.com/questions/484719/html-anchors-with-name-or-id


from bs4 import BeautifulSoup


def ToHTML(docs):

    # HTML needs to be built from the inside out
    page = BeautifulSoup('', "lxml")
    
    for i, s in enumerate(docs):
        comment_tag = page.new_tag('comment')
        comment_tag['class'] = 'comment'
        comment_tag['id'] = i
        comment_tag.string = s
        page.append(comment_tag)
        
        lineskip_tag = page.new_tag('br')
        page.append(lineskip_tag)
    
    # Container for everything
    container = BeautifulSoup('', "lxml")
    bodytag = container.new_tag('body')
    container.append(bodytag)
    container.body.append(page)
    page = container
    
    container = BeautifulSoup('', "lxml")
    htmltag = container.new_tag('html')
    container.append(htmltag)
    container.html.append(page)
    page = container
        
    return page.prettify()