The original data was modified by adding information about the x axis: whether or not the categories on the x axis are ordered, if yes how.

Example:

new = {"x_is_ordered":True, "x_order":['2000', '2005', '2010', '2015'], "order":"ascending"}

In practice, two plot datasets have ordered x categories:
- Median Salary of Women Per Year: {"x_is_ordered":True, "x_order":['2000', '2005', '2010', '2015'], "order":"ascending"}

- Median Salary Per Year For Software Engineers with Respect to their Degree: {"x_is_ordered":True, "x_order":['No Degree','Bachelor', 'Master', 'PhD'], "order":"ascending"}

Other plot datasets were assigned {"x_is_ordered":True, "x_order":['No Degree','Bachelor', 'Master', 'PhD'], "order":"ascending"}
