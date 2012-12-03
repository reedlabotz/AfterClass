from django.template import Context, Node, Library, TemplateSyntaxError, VariableDoesNotExist

register = Library()


@register.simple_tag
def availability_check(one,two):
   if (int(one.monday_availability,2) & int(two.monday_availability,2) > 0 or 
      int(one.tuesday_availability,2) & int(two.tuesday_availability,2) > 0 or 
      int(one.wednesday_availability,2) & int(two.wednesday_availability,2) > 0 or 
      int(one.thursday_availability,2) & int(two.thursday_availability,2) > 0 or 
      int(one.friday_availability,2) & int(two.friday_availability,2) > 0 or 
      int(one.saturday_availability,2) & int(two.saturday_availability,2) > 0 or 
      int(one.sunday_availability,2) & int(two.sunday_availability,2) > 0):
      return "true"
   return "false"