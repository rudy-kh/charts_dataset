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

def get_annotations(file_list, result):
    """
    Returns a dictionary of the annotations  
    """
    
    for file in file_list:
        file1 = open(file, 'r')
    
        while True:
            line = file1.readline()
            if line == '':
                break
            words = line.split('   ')
            
            for word in words:
                if "<" in word:
                    if word.rstrip().strip() in result:
                        continue
                    else:
                        result[word.rstrip().strip()] = ""
               
        file1.close()
    return result

result = {}

annotaions_dict = get_annotations(descriptions, result)

# write all annotations in all_annotations file
with open('all_annotations.txt', 'w') as f:
    for item in annotaions_dict:
        f.write(item + '\n')


def get_annotated_words(file_list, result):
    """
    Returns a dictionary of the annotations  
    """
    
    for file in file_list:
        file1 = open(file, 'r')
    
        while True:
            line = file1.readline()
            if line == '':
                break
            words = line.split('   ')
            
            for word in words:
                if "<" in word:
                    if words[0].lower() in result[word.rstrip().strip()].lower():
                        continue
                    else:
                        result[word.rstrip().strip()] += words[0] + " - "     
               
        file1.close()
    return result


key_value_dict = get_annotated_words(descriptions, annotaions_dict)

# write all words and their annotations in a file
with open('all_annotations_with_values.txt', 'w') as f:
    for key, value in key_value_dict.items():
        f.write(key + ' =  '+ value + '\n')
