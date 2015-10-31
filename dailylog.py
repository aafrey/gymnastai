import sqlite3 as lite
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.label import Label


class DailyLog(BoxLayout):
    con = lite.connect('gymnastai.db')
    con.row_factory = lite.Row
    set_date_text = ObjectProperty()
    num_reps_text = ObjectProperty()
    set_weight_text = ObjectProperty()
    add_set_button = ObjectProperty()
    movement_info = ObjectProperty()
    time_input = ObjectProperty()
    session_loads = []
    session_volume = []
    weight_dict = {'Squat': 0, 'Deadlift': 0, 'Bench': 0, 'Press': 0,
                     'Snatch': 0, 'Clean_and_Jerk': 0}
    rep_dict = {'Squat': 0, 'Deadlift': 0, 'Bench': 0, 'Press': 0,
                     'Snatch': 0, 'Clean_and_Jerk': 0}
    dist_dict = {}
    ft_lbs_list = []

    with con:
        name = '-'
        cur = con.cursor()
        cur.execute("SELECT * FROM UserInfo WHERE Name = ?", name)

        rows = cur.fetchone()
        dist_dict['Squat'] = int(rows["Femur"])
        dist_dict['Deadlift'] = int(rows["Acromion_Height"]) - int(rows["Humerus"]) \
                   - int(rows["Forearm"]) - int(rows["Ankle_to_Ground"]) - (int(rows["Tibia"])/2) - (17.7/2)
        dist_dict['Bench'] = int(rows["Forearm"]) + int(rows["Humerus"]) / 2
        dist_dict['Press'] = int(rows["Humerus"]) + int(rows["Forearm"])
        dist_dict['Snatch'] = int(rows["Overhead_Height"]) - (17.7 / 2)
        dist_dict['Clean_and_Jerk'] = int(rows["Overhead_Height"]) - (17.7 / 2)
        print dist_dict

    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Watts")
        cur.execute("CREATE TABLE Watts(ID INTEGER PRIMARY KEY AUTOINCREMENT, Date VARCHAR(25),"
                    "WO_Time VARCHAR(25), WO_Watts VARCHAR(25))")

    def add_set(self):
        reps = self.num_reps_text.text
        weight = self.set_weight_text.text
        movement = self.movement_info.text

        DailyLog.rep_dict[movement] = reps
        DailyLog.weight_dict[movement] = weight
        in_lbs = float(DailyLog.dist_dict[movement]) * (int(weight) * int(reps))
        ft_lbs = in_lbs * 0.083333333
        DailyLog.ft_lbs_list.append(ft_lbs)
        set_load = int(reps) * int(weight)
        DailyLog.session_loads.append(set_load)

    def add_set_label(self):
        reps = self.num_reps_text.text
        weight = self.set_weight_text.text
        movement = self.movement_info.text

        spacer = SpacerLabel()
        self.ids._workout_container.add_widget(spacer)
        set_label = SetLabel(text=movement+'    '+reps+'x'+weight)
        self.ids._workout_container.add_widget(set_label)

        self.ids._metrics_container.clear_widgets()
        spacer = SpacerLabel()
        self.ids._metrics_container.add_widget(spacer)
        set_load_label = SetLabel(text='Session Load: '+str(sum(DailyLog.session_loads)))
        self.ids._metrics_container.add_widget(set_load_label)
        spacer2 = SpacerLabel()
        self.ids._metrics_container.add_widget(spacer2)
        DailyLog.session_volume.append(int(reps))
        session_volume_label = SetLabel(text='Session volume: '+str(sum(DailyLog.session_volume)))
        self.ids._metrics_container.add_widget(session_volume_label)

    def calculate_power(self):
        con = lite.connect('gymnastai.db')
        self.ids._power_stats.clear_widgets()
        date = self.set_date_text.text
        time = self.time_input.text
        foot_pounds_sec = sum(DailyLog.ft_lbs_list) / float(time)
        wo_watts = int(foot_pounds_sec / .738)

        ft_lbs_sec_label = PowerLabel(text=str(int(foot_pounds_sec))+' ft lbs/sec')
        watt_label = PowerLabel(text=str(int(wo_watts)) + ' watts')
        spacer = SpacerLabel()
        spacer2 = SpacerLabel()
        self.ids._power_stats.add_widget(spacer)
        self.ids._power_stats.add_widget(ft_lbs_sec_label)
        self.ids._power_stats.add_widget(spacer2)
        self.ids._power_stats.add_widget(watt_label)

        minutes = int(int(time) / 60)
        seconds = int(time) % 60
        if int(time) % 60 < 10:
            wo_time = str(minutes) + ':0' + str(seconds)
        else:
            wo_time = str(minutes) + ':' + str(seconds)
        print wo_time

        with con:
            cur = con.cursor()

            cur.execute("INSERT INTO Watts(Date) VALUES(?)", (date,))
            cur.execute("UPDATE Watts SET WO_Watts = ? WHERE Date=?", (wo_watts, date))
            cur.execute("UPDATE Watts SET WO_Time = ? WHERE Date = ?", (wo_time, date))


class SetLabel(Label):
    pass


class SpacerLabel(Label):
    pass


class PowerLabel(Label):
    pass


