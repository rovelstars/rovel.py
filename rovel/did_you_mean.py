def _levenshtein(s1, s2):
    if len(s1) < len(s2):
        return _levenshtein(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)

    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            
            current_row.append(min(insertions, deletions, substitutions))

        previous_row = current_row
    
    return previous_row[-1]

class Matcher:
    def __init__(self, options=None):
        if options == None:
            options = {}

        if isinstance(options, str) or isinstance(options, list):
            options = {"values": options}

        self.values = []
        self.threshold = options.get("threshold", 2)

        if isinstance(options["values"], list):
            self.values = options["values"]
        elif isinstance(options["values"], str):
            self.values = options["values"].split(" ")

        self.case_sensitive = options.get("case_sensitive", False)

    def add(self, *args):
        self.values.extend(args)
        return self

    def ignore_case(self):
        self.case_sensitive = False
        return self

    def match_case(self):
        self.case_sensitive = True
        return self

    def set_threshold(self, number):
        self.threshold = number
        return self

    def distance(self, word1, word2):
        return _levenshtein(word1, word2)

    def list(self, q):
        q = q.strip()

        if not self.case_sensitive:
            q = q.lower()

        matches = []
        for word in self.values:
            distance = self.distance(q, word if self.case_sensitive else word.lower())

            if distance <= self.threshold:
                matches.append({
                    "value": word,
                    "distance": distance
                })

        matches.sort(key=lambda v: v["distance"])
        return matches

    def get(self, q):
        try:
            return self.list(q)[0]["value"]
        except IndexError:
            pass