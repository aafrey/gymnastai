import MySQLdb as mdb


con = mdb.connect('localhost', 'austin', 'chicken4wing', 'prdb')

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS UserInfo")
    cur.execute("CREATE TABLE UserInfo(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25),  "
                "Squat VARCHAR(25), Deadlift VARCHAR(25), Bench VARCHAR(25), Press VARCHAR(25), "
                "Snatch VARCHAR(25), Clean_and_Jerk VARCHAR(25), Height VARCHAR(25),"
                "Weight VARCHAR(25), Head_and_Neck VARCHAR(25), Torso VARCHAR(25), Pelvis VARCHAR(25), "
                "Femur VARCHAR(25), Tibia VARCHAR(25), Ankle_to_Ground VARCHAR(25), Foot VARCHAR(25), "
                "Humerus VARCHAR(25), Forearm VARCHAR(25), Hand VARCHAR(25), Acromion_Height VARCHAR(25),"
                " Overhead_Height VARCHAR(25))")

    cur.execute("INSERT INTO UserInfo(Name, Squat, Deadlift, Bench, Press, Snatch, Clean_and_Jerk, "
                "Height, Weight, Head_and_Neck, Torso, Pelvis, Femur, Tibia, "
                "Ankle_to_Ground, Foot, Humerus, Forearm, Hand, Acromion_Height, Overhead_Height)"
                " VALUES('-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')")