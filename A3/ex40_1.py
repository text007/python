# 练习类


class Song(object):

    def __init__(self, lyrics):
        print("A+", lyrics)
        self.lyrics = lyrics
        print("B+", self.lyrics)

    def sing_me_a_song(self):
        for line in self.lyrics:
            print("C+", line)


happy_bday = Song(["123", "456", "789"])

bulls_on_parade = Song(["369", "258"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
