

descriptions = ["money_spent_he.txt",    # freq 1
         "num_top_unis.txt",    # freq 2
         "gender_pay_gap.txt",    # freq 3
         "women_study_department.txt",   # freq 4
         "women_work_sector.txt",    # freq 5
         "obesity.txt", # freq 6
         "young_evenings.txt", # freq 7
         "student_choice_study.txt", # freq 8
         "median_salary_se.txt", # freq 9
         "median_salary_women.txt", # freq 10
         ]

labels_dict = [
		"<y_axis_least_value_val>\n",
		"<y_axis_Scnd_highest_val>\n",
		"<y_axis_highest_value_val>\n",
		"<y_axis_3rd_highest_val>\n",
        "<y_axis_4th_highest_val>\n",
        "<x_axis_label_highest_value>\n",
        "<x_axis_label_least_value>\n",
        "<x_axis_label_Scnd_highest_value>\n",
        "<x_axis_label_3rd_highest_value>\n",
        "<x_axis_label_4th_highest_value>\n"    
        #""" "<y_axis_inferred_value_approx>\n",
        #"<y_axis_inferred_value>\n" """
    ]

for file in descriptions:
    counter = 1
    with open(file) as f:
        with open("delexicalized/delexicalized_" + file, "w") as f1:
        #while True :
            lines = f.readlines()
        #f1.write("NUMBER")
            for line in lines:
                if line == '\n':
                    continue
                if line.find('\"') != -1 and counter == 1:
                    line = "''\n"
                    counter += 1
                if '\"' in line and counter > 1:
                    line = "<end_of_desciption>\n"    
                if "    " in line:
                    words = line.split("    ")
                    label_found = False
                    for word in labels_dict:
                        if words[1] == word:
                            label_found = True
                    if label_found:
                    #f1.write("NUMBER")
                        if words[1] == '<y_axis_highest_value_val>\n':
                            words[0] = "NUMBER_HIGHEST"
                        if words[1] == '<y_axis_least_value_val>\n':
                            words[0] = "NUMBER_LEAST"
                        if words[1] == '<y_axis_Scnd_highest_val>\n':
                            words[0] = "NUMBER_SCND"
                        if words[1] == '<y_axis_3rd_highest_val>\n':
                            words[0] = "NUMBER_3RD"
                        if words[1] == '<x_axis_label_4th_highest_value>\n':
                            words[0] = "NUMBER_4TH"
                        if words[1] =='<x_axis_label_highest_value>\n':
                            words[0] = "X_AXIS_HIGHEST"
                        if words[1] =='<x_axis_label_least_value>\n':
                            words[0] = "X_AXIS_LEAST"
                        if words[1] =='<x_axis_label_Scnd_highest_value>\n':
                            words[0] = "X_AXIS_SCND"
                        if words[1] =='<x_axis_label_3rd_highest_value>\n':
                            words[0] = "X_AXIS_3RD"
                        if words[1] =='<x_axis_label_4th_highest_value>\n':
                            words[0] = "X_AXIS_4TH"
                        line_to_print = words[0] + '    ' + words[1]
                        f1.write(line_to_print)
                       # f1.write("\n")
                    else:
                            
                        line_to_print = words[0] + '    ' + words[1]
                        f1.write(line_to_print)
                #elif len(words) == 1:
                #        f1.write(words[0])
                else:
                #f1.write("NUMBER")
                    f1.write(line)
                #f1.write("\n") 
            f.close()
            f1.close()