from django import template
from django.contrib.auth.models import User
from django.utils.html import escape,format_html
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def author_details(author,current_user=None):
  #print
  if not  isinstance(author,User):# and isinstance(current_user,User) ):
    return " "
  
  if author==current_user:
    return format_html("<strong>me</strong>")
  
  if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
  else:
      name = f"{author.username}"

  if author.email:
      prefix = format_html('<a href="mailto:{}">', author.email)
      suffix = format_html("</a>")
  else:
      prefix = ""
      suffix = ""
  
  return format_html('{}{}{}', prefix, name, suffix)