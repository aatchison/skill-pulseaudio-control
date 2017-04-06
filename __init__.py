# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

from pulsectl import Pulse

__author__ = 'aatchison'

LOGGER = getLogger(__name__)

pulse = Pulse('mycroft-pulse-client')


class PulseAudioControlSkill(MycroftSkill):
    def __init__(self):
        super(PulseAudioControlSkill, self).__init__(name="PulseAudioControlSkill")

    def initialize(self):
        list_source_intent = IntentBuilder("SourceList").\
            require("SourceList").build()
        self.register_intent(list_source_intent, self.handle_list_source_intent)

        list_sink_intent = IntentBuilder("SinkList").\
            require("SinkList").build()
        self.register_intent(list_sink_intent, self.handle_list_sink_intent)

        intent = IntentBuilder("SourceSetIntent").require(
            "SourceSet").require("Device").build()
        self.register_intent(intent, self.handle_set_source_intent)

        intent = IntentBuilder("SinkSetIntent").require(
            "SinkSet").require("Device").build()
        self.register_intent(intent, self.handle_set_sink_intent)

    def handle_list_source_intent(self, message):
        self.speak_dialog("Source.List")
        for source in pulse.source_list():
            say = str(source.proplist['device.description']) + " is device number " + str(source.proplist['alsa.card'])
            self.speak(say)

    def handle_list_sink_intent(self, message):
        self.speak_dialog("Sink.List")
        for sink in pulse.sink_list():
            say = str(sink.proplist['device.description']) + " is device number " + str(sink.proplist['alsa.card'])
            self.speak(say)

    def handle_set_source_intent(self, message):
        self.speak("Setting default source to " + message.data.get("Device"))

    def handle_set_sink_intent(self, message):
        self.speak("Setting default sink to " + message.data.get("Device"))

    def stop(self):
        pass


def create_skill():
    return PulseAudioControlSkill()