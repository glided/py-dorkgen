import itertools


class KFT_Dork:
    # Make a <keyword><pformat><ptype> format dork.
    def __init__(self, pathKeyWords: str, pathPageType: str, pathPageFormat: str):
        self.kw = self.readTextFileAsList(pathKeyWords)
        self.pformats = self.readTextFileAsList(pathPageFormat)
        self.ptypes = self.readTextFileAsList(pathPageType)

    def createString(self):
        # Where the actual dorks are made
        with open('Dorks.txt', 'w', encoding='utf8') as dorkWriter:
            for permutation in itertools.product(self.kw, self.pformats, self.ptypes):
                dorkWriter.write('{} {} {}\n'.format(*permutation))

    @staticmethod
    def readTextFileAsList(filePath: str) -> list[str]:
        with open(filePath, 'r', encoding='utf8') as f:
            return [line.strip() for line in f]
