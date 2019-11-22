from blog import Blog

blogs = dict()
MENU_PROMPT = "Enter 'c' to create a blog,'l' to list blogs, 'r' to read one, 'p' to post or 'q' to quit"
POST_TEMPLATE = '''
    --- {} ---
    {}
    '''

def menu():
    # show the user available blogs
    # Let the user make a choice
    # Do sth with that choice
    # Eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    title = input("Enter a title")
    name = input("Enter your name")
    blog = Blog(title,name)
    blogs[title] = blog


def ask_read_blog():
    title = input("Enter the blog title:")
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title,post.content))



def ask_create_post():
    blog_name = input("Enter the blog title")
    title = input("Enter your post title")
    content = input("Enter your post content")

    blogs[blog_name].create_post(title,content)
