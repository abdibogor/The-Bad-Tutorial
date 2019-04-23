sp=1500
cp=1200
if (sp>cp):
    print("Congratulations!")
    print("You've made a profit of",sp-cp,"bucks")
elif (cp>sp):
      print("Oops!")
      print("You've made a loss of", cp-sp, "bucks")
else:
     print("You didn't make or lose money.")
