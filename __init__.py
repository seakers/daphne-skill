# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent        import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log    import LOG
import websocket


# Personal Imports
import os




# Useful functions
# get_response() --> Asks the user a question and get's a response












# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.

# TODO: Change "Template" to a unique name for your skill
class DaphneSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(DaphneSkill, self).__init__(name="DaphneSkill")



        # ----- Initialize working variables used within the skill -----

        # --> Connection Variables



    def initialize(self):
        dir_path      = os.path.dirname(os.path.realpath(__file__)) # /opt/mycroft/skills/daphne-skill


        # ----- Incoming Message Events -----
        self.add_event('skill.daphneskill.in.teacher',     self.handle_incoming_teacher_intent)   # -Teacher
        self.add_event('skill.daphneskill.in.historian',   self.handle_incoming_historian_intent) # -Historian
        self.add_event('skill.daphneskill.in.critic',      self.handle_incoming_critic_intent)    # -Critic
        self.add_event('skill.daphneskill.in.analyst',     self.handle_incoming_analyst_intent)   # -Analyst
        self.add_event('skill.daphneskill.in.datamining',  self.handle_incoming_datamining_intent)# -Datamining



        self.speak("Loaded")







    ###### Incoming Message Functions #####

    # Teacher
    def handle_incoming_teacher_intent(self, message):
        return 0

    # Historian
    def handle_incoming_historian_intent(self, message):
        return 0

    # Critic
    def handle_incoming_critic_intent(self, message):
        return 0

    # Analyst
    def handle_incoming_analyst_intent(self, message):
        return 0

    # Datamining
    def handle_incoming_datamining_intent(self, message):
        return 0





    ##### Outgoing Message Functions - User Intents #####

    # Teacher
    @intent_handler(IntentBuilder("OutgoingTeacherIntent").require("Connect"))
    def handle_outgoing_teacher_intent(self, message):
        return 0


    # Historian
    @intent_handler(IntentBuilder("OutgoingHistorianIntent").require("Connect"))
    def handle_outgoing_historian_intent(self, message):
        return 0


    # Critic
    @intent_handler(IntentBuilder("OutgoingCriticIntent").require("Connect"))
    def handle_outgoing_critic_intent(self, message):
        return 0


    # Analyst
    @intent_handler(IntentBuilder("OutgoingAnalystIntent").require("Connect"))
    def handle_outgoing_analyst_intent(self, message):
        return 0


    # Datamining
    @intent_handler(IntentBuilder("OutgoingDataminingIntent").require("Connect"))
    def handle_outgoing_datamining_intent(self, message):
        return 0












    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False



    

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return DaphneSkill()
