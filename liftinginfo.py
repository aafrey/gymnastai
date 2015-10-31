import sqlite3 as lite
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class LiftingInfo(BoxLayout):
    con = lite.connect('gymnastai.db')
    movement_name = ObjectProperty()
    new_pr = ObjectProperty()
    pr_columns = ['Squat', 'Deadlift', 'Bench', 'Press', 'Snatch', 'Clean and Jerk']

    def add_pr(self):
        con = lite.connect('gymnastai.db')
        movement_name = self.movement_name.text
        new_pr = self.new_pr.text

        with con:
            cur = con.cursor()
            pr_columns = LiftingInfo.pr_columns
            if movement_name == 'Choose Lift' or new_pr == '' \
                    or new_pr == 'Add PR':
                print('Try Again')
            elif movement_name in pr_columns:
                cur.execute("UPDATE UserInfo SET "+movement_name.replace(' ', '_')+"=? WHERE ID=?", (new_pr, '1'))

    def add_movement_label(self):
        cur = LiftingInfo.con.cursor()
        cur.execute("SELECT * FROM UserInfo")
        description = cur.description
        self.ids._movement_label_container.clear_widgets()

        for desc in description[2:8]:
            movement_label = PrLabel(text='    '+str(desc[0].replace('_', ' ')))
            self.ids._movement_label_container.add_widget(movement_label)

    def update_pr(self):
        con = lite.connect('gymnastai.db')
        self.ids._pr_label_container.clear_widgets()

        with con:
            cur = con.cursor()
            cur.execute("SELECT * FROM UserInfo")

            row = cur.fetchone()
            while row is not None:
                for i in row[2:8]:
                    pr_label = PrLabel(text=str(i))
                    self.ids._pr_label_container.add_widget(pr_label)
                    row = cur.fetchone()


class PrLabel(Label):
    pass