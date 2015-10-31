import MySQLdb as mdb

con = mdb.connect('localhost', 'austin', 'chicken4wing', 'prdb')

with con:
    name = '-'
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute("SELECT * FROM Anthropometry WHERE Name = %s", name)

    rows = cur.fetchone()
    squat = rows["Femur"]
    deadlift = int(rows["Acromion_Height"]) - int(rows["Humerus"])\
               - int(rows["Forearm"]) - int(rows["Ankle_to_Ground"]) - (int(rows["Tibia"])/2) - (17.7/2)
    bench = int(rows["Forearm"]) + int(rows["Humerus"]) / 2
    press = int(rows["Humerus"]) + int(rows["Forearm"])
    snatch = int(rows["Overhead_Height"]) - (17.7 / 2)
    clean_and_jerk = int(rows["Overhead_Height"]) - (17.7 / 2)
    print rows
    print squat
    print deadlift
    print bench
    print press
    print snatch
    print clean_and_jerk


    # for row in rows:
    #     print row["Id"], row["Name"]






# movement = {'squat': 100, 'bench': 50, 'deadlift': 200}
# dist = {'squat': 1.5, 'bench': 1, 'deadlift': 3}
# rep = {'squat': 10, 'bench': 5, 'deadlift': 1}
# wo_total = []
#
# if 'squat' in movement:
#     foot_pounds = (dist['squat'] * movement['squat']) * rep['squat']
#     wo_total.append(foot_pounds)
#     print foot_pounds
#     print wo_total
#
# if 'bench' in movement:
#     foot_pounds = (dist['bench'] * movement['bench']) * rep['bench']
#     wo_total.append(foot_pounds)
#     print foot_pounds
#     print wo_total
#
# if 'deadlift' in movement:
#     foot_pounds = (dist['deadlift'] * movement['deadlift']) * rep['deadlift']
#     wo_total.append(foot_pounds)
#     print foot_pounds
#     print wo_total
#
# print sum(wo_total)

# if 'squat' in movement:
#     movement['squat'] += 100
#     print movement['squat']
#
# movement_sum = sum(movement.itervalues())
# print movement_sum