from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('c','Test Create Blog', 'Test Author','q')
            app.menu()
            self.assertIsNotNone(app.blogs['Test Create Blog'])

    def test_print_blog(self):
        blog = Blog('Test','Test Author')
        app.blogs['Test'] = blog
        with patch ('builtins.print') as mock_print:
            app.print_blogs()
            mock_print.assert_called_with('- Test by Test Author (0 posts)')

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mock_print_blog:
            with patch('builtins.input',return_value = 'q') as mock_input:
                app.menu()
                mock_print_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mock_print:
            app.menu()
            mock_print.assert_called_with(app.MENU_PROMPT)

    def test_ask_create_blog(self):
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('Test','Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}
        with patch('builtins.input',return_value = 'Test'):
            with patch ('app.print_posts') as mock_print_posts:
                app.ask_read_blog()
                mock_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}
        blog.create_post('Test Post','Test Content')

        with patch('app.print_post') as mock_print_post:
            app.print_posts(blog)

            mock_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Test','Test Content')
        expected_print = '''
    --- Test ---
    Test Content
    '''
        with patch('builtins.print') as mock_print:
            app.print_post(post)
            mock_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        blog = Blog('Test','Test Author')
        app.blogs = {'Test':blog}
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ('Test','Test Title','Test Content')

            app.ask_create_post()

            self.assertEqual(blog.posts[0].title,'Test Title')
            self.assertEqual(blog.posts[0].content, 'Test Content')
