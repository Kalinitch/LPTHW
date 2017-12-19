from sys import exit
from random import randint

class Scene(object):

    def enter (self):
        print "It's just another foggy, cold, miserable day, you alarm clook goes off marking the beggning of yet another working day."
        pass

class Engine(object):

    def __init__ (self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Life_Owned(Scene):

    quips = [
        "Now when you work in Google inc. you have reached the top of the tops, now you can die in peace"
        "Now when you make more money then the rest of your family and relatives you can sip you Daikiri under the sun of Maiorca"

    ]

    def enter (self):
        print Death.quips[randint(0, len(self.quips) -1)]
        exit(1)

class Homeless(Scene):

    def enter(self):

        quips = [
            "Now that you have decided to stay in your bed fprever, your life haas gone by unnoticed. Day was followed by night, night by day until your landlord got fed up with you and now you live on the street, congrats!."
            "Wll. You surely had a good nights sleep, but no friends and work, what a way to live!"

class Out(Scene):
    def enter(self):
        print "You finally get up. Good job!"
        print "However you still feel like you could use some rest."
        print "You also notice that your hair need washing"
        print "And you're humgry"
        print "You have 20 minutes until the bus leaves"
        print "What do you do? have some rest/have a shower/have breakfast/dress up and leave the house"

        action = raw_input("> )

        if action == "have some rest":
            return 'homeless'

        if action == "have a shower":
            print "You get out of you room and approcah the bathroom"
            print "You hear the sounds of water splashing"
            print "Seems like your flatmate has occupied the bathroom"
            print "What do you do? give up and go to have some breakfast/ knock on the door/ leave the house like this"

            action = raw_input("> ")

            if action == "give up and go to have some breakfast":
                return 'breakfast'

            if action == "knock on the door":
                print "You timidly knock on the door and ask your flatmate how long their are going to stay in the shower"
                print "You hear the water stop flowing"
                print "Several moments pass"
                print "There is no answer, only the sound of splashing footsteps apptoaching the door"
                print "You feel something uncanny going on"
                print "You see the red ominous shinning comming through the doorframe"
                print "Your body is petrified, you can't run there is no way back"
                print "The door opens and you can feel the death approaching"
                print "Is it a dream or reality?"

                return 'morning'

            if action == "leave the house like this":
                print "You decide to leave the house with greezy head and no breakfast"
                print "You manage to catch the bus, good job!"
                print "You get in the classroom and take a seet as usual"



class Morning(Scene):

    def enter(self):
        print "Good morning sleepy head! It's 7 am, dark, cold morning outside"
        print "Your alarm clook goes off as usuall, what do you do? snooze/get up/ignore"

        action = raw_input("> ")

        if action == "snooze":
            print "You put your alarm on snooze and let yourself relax for a while"
            print "You do enjoy yourself lying in a warm, cosy bed"
            print "However, life is cruel and merciless, the alarm gors off again after 10 minutes"
            print "What do you do? snooze/get up/ignore"

            action = raw_input("> ")

            if action == "snooze":
                return 'homeless'

            elif action == "ignore":
                return 'homeless'

            elif == "get up":
                return 'out'

        elif action == "ignore":
            return 'homeless'

        elif action == "get up":
            return 'out'

        else:
            print "Better think again!"
            return 'morning'

class Finished(self):

    def enter(self):
        print "You have achived a total harmony with yourself. Good job!"
        return 'finished'

class Map(object):
    scenes = {
    'life_owned': Life_Owned(),
    'homeless': Homeless(),
    'Out': Out(),
    'Morning': Morning(),
    }

    def __init__ (self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('morning')
a_game = Engine(a_map)
a_game.play()
