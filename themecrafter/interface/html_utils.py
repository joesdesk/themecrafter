# Utilities to aid handling the tags passed to the html interface.

def breaknodes(node_elem):
    '''If a node element is too long,
    break it into smaller pieces.
    '''
    l = 0
    for tok in node_elem.find_all('tok'):
        l += len(tok.string)
        if l > 50:
            tok.insert_before(' ')
            l = 0

def offset2space(elem):
    '''Recursively finds all elements with an offset attribute and
    inserts the appropriate space between tags.
    Removes the unneeded offset attribute in the process.'''
    offset = 0
    for t in elem.find_all(True, {'offset':True}, recursive=False):

        loc_offset = int( t.get('offset') )            
        space_len = loc_offset - offset
        space = ' '*space_len
        
        t.insert_before(space)
        offset2space(t)

        text_len = int(t.get('len'))
        offset = loc_offset + text_len
        
        del t['offset']
        del t['len']
        
def unwrap(tag):
    '''If a tag has a style attribute, don't unwrap it.'''
    if not tag.has_attr('style'):
        tag.unwrap()
        
        