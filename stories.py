"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of placeholder words and the text of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, prompt:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, placeholders, template):
        """Create story with words and template text. ."""

        self.placeholders = placeholders
        self.template = template

    def generate(self, placeholders_and_values):
        """Substitute answers into text."""

        completed_story = self.template

        for (placeholder, value) in placeholders_and_values.items():
            completed_story = completed_story.replace("{" + placeholder + "}", value)

        return completed_story


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    "Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb} {plural_noun}."
)

story2 = Story(
    ["noun", "adjective", "second adjective", "person", "verb"],
    "There once was a {noun} that was so {adjective} and {second adjective} that {person} ended up {verb}ing it."
)

story3 = Story(
    ["adjective", "second adjective", "person"],
    "Here's a fun fact: {adjective} and {second adjective} are {person}'s favorite words."
)
