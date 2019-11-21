blogs = dict()


def menu():
    # show the user available blogs
    # Let the user make a choice
    # Do sth with that choice
    # Eventually exit

    print_blogs()

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))