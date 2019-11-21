from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):
    def test_print_blogs(self):
        blog = Blog('Test Title','Test Author')
        app.blogs = {'Test Title': blog}

        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test Title by Test Author (0 posts)')

