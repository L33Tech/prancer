import logging
from tokenize import COMMENT
from random import randint
from prancer.utils import fix_wrapper
from pkg_resources import resource_filename

__author__ = "Levi Borodenko"
__copyright__ = "Levi Borodenko"
__license__ = "mit"

# setting up logger instance
_logger = logging.getLogger(__name__)


class CommentFixer(object):
    """[summary]
    Turns all comments in a file into Pitbull song lyrics.

    [description]
    Iterates over all tokens, substituting the "COMMENT"
    ones with its own.

    Methods:
        fix(file) - takes file and returns the fixed "file.pranced"
    """

    def __init__(self):
        super(CommentFixer, self).__init__()
        
        # Number of lines
        self.NUM_LINES = len(self.LINES)
        # Path to lines file resource
        self.LINE_FILE = resource_filename(__name__, "resources/lines.txt")

        # Load lines which replace original comments here
        self.LINES = None
        with open(self.LINE_FILE, 'r') as f:
            self.LINES = f.readlines()

        # setting name
        self.__name__ = "CommentFixer"

    def _get_lyric(self) -> str:
        """Returns a random line from My Little Pony.
        """

        # Grab a random line from our lines
        random_index = randint(0, self.NUM_LINES - 1)

        # .rstrip to remove trailing whitespace
        return "# " + self.LINES[random_index].rstrip()

    @fix_wrapper
    def fix(self, tokens):
        """After decoration, it will take the file that you want to fix and
        create a fixed .pranced file.

        BEFORE DECORATION: takes a list of tokens and returns
        a list of the fixed tokens.

        Arguments:
            tokens -- the list of tokens from the file

        Returns:
            result - list of tokens, but now with fixed comments
        """

        result = []

        # iterating over tokens
        for token_type, token_val, _, _, _, in tokens:

            # if token is a comment, substitute with a random lyric comment.
            if token_type == COMMENT:
                result.append(
                    (COMMENT, self._get_lyric())
                )

            else:
                result.append((token_type, token_val))
        return result
