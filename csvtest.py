import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

names = []
actual_name_count = 0
with open('names_collection.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        names.append(row[0])


with open('series_standings_NASCAR_iRacing_Series_-_Open_2019_Season1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    irating_list = []
    club_list = []
    starts_dict = {}
    poles_dict = {}
    avg_incident_dict = {}
    avg_lap_incident_dict = {}
    avg_finish_dict = {}
    wins_dict = {}
    top5_dict = {}
    champ_point_dict = {}
    laps_led_dict = {}
    win_percent_dict = {}
    top5_percent_dict = {}

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[1] in names:
                actual_name_count += 1
                irating_list.append(int(row[6]))
                club_list.append(row[4])
                poles_dict[row[1]] = int(row[16])
                starts_dict[row[1]] = int(row[9])
                champ_point_dict[row[1]] = int(row[2])
                avg_finish_dict[row[1]] = int(row[7])
                top5_dict[row[1]] = int(row[8])
                laps_led_dict[row[1]] = int(row[10])
                wins_dict[row[1]] = int(row[11])
                win_percent_dict[row[1]] = round(int(row[11]) / int(row[9])*100, 2)
                top5_percent_dict[row[1]] = round(int(row[8]) / int(row[9])*100, 2)
                if int(row[9]) == 0:
                    avg_incident_dict[row[1]] = 0
                    avg_lap_incident_dict[row[1]] = 0

                else:
                    avg_incident_dict[row[1]] = round(int(row[12]) / int(row[9]), 2)
                    avg_lap_incident_dict[row[1]] = round(int(row[12]) / int(row[15]), 2)

            line_count += 1
    print(f'Processed {line_count} lines.\n')

    avg_incident_dict_sorted = sorted(avg_incident_dict, key=avg_incident_dict.get, reverse=False)
    avg_lap_incident_dict_sorted = sorted(avg_lap_incident_dict, key=avg_lap_incident_dict.get, reverse=False)
    avg_finish_dict_sorted = sorted(avg_finish_dict, key=avg_finish_dict.get, reverse=False)
    wins_dict_sorted = sorted(wins_dict, key=wins_dict.get, reverse=True)
    wins_percent_dict_sorted = sorted(win_percent_dict, key=win_percent_dict.get, reverse=True)
    top5_percent_dict_sorted = sorted(top5_percent_dict, key=top5_percent_dict.get, reverse=True)
    top5_dict_sorted = sorted(top5_dict, key=top5_dict.get, reverse=True)
    champ_point_dict_sorted = sorted(champ_point_dict, key=champ_point_dict.get, reverse=True)
    laps_led_dict_sorted = sorted(laps_led_dict, key=laps_led_dict.get, reverse=True)
    starts_dict_sorted = sorted(starts_dict, key=starts_dict.get, reverse=True)
    poles_dict_sorted = sorted(poles_dict, key=poles_dict.get, reverse=True)

    dict_list_sorted = [avg_incident_dict_sorted, avg_finish_dict_sorted, wins_dict_sorted, top5_dict_sorted,
                        champ_point_dict_sorted, laps_led_dict_sorted, avg_lap_incident_dict_sorted,
                        wins_percent_dict_sorted, top5_percent_dict_sorted, starts_dict_sorted, poles_dict_sorted]

    dict_list = [avg_incident_dict, avg_finish_dict, wins_dict, top5_dict,
                 champ_point_dict, laps_led_dict, avg_lap_incident_dict, win_percent_dict,
                 top5_percent_dict, starts_dict, poles_dict]

    dict_list_desc = ["Avg Inc/Race", "Avg Finish", "Top 5 Wins", "Top 5 Finishes",
                      "Championship Points", "Laps Led", "Avg Inc/Lap", "Win Percentage", "Top 5 Percentage",
                      "Starts", "Poles"]

    dict_list_desc_unit = ["Incidents/Race", "Average Finish", "Wins", "Top 5 Finishes", "Points", "Laps",
                           "Incidents/Lap", "Win Percentage", "Top 5 Percentage", "Starts", "Poles"]

    for i in range(0, dict_list.__len__()):
        data = []
        label = []
        print(dict_list_desc[i], "\n")
        for j in range(0, actual_name_count):
            data.append(dict_list[i][dict_list_sorted[i][j]])
            label.append(dict_list_sorted[i][j])
            print(dict_list_sorted[i][j], dict_list[i][dict_list_sorted[i][j]], dict_list_desc_unit[i])
        print("\n")
        df = pd.DataFrame(list(zip(label, data)), columns=['Driver', dict_list_desc_unit[i]])
        test_fig = px.bar(df, x="Driver", y=dict_list_desc_unit[i], color=dict_list_desc_unit[i], color_continuous_scale="Jet")
        test_fig.update_layout(title_text="BFM 2019 NiS Open - "+dict_list_desc[i])
        test_fig.show()
        # fig = go.Figure(
        #     go.Bar(y=data, x=label, textposition="inside"),
        #     layout_title_text = dict_list_desc[i]
        # )
        # fig.show()