Django Suit Object Tools
------------------------

Django suit provides a sidebar with "object tools" such as "Add another <object>" - this is a perfect opportunity to add what django has long been missing: per-object actions.

![Object Tools.gif](object_tools.gif)



## Installation

- `pip install suit_object_tools`  
- add `suit_object_tools` to `INSTALLED_APPS` *before* `suit`

## Simple Usage

- Mix in `suit_object_tools.admin.SuitObjectActionsMixin` to your `ModelAdmin` class
- Add `suit_object_actions` attribute consisting of a list of local function names
- Define functions matching above names which accept `request, obj` as arguments
- Profit


## More Usage

- Define a `short_description` property on the function to override the default name
- Define an `icon_class` property on the functionto override the default icon (bootstrap 2 icons)
- Return an `http.HttpResponse` subclass to render your view instead of redirecting back to the object page.



## Full Example

	from suit_object_tools.admin import SuitObjectActionsMixin


	class MyAdmin(SuitObjectActionsMixin, admin.ModelAdmin):
	    suit_object_actions = [
	        '_object_action',
	    ]

	    def _object_action(self, request, obj):
	    	obj.do_something()
	    	self.message_user(reqest, 'Did something')

	    _object_action.short_description = 'Do Something'
	    _object_action.icon_class = 'icon-cog icon-alpha75'
