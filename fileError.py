class NoErrorFromWords(Exception):

    def __init__(self, filename=''):
        self.message = """
                       No words were found at the file {0}
                       Please, change the main.py or fill the file with some words separeted
                       by spaces, only.
                       """.format(filename)
