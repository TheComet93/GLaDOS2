import glados


class Hug(glados.Module):

    def get_help_list(self):
        return [
            glados.Help('hug', '[intensity]', 'The bot hugs you. Intensity is optional, goes from 1 to 10')
        ]

    @glados.Module.commands('hug')
    def hug(self, client, message, intensity):
        """Because everyone likes hugs
        Up to 10 intensity levels."""
        name = " *" + message.author.name + "*"

        if intensity == '':
            intensity = 0
        intensity = int(intensity)

        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        else:
            msg = "(づ￣ ³￣)づ" + name + " ⊂(´・ω・｀⊂)"
        yield from client.send_message(message.channel, msg)