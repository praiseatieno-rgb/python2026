# Create a tuple of languages with 10 international languages. If English is found in th tuple, terminate the loop and print ("English is found")


languages = ("French", "Spanish", "German", "Chinese", "Arabic", "English", "Swahili", "Portugese", "Russian", "Japanese")

found = False

for language in languages:
  if language == "English":
    print("English is found")
    found = True

    if found == False:
      print("English is not found")