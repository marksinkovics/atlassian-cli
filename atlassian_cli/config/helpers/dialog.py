""" Classes to remove and update config file """

import getpass

class Dialog:
    """ Helper class to ask questions from std in"""
    # pylint: disable=R0201
    @classmethod
    def ask_question(cls, question):
        """ ask a simple question """
        answer = input(question)
        return answer

    @classmethod
    def ask_secure_question(cls, question):
        """ ask a secure question """
        secure = getpass.getpass(prompt=question)
        return secure
