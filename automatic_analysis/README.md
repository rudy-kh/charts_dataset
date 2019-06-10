## Automatic analysis of raw data for bar charts

Apart from raw data, the input to the NLG system should also be results of automatic analysis of the data.

For a bar chart with categorical data on the x axis, the analysis would output: 
- ordered categories according to their y values
- relative differences between categories as raw values (A has 30 more/less million than B) or 
- as multipliers (A has 2 times more/less than B)

The data comes as a json file, specifically as annotations.json

More about the format: https://github.com/rudy-kh/FigureQA/blob/dev/docs/annotations_format.md
