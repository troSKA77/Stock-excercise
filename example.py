Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@troSKA77 
troSKA77
/
Stock-excercise
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Stock-excercise
/
Name your file…
in
main
 
import pandas as pd

"""So I tried to simulate similar list of lists as I saw in your video and called this list elements

So we have following list (first one):
["0", "20002154", "NIFRA", "10", "20", "50", "85", "47"]

And our purpose is to find if there is another list in elements where index [2] is "NIFRA"
If so - element in index [5] of original (first one) will be replaced with value from matched list[5]

So expected result after compiling this code is list:
["0", "20002154", "NIFRA", "10", "20", "54", "85", "47"]

value 50 in index 5 has been replaced by 54 from index 5 of matched list"""

elements = [
    ["0", "20002154", "NIFRA", "10", "20", "50", "85", "47"],
    ["1", "20002154", "SIL", "11", "20", "50", "85", "47"],
    ["2", "20002154", "Whatever", "15", "20", "50", "54", "47"],
    ["3", "20002154", "SIL", "14", "20", "50", "85", "47"],
    ["4", "20002154", "RANDOM", "19", "20", "50", "87", "47"],
    ["5", "20002154", "SIL", "17", "20", "50", "85", "47"],
    ["6", "20002154", "SIL", "11", "20", "50", "85", "47"],
    ["7", "20002154", "RANDOM", "20", "20", "50", "85", "47"],
    ["8", "20002154", "NIFRA", "11", "24", "54", "85", "35"]
]

result = elements[0] #creating result variable containing first list from scrapped data which will be updated later

"""Using pandas dataframe I transferred data to dataframe object called df
I called column names by its index as I do not understand data
I also exluded elements[0] as this is stored in result variable that's why we have elements[1:] as first argument"""

df = pd.DataFrame(elements[1:], columns=["index 0", "index 1", "index 2", "index 3", "index 4", "index 5", "index 6", "index 7"])

"""As we need to find only rows from this dataframe where index 2 is NIFRA one of possible solution
I thought about is to drop all other rows / lists from these data so we have present only those relevant for our function

We can create another variable containing only those data but in this case I= m gonna assign it to the same
as we do not need other rows for this analysis for now"""

df = df.drop(df[df["index 2"] != "NIFRA"].index) #df.drop will remove from df all rows (indexes) where value in column "index 2 is not NIFRA"

"""Now we have only one row in this dataframe - the matched one

If there will be more lists in data where index[2] is NIFRA all of them will still be part of it

Now we need to extract value from index 5 column of this row so we can add it to result[5]
I used iloc fiunction - some explanation can be found for example here:
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html
or here:
https://www.geeksforgeeks.org/python-extracting-rows-using-pandas-iloc/
"""

result[5] = df['index 5'].iloc[0]

print(result)
@troSKA77
Commit new file
Commit summary
value_update.py
Optional extended description
value_update.py
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
