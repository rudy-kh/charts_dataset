

descriptions = ["Money_spent_on_higher_education.txt",    # freq 1
         "Number_of_top_Unis.txt",    # freq 2
         "gender_pay_gap.txt",    # freq 3
         "women_representation_in_different_departments.txt",   # freq 4
         "women_representation_in_different_sectors.txt",    # freq 5
         "what_causes_obesity.txt", # freq 6
         "how_do_young_people_spend_their_evenings.txt", # freq 7
         "what_do_students_choose_to_study.txt", # freq 8
         "median_salary_per_year_for_se_with_respect_to_their_degrees.txt", # freq 9
         "example_Median_salary_of_women.txt", # freq 10
         ]

labels_dict = [
		"<y_axis_least_value_val>\n",
		"<y_axis_Scnd_highest_val>\n",
		"<y_axis_highest_value_val>\n",
		"<x_axis_label_3rd_highest_value>\n"
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
                            words[0] = "NUMBER_highest"
                        if words[1] == '<y_axis_least_value_val>\n':
                            words[0] = "NUMBER_least"
                        if words[1] == '<y_axis_Scnd_highest_val>\n':
                            words[0] = "NUMBER_scnd"
                        if words[1] == '<y_axis_3rd_highest_val>\n':
                            words[0] = "NUMBER_3rd"            
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