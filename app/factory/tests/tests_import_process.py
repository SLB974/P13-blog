from unittest.mock import patch

from django.test import TestCase
from factory.core.import_process import ImportProcessor


class TestImportProcessor(TestCase):
    
    fixtures = [
        'article_fixture.json',
        'category_fixture.json',
        'article_category_fixture.json',
    ]
    
    def setUp(self):
        self.file = 'factory/tests/test_file.md'
        self.processor = ImportProcessor(self.file)
        
    @patch('factory.core.import_process.Parser')    
    def test_html_dict_returns_parser_html_dict(self, mockParser):
        expected = self.processor.html_dict
        self.assertTrue(mockParser.get_html_dict(), expected)
        
    def test_get_html_dict_returns_html_dict(self):
        self.assertTrue(self.processor.get_html_dict(), self.processor.html_dict)

    @patch('factory.core.import_process.Parser.get_html_dict')
    def test_check_file_returns_false_with_no_title(self, mockfile):
        mockfile.return_value={"content":[]}
        processor = ImportProcessor(self.file)
        expected_result = False
        expected_error = "Le fichier doit contenir un titre."
        actual_result = processor.check_file()
        actual_error = processor.get_error_message()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_error, actual_error)

    @patch('factory.core.import_process.Parser.get_html_dict')
    def test_check_file_returns_false_with_no_category(self, mockfile):
        mockfile.return_value={"title":"titre", "content":[]}
        processor = ImportProcessor(self.file)
        expected_result = False
        expected_error = "Le fichier doit contenir au moins une catégorie."
        actual_result = processor.check_file()
        actual_error = processor.get_error_message()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_error, actual_error)

    @patch('factory.core.import_process.Parser.get_html_dict')
    def test_check_file_returns_false_with_no_intro(self, mockfile):
        mockfile.return_value={"title":"titre", "category":"Python","content":[]}
        processor = ImportProcessor(self.file)
        expected_result = False
        expected_error = "Le fichier doit contenir une introduction."
        actual_result = processor.check_file()
        actual_error = processor.get_error_message()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_error, actual_error)

    @patch('factory.core.import_process.ArticleCreator.check_article')
    @patch('factory.core.import_process.Parser.get_html_dict')
    def test_check_file_returns_false_with_existing_article(self, mockfile, mockarticle):
        mockfile.return_value={"title":"Récursion en Python", 
                               "category":"Python",
                               "intro":"intro",
                               "content":[]}
        mockarticle.return_value=True
        processor = ImportProcessor(self.file)
        expected_result = False
        expected_error = "Cet article a déjà été importé."
        actual_result = processor.check_file()
        actual_error = processor.get_error_message()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_error, actual_error)

    @patch('factory.core.import_process.ArticleCreator.check_article')
    @patch('factory.core.import_process.Parser.get_html_dict')
    def test_check_file_returns_true(self, mockfile, mockarticle):
        mockfile.return_value={"title":"Récursion en Python", 
                               "category":"Python",
                               "intro":"intro",
                               "content":[]}
        mockarticle.return_value=False
        processor = ImportProcessor(self.file)
        expected_result = True
        expected_error = None
        actual_result = processor.check_file()
        actual_error = processor.get_error_message()
        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_error, actual_error)

    def test_get_file_name_returns_proper_value(self):
        actual = self.processor.get_file_name()
        expected = self.processor.html_file
        self.assertEqual(actual, expected)

    @patch('factory.core.import_process.FileSystemStorage.delete')
    def test_kill_file_calls_delete_on_storage(self, mockdelete):
        mockdelete.return_value=True
        processor = ImportProcessor(self.file)
        processor.kill_file()
        mockdelete.assert_called_once()

    @patch('factory.core.import_process.ArticleCreator.append_database')
    def test_process_calls_article_creator_append_database_method(self, mockappend):
        mockappend.return_value=True
        self.processor.process()
        mockappend.assert_called_once()

    @patch('factory.core.import_process.TemplateCreator.save_html')
    def test_process_calls_template_creator_save_method(self, mocktemplate):
        mocktemplate.return_value=True
        self.processor.process()
        mocktemplate.assert_called_once()

    @patch('factory.core.import_process.FileSystemStorage.delete')
    def test_process_calls_kill_file_when_ok(self, mockdelete):
        mockdelete.return_value=True
        processor = ImportProcessor(self.file)
        processor.process()
        mockdelete.assert_called_once()

    @patch('factory.tests.tests_import_process.ImportProcessor.check_file')
    @patch('factory.core.import_process.FileSystemStorage.delete')
    def test_process_calls_kill_file_when_not_ok(self, mockdelete, mockcheck):
        mockcheck.return_value=False
        mockdelete.return_value=True
        processor = ImportProcessor(self.file)
        try:
            processor.process()
        except Exception:
            pass
        mockdelete.assert_called_once()
    
    