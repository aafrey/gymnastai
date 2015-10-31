import sqlite3 as lite
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


class Anthropometry(BoxLayout):

    con = lite.connect('gymnastai.db')
    body_part_container = ObjectProperty()
    anthro_values = ObjectProperty()
    anthro_metrics_input = ObjectProperty()

    with con:
        cur = con.cursor()

    def add_body_part_label(self):
        cur = Anthropometry.con.cursor()
        cur.execute("SELECT * FROM UserInfo")
        description = cur.description
        self.ids._body_part_container.clear_widgets()

        for desc in description[8:22]:
            spacer = SpacerLabel()
            self.ids._body_part_container.add_widget(spacer)
            bodypart_label = AnthroLabel(text='    '+str(desc[0].replace('_', ' ')))
            self.ids._body_part_container.add_widget(bodypart_label)

    def update_anthro_metrics(self):
        con = lite.connect('gymnastai.db')
        self.ids._body_part_metrics_container.clear_widgets()
        anthro_values = self.anthro_values.text
        anthro_metrics_input = self.anthro_metrics_input.text
        tb_columns = ['Height', 'Weight', 'Head and Neck', 'Torso', 'Pelvis', 'Femur', 'Tibia', 'Ankle to Ground',
                      'Foot', 'Humerus', 'Forearm', 'Hand', 'Acromion Height', 'Overhead Height']

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM UserInfo")

            if anthro_values in tb_columns:
                cur.execute("UPDATE UserInfo SET %s = %s WHERE Id = %s"
                            % (anthro_values.replace(' ', '_'), anthro_metrics_input, '1'))

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM UserInfo")

            row = cur.fetchone()
            while row is not None:
                for i in row[8:22]:
                    spacer = SpacerLabel()
                    self.ids._body_part_metrics_container.add_widget(spacer)
                    body_part_matrics_label = AnthroLabel(text=str(i))
                    self.ids._body_part_metrics_container.add_widget(body_part_matrics_label)

                    row = cur.fetchone()


class AnthroLabel(Label):
    pass


class SpacerLabel(Label):
    pass

