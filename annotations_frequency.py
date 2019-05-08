import re
pattern = re.compile("<>")

#for i, line in enumerate(open('test.txt')):
#    for match in re.finditer(pattern, line):
#        print 'Found on line %s: %s' % (i+1, match.groups())



def word_frequencies(file_list):
    """
    Returns a dictionary with the frequencies
    of the annotations occurring on file with name.
    """
    result = {}
    for file in file_list:
        file1 = open(file, 'r')
    
        while True:
            line = file1.readline()
            if line == '':
                break
            words = line.split(' ')
            for word in words:
                if "<" in word:
                    if word.rstrip().strip() in result:
                        result[word.rstrip().strip()] += 1
                    else:
                        result[word.rstrip().strip()] = 1
        file1.close()
    return result
#


#s = (word_frequencies(file_list))   
#sorted_by_value = sorted(s.items(), key=lambda kv: kv[1], reverse = True) 
#print (s)
#for item in sorted_by_value:
#    print (item + "\n")

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
#files = ["gender_pay_gap.txt"]    
# 
#      

#files = ["gender_pay_gap.txt"]         
s1 = (word_frequencies(descriptions))   
#s2 = (word_frequencies(files))
sorted_by_value = sorted(s1.items(), key=lambda kv: kv[1], reverse = True)
#sorted_by_value = sorted(s2.items(), key=lambda kv: kv[1], reverse = True)


with open('tags_freq_10.txt', 'w') as f:
#with open('gender_pay_gap_labels.txt', 'w') as f:
    for item in sorted_by_value:
        
        f.write('%s = %d \n' % item)
        #f.write("\n")

