class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self,paths):
        self.paths.update(paths)

# Create the scenes of the game
#Instructions
welcome = Scene("Welcome", "welcome",
"""
Welcome to the 'Big decisions game!
In this game you are going to make...same big decisions.
The outcome of the game depends on your choice.
Foe each scene you are given a choice in brackets.
To proceed from one scene to another please type in your choice below.
Redy to begin? (type 'yes' to proceed)
""")

# Scene 1 - Beginning
morning = Scene("Morning", "morning",
"""
It's just another foggy, cold, miserable morning, you alarm clook goes off marking the beggning of yet another working day.
'Hell, I should have never stayed up untill 4:00 to watch the rest of the episodes of 'Hell's Kitchen' in one night'
That's a rough morning, your eyes and throat are dry, your hean is all dizzy.
Whatever... The alarm hits you hard with an insanely unnerving sound of clavecin.
It's time to make some big decisions! (Put on snooze/get up/ignore)
""")
# Scene 2 - Getting Up
getting_up = Scene("Getting up", "getting_up",
"""
You finally get up. Good job!
However you still feel like you could use some rest.
You also notice that your hair need washing
And you're humgry
You have 20 minutes until the bus leaves
What do you do? (have some rest/have a shower/have breakfast/leave the house)
""")
# Scene 2, Branch 2 - have a shower
have_a_shower = Scene("Have a shower", "have_a_shower",
"""
You get out of you room and approcah the bathroom
You hear the sounds of water splashing
Seems like your flatmate has occupied the bathroom
What do you do? have breakfast/ knock on the door/ leave the house like this
""")
# Scene 2, Branch 1, Subbranch - 1
have_breakfast = Scene("breakfast", "have_breakfast",
"""
You decide to go to the class with greezy hair but you decide that you at least to need to feed yourself.
You have a toast with a piece of bread and a cup of coffee.
You manage to catch the bus.
You enter the classroom, you feel like you look a bit clumsy, but since you had breakfast you have a shinning smile.
Everyone seem to admire you, you look fabulous, don't you agree? (yes/no)
""")
#Scene 2, Branch 1, Subbranch - 2
knock_on_the_door = Scene("knocking on the door", "knock_on_the_door",
"""
You timidly knock on the door and ask your flatmate how long their are going to stay in the shower
You hear the water stop flowing
Several moments pass
There is no answer, only the sound of splashing footsteps apptoaching the door
You feel something uncanny going on
You see the red ominous shinning comming through the doorframe
Your body is petrified, you can't run there is no way back
The door opens and you can feel the death approaching
Is it a dream or reality?
""")
#--------------------------------------------------------------------------------
#Endings
the_end_failure = Scene("Failure!", "the_end_failure",
"""
You decide to leave the house with greezy head and no breakfast
You manage to catch the bus, good job!
You get in the classroom and take a seat as usual
After some time you start noticing unfiendly scornful glances, no wonder since you haven't washed your hair
It even gets worse because you left the house hungry
Your belly makes embarssing noises
Can this day become even worse?
You get kicked in out of the class for being not fabulous enough.
""")

the_end_winner = Scene("Success!", "the_end_winner",
"""
Through hard work, asketism, and self-denial, you have managed to make it to the top of the tops - you got a position at Google inc
and when you make more money than the rest of your family and relatives you can sip your daikiri under the sun of Maiorca.
Eneryone is green with envy - you can die in peace!
""")

the_end_loser = Scene("Oops", "the_end_loser",
"""
Now that you have decided to stay in your bed forever, your life haas gone by unnoticed.
You surely had a good nights sleep, but no friends and work, what a way to live!
Day was followed by night, night by day until your landlord got fed up with you and now you live on the street, congrats!
Your life has went downhill ever since, you never manage to be as successful as your groupmates.
""")


#Paths
welcome.add_paths({
    'yes':morning
})

morning.add_paths({
    'put on snooze':the_end_loser,
    'get up':getting_up,
    'ignore': the_end_loser
})

getting_up.add_paths({
    'have some rest': the_end_loser,
    'have a shower': have_a_shower,
    'have breakfast': have_breakfast
})

have_a_shower.add_paths({
    'have breakfast': have_breakfast,
    'knock on the door': morning,
    'leave the house': the_end_failure
})

have_breakfast.add_paths({
    'yes': the_end_winner,
    'no': the_end_loser
})

# Scenes
SCENES = {
    welcome.urlname : welcome,
    morning.urlname : morning,
    getting_up.urlname : getting_up,
    have_a_shower.urlname : have_a_shower,
    have_breakfast.urlname : have_breakfast,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    the_end_failure.urlname : the_end_failure
}

START = welcome
