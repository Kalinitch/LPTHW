class Song(object):

     def __init__(self, lyrics):
         self.lyrics = lyrics

     def sing_me_a_song(self):
            for line in self.lyrics:
              print line

happy_bday = Song(["Happy birthday to you",
                   "I dont' want to get suied",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()