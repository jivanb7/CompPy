# DO NOT ADD LIBRARIES/PACKAGES.
# If you want to cover additional error cases other than the given below,
# feel free to create a error message.

spotify = {
    1: {"artists": ["ROSÉ", "Bruno Mars"], "title": "APT.", "length": "2:49"},
    2: {"artists": ["Lady Gaga", "Bruno Mars"], "title": "Die With a Smile",
        "length": "4:11"},
    3: {"artists": ["Ed Sheeran"], "title": "Sapphire", "length": "2:59"},
    4: {"artists": ["Billie Eilish"], "title": "Birds of a Feather",
        "length": "3:30"},
    5: {"artists": ["Benson Boone"], "title": "Beautiful Things",
        "length": "3:00"},
    6: {"artists": ["Sabrina Carpenter"], "title": "Manchild",
        "length": "3:33"},
    7: {"artists": ["Alex Warren"], "title": "Ordinary", "length": "3:06"},
    8: {"artists": ["Billie Eilish"], "title": "Wildflower", "length": "4:21"},
    9: {"artists": ["Sabrina Carpenter"], "title": "Espresso",
        "length": "2:55"},
    10: {"artists": ["Lady Gaga"], "title": "Abracadabra", "length": "3:43"}
}


user_choice_question = "Enter what you would like to browse:\n \
                        \t1: A list of artists in the top 10 most played songs\n \
                        \t2: Song by ranking\n \
                        \t3: Songs by an artist\n \
                        \t4: Songs ordered by length\n \
                        \t0: Exit\n"

ranking_question = "Enter the ranking you're interested in (between 1 and 10): "
ranking_value_error = "Invalid input. Please enter a number."
ranking_range_error = "Ranking out of range."

artist_question = "Enter the name of the artist you're interested in: "
artist_error = "No songs were found by "

length_question = "Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): "
length_value_error = "Invalid vallue. Please enter a number."

# CODE START
def main ():
    state = True;
    while state:
        user = input(user_choice_question)

        if (user == "1"):
            empty = set();
            for i in spotify:
                for art in spotify[i]["artists"]:

                    if art not in empty:
                        empty.add(art)
            
            print(", ".join(sorted(empty)))
            state = False;
            

        elif (user == "2"):
            user2 = input("Enter the ranking you're interested in (between 1 and 10) : ")

            if (not user2.isdigit()):
                print("Invalid input. Please enter a number.")
                state = False;
            
            elif (int(user2) < 0 or int(user2) > 11):
                print("Ranking out of range.")
                state = False;
            
            else:
                print(f"{int(user2)}: {spotify[int(user2)]['title']} by {', '.join(spotify[int(user2)]['artists'])}")
                state = False;


        elif (user == "3"):
            user3 = input("Enter the name of the artist you're interested in: ")

            count = 0

            for i in spotify:
                for person in spotify[i]["artists"]:
                    if (person.lower() == user3.lower()):
                        print(f"{i}: {spotify[i]['title']}")
                        count+=1
                state = False;
            if (count == 0):
                print(f"No songs were found by {user3}")
                state = False;

        elif (user == "4"):
            user4 = input("Enter a number to view songs by length. (Positive: longest songs, Negative: shortest songs): ")

            if (user4.isdigit() or int(user4)):
                if (int(user4) > 0):
                    list1 = (list(spotify.values()))
                    s = sorted(list1, key=lambda item: item['length'], reverse=True)
                    for item in s[:int(user4)]:
                        min, sec = item["length"].split(":")
                        seconds = (int(min) * 60) + int(sec)
                        print(f"{item['title']} by {', '.join(item['artists'])} ({seconds} seconds)")
                    
                    state = False

                elif (int(user4) < 0):
                    list1 = (list(spotify.values()))
                    s = sorted(list1, key=lambda item: item['length'], reverse=False)
                    user4 = int(user4) * (-1)
                    for item in s[:int(user4)]:
                        min, sec = item["length"].split(":")
                        seconds = (int(min) * 60) + int(sec)
                        print(f"{item['title']} by {', '.join(item['artists'])} ({seconds} seconds)")
                    
                    state = False

            else:
               print("Invalid value. Please enter a number.")

        elif (user == "0"):
            exit()

        else:
            print("Error")

main()