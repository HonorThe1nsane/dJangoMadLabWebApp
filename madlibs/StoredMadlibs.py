# allows use input from their keyboard
import sys
import inspect


class ZooMadLib:
    def blanks(self):
        return {
            "animal": "chose a type of animal",
            "verb past tense": "past tense verb",
            "Noun": "enter a noun",
            "Adjective": "enter an adjective",
            "verb": "enter a verb",
        }

    def story(self, blanks):
        story = (
            "Today I went to the zoo. I saw a "
            + blanks["animal"]
            + " jumping up and down in its tree."
        )
        story = (
            story
            + "He "
            + blanks["verb past tense"]
            + " quickly through the large tunnel that led to its huge "
            + blanks["Noun"]
            + "."
        )
        story = (
            story
            + "I got some peanuts and passed them through the cage to a gigantic gray "
            + blanks["Noun"]
            + " towering above my head."
        )
        story = story + "Feeding that Animal made me hungry. "
        story = (
            story + "I went to get a " + blanks["Adjective"] + " scoop of ice cream."
        )
        story = story + "It filled my stomach."
        story = (
            story
            + "Afterwards I had to "
            + blanks["verb"]
            + " quickly to catch our bus."
        )
        story = (
            story
            + "When I got home I "
            + blanks["verb"]
            + " to my mom for a "
            + blanks["Adjective"]
            + " day at the zoo."
        )
        return story


if __name__ == "__main__":
    # This code finds all of the Madlibs in this program.
    classes = []
    for name in dir(StoredMadlibs):
        obj = getattr(StoredMadlibs, name)
        if inspect.isclass(obj):
            classes.append(obj.__name__)

    # First, we need to get the blanks to fill in.
    # Our program uses the blanks() function to determine what blanks
    # are needed by the Madlib. We "loop" through each of the blanks
    # and add the answers to the "answers" variable.
    m = ZooMadLib()
    blanks = m.blanks()
    answers = {}
    for key in blanks:
        answers[key] = input("Fill in an answer for '{}': ".format(blanks[key]))

    # This takes the answers you typed in, sends them to the
    # story function, and then prints out the final story.
    print(m.story(answers))
