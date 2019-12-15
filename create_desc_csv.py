

descriptions = ["money_spent_he",    # freq 1
         "num_top_unis",    # freq 2
         "gender_pay_gap",    # freq 3
         "women_study_department",   # freq 4
         "women_work_sector",    # freq 5
         "obesity", # freq 6
         "young_evenings", # freq 7
         "student_choice_study", # freq 8
         "median_salary_se", # freq 9
         "median_salary_women", # freq 10
         ]



event_dict = {}


with open("data1/" + "event_desc.csv", 'w' ) as f:
        
    for file in descriptions:
                
        with open("data1/" + file, 'r') as f1:
            lines = f1.readlines()
        
            for line in lines:
                words = line.split("    ")
                if (len(words) == 1): # No label found
                    continue
                else: # there's a label
                    if words[1] in event_dict: # label already in event_desc.csv
                        continue
                    else: # add label to the dictionary
                        event_dict[words[1]] = words[0]
        f1.close()
    for key, value in event_dict.items():
        f.write(str(key))
        f.write(value + '\n')
    f.close()