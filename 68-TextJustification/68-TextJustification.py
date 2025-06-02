# Last updated: 6/2/2025, 7:01:39 AM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # len of line gives min. number of spaces required to represent
        result = []
        line = []
        width = 0

        for w in words:
            if width + len(line) + len(w) > maxWidth:
                for i in range(maxWidth-width):
                    line[i%(len(line)-1 or 1)] += ' '
                result.append(''.join(line))
                line = []
                width = 0

            line += [w]
            width += len(w)
        return result + [' '.join(line).ljust(maxWidth)]
        