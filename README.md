Django Suit Object Tools
------------------------

> Note: this is not an official django suit package. This is just an extremely light weight addition consisting of < 100 lines.

Django suit provides a sidebar with "object tools" such as "Add another <object>" which is a perfect opportunity to add what django has long been missing: per-object actions.

Most importantly, we replicate the pattern familiar by heart to any django developer: django admin actions.

![Object Tools.gif](object_tools.gif)

How did we come this far without this?


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

```python
from suit_object_tools.admin import SuitObjectActionsMixin


class MyAdmin(SuitObjectActionsMixin, admin.ModelAdmin):
    suit_object_actions_title = 'Custom Actions Title'
    suit_object_actions = [
        'object_action',
    ]

    def object_action(self, request, obj):
        obj.do_something()
        self.message_user(request, 'Did something')

    object_action.short_description = 'Do Something'
    object_action.icon_class = 'icon-cog icon-alpha75'
```




# License
    This file is part of the python package Suit Object Tools.

    Suit Object Tools is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Suit Object Tools is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Suit Object Tools.  If not, see <http://www.gnu.org/licenses/>.
