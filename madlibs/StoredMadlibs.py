# allows use input from their keyboard
# StoreMadlibs.py file
import inspect


class ZooMadLib:
    def blanks(self):
        return {
            "animal": "choose a type of animal",
            "verb past tense": "past tense verb",
            "Noun": "enter a noun",
            "Adjective": "enter an adjective",
            "verb": "enter a verb",
        }

    def story(self, answers):
        story = (
            "Today I went to the zoo. I saw a "
            + answers["animal"]
            + " jumping up and down in its tree."
        )
        story += (
            "He "
            + answers["verb past tense"]
            + " quickly through the large tunnel that led to its huge "
            + answers["Noun"]
            + "."
        )
        story += (
            "I got some peanuts and passed them through the cage to a gigantic gray "
            + answers["Noun"]
            + " towering above my head."
        )
        story += "Feeding that Animal made me hungry. "
        story += (
            "I went to get a " + answers["Adjective"] + " scoop of ice cream."
        )
        story += "It filled my stomach."
        story += (
            "Afterwards I had to "
            + answers["verb"]
            + " quickly to catch our bus."
        )
        story += (
            "When I got home I "
            + answers["verb"]
            + " to my mom for a "
            + answers["Adjective"]
            + " day at the zoo."
        )
        return story


# if __name__ == "__main__":
#     # First, we need to get the blanks to fill in.
#     # Our program uses the blanks() function to determine what blanks
#     # are needed by the Madlib. We "loop" through each of the blanks
#     # and add the answers to the "answers" variable.
#     m = ZooMadLib()
#     blanks = m.blanks()
#     answers = {}
#     for key in blanks:
#         answers[key] = input("Fill in an answer for '{}': ".format(blanks[key]))

#     # This takes the answers you typed in, sends them to the
#     # story function, and then prints out the final story.
#     print(m.story(answers))
