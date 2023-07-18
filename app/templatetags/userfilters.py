from django import template

register=template.Library()



@register.filter('swapping')# swapping is the filter name for swap function
def swap(data):
    return data.swapcase()


@register.filter()#it considers function name as Filter name
def remove(data,arg):
    return data.replace(arg,'')


#register.filter('swap',swap)
#register.filter('remove',remove)






