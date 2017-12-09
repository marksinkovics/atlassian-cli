""" Test dialog """

from mock import patch

from atlassian_cli.config.helpers import Dialog

#pylint: disable=R0201

class DialogTestCase:
    """ Test base Dialog """

    @patch('builtins.input')
    def test_ask_question(self, mock_input):
        """ ask a question from std input """
        mock_input.return_value = 'answer'
        dialog = Dialog()
        assert dialog.ask_question('question') == 'answer'
        mock_input.assert_called_with('question')

    @patch('getpass.getpass')
    def test_ask_secure_question(self, mock_getpass):
        """ ask a secret question from std input """
        mock_getpass.return_value = 'secure_answer'
        dialog = Dialog()
        assert dialog.ask_secure_question('secure_question') == 'secure_answer'
        mock_getpass.assert_called_with(prompt='secure_question')
