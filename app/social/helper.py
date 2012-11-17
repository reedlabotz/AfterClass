def isWelcome(user):
   if len(user.first_name) == 0:
      return False
   if user.get_profile().monday_availability == "":
      return False
   return True