import glados


class Blog(glados.Module):
    def setup_memory(self):
        self.memory['data path'] = os.path.join(self.data_dir, 'blog')
        if not os.path.isdir(self.memory['data path']):
            os.mkdir(self.memory['data path'])
        self.memory['data file'] = os.path.join(self.memory['data path'], 'submissions.txt')
        self.memory['count file'] = os.path.join(self.memory['data path'], 'count.txt')

    @glados.Module.command('blog', '', 'Returns a link to the chat blog')
    async def blog(self, message, channel):
        await self.client.send_message(message.channel, 'http://gdnetchat.tumblr.com/submit')

    @glados.Module.command('blogpost', '', 'Submits the current conversation to the chat blog')
    async def blogpost(self, message, channel):
        with codecs.open(self.memory['count file'], 'r', encoding='utf-8') as f:
          contents = f.read()

          if len(contents) == 0:
              count = 1
          else:
              count = int(contents) + 1

        with codecs.open(self.memory['count file'], 'w', encoding='utf-8') as f:
          f.write(count)

        with codecs.open(self.memory['data file'], 'a', encoding='utf-8') as f:
            f.write('blogpost#{}'.format(count))

        await self.client.send_message(message.channel, "Thanks for your submission! [blogpost#{}]".format(count))

    @glados.Permissions.moderator
    @glados.Module.command('blogadmin', '<command>', 'Performs admin operations on the chat blog submission queue')
    async def blogadmin(self, message, command):
        if command == 'list':
            with codecs.open(self.memory['data file'], 'r', encoding='utf-8') as f:
                submissions = f.read().splitlines()

            if len(submissions) == 0:
                await self.client.send_message(message.channel, "No blog submissions to review.")
            else:
                await self.client.send_message(message.channel, submissions.join("\n"))
        elif command == 'pop':
            with codecs.open(self.memory['data file'], 'r', encoding='utf-8') as f:
                submissions = f.read().splitlines()

            if len(submissions) == 0:
                await self.client.send_message(message.channel, "No blog submissions to review.")
            else:
                with codecs.open(self.memory['data file'], 'w', encoding='utf-8') as f:
                    f.writelines(submissions[1:])
                await self.client.send_message(message.channel, submissions[0])
        else:
            await self.client.send_message(message.channel, "Allowed commands are list, pop.")

