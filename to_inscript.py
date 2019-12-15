

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
        "<topic>\n",
        "<x_axis_labels>\n",
        "<topic_related_property>\n",
        "<topic_related_object>\n",   
        "<y_axis>\n",
        "<x_axis>\n",
        "<x_axis_labels_rest>\n",
        "<x_axis_labels_count>\n",   
        
        #""" "<y_axis_inferred_value_approx>\n",
        #"<y_axis_inferred_value>\n" """
    ]

for file in descriptions:
    counter = 1
    with open("delexicalized/delexicalized_" + file) as f:
        file_name = file[:-4]
        #print("file name is:")
        #print(file_name)
        with open("data1/" + file_name, "w") as f1:
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
                    line = "<end_of_description>\n"    
                if "    " in line:
                    words = line.split("    ")
                    label_found = False
                    for word in labels_dict:
                        if words[1] == word:
                            label_found = True
                    if label_found:
                    #f1.write("NUMBER")
                        if words[1] == "<topic>\n":
                            words[1] = "<topic>_" + file_name+"\n"
                        if words[1] == "<x_axis_labels>\n":
                            words[1] = "<x_axis_labels>_" + file_name+"\n"
                        if words[1] == "<topic_related_property>\n":
                            words[1] = "<topic_related_property>_" + file_name+"\n"
                        if words[1] == "<topic_related_object>\n":
                            words[1] = "<topic_related_object>_" + file_name+"\n"
                        if words[1] == "<y_axis>\n":
                            words[1] = "<y_axis>_" + file_name+"\n"
                        if words[1] == "<x_axis>\n":
                            words[1] = "<x_axis>_" + file_name+"\n"
                        if words[1] == "<x_axis_labels_count>\n":
                            words[1] = "<x_axis_labels_count>_" + file_name+"\n"
                        if words[1] == "<x_axis_labels_rest>\n":
                            words[1] = "<x_axis_labels_rest>_" + file_name+"\n"
                         
                        #if words[0] == '<end_of_description>\n':
                        #    words[0] = "<end_of_description>_" + file_name + '\n'
                        
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
                    if line == "<end_of_description>\n":
                        line = "<end_of_description>_" + file_name + "\n"
                    f1.write(line)
                #f1.write("\n") 
            f.close()
            f1.close()