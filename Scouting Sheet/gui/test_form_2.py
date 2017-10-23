import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton

class MatchScoutForm(BaseWidget):

    def __init__(self):
        super(MatchScoutForm,self).__init__('Match Scouting Form')

        #Definition of the forms fields
        self._firstname     = ControlText('Team Number')
        self._middlename    = ControlText('Match Number')
        self._lastname      = ControlText('Alliance Code')
        self._button        = ControlButton('Save Form')


#Execute the application
if __name__ == "__main__":   pyforms.startApp(MatchScoutForm)