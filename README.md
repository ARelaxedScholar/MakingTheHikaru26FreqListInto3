# MakingTheHikaru26FreqListInto3
A simple script I written as a a way to bypass the free-user restriction on **JPDB** for making decks from text files (max 10k). This is made specifically to split the Hikaru 26k freq list, to three decks of 10k-10k-6k respectively. Written in such a way that the output file contains only the term itself since the order they appear in already indicates freq. For context, this is the frequency list for words said by Hikary (a japanese youtuber) to study in parallel of the Hikaru Challenge. For even more context: https://www.youtube.com/watch?v=hdsp3cMl_20&t=2s .

This is python code, and it **assumes a few things**.
1. Your source name is "actual_hikaru_freq.txt"
2. You want your file split in three parts of 10k-10k-rest of the file
3. You are dealing with an Hikaru freq list and want your output files labeled as such.

There's really not much to change if these assumptions are false, just rename the input and output files to whatever you feel like,
and play with the range of the in range functions to make them do your bidding.

## How I used it:
1. Create a python file with the above code, and put that file in the same directory as the frequency list (this code assumes the file is named actual_hikaru_list.txt, if its not, just change it to whatever yours is)
2. Run the python file, you should get 3 files.
3. In JPDB, while in your "Learn" tab, scroll to the very bottom and click on the "New Deck From Text" option.
4. Paste the content of the first file in.
5. Repeat steps 3-4 for the second and third file.
6. When comes time to study the Hikaru decks, set whichever you're at as your "Highest priority deck" and in your settings set the "New Vocabulary Order" setting to "One Deck at a time, chronologically".

*Note: This is only useful if you're a non patreon JPDB user, patreon members can upload up to 50k in one go apparently. Useful for penny grubbers like me (who happen to use jpdb).*

If you've seen this exact thing on discord before, be assured it's not plagiarism, my discord handle is Orosei#8053.
