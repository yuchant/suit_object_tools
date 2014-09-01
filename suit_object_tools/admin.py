import functools
from django import http
from django.conf.urls import patterns, url


class SuitObjectActionsMixin(object):
    """ Mixin provides functionality to allow an object action upon click.
    """

    def get_urls(self):
        """ Register the user supplied action views
        """
        urls = super(SuitObjectActionsMixin, self).get_urls()
        for object_action in self.get_suit_object_actions():
            urls = patterns('', 
                url(r'^(?P<obj_pk>\d+)/{url}/$'.format(url=object_action['action_string']),
                    self.view_wrapper(object_action['function'])),
            ) + urls
        return urls

    def get_suit_object_actions(self):
        """ Prepare and get a list of valid actions
        """
        action_strings = getattr(self, 'suit_object_actions', [])
        valid_actions = []
        for action_string in action_strings:
            action_func = getattr(self, action_string, None)
            if action_func is not None:
                valid_actions.append({
                    'function': action_func,
                    'name': getattr(action_func, 'short_description', action_string),
                    'action_string': action_string,
                    'icon_class': getattr(action_func, 'icon_class', ''),
                })
        return valid_actions

    def view_wrapper(self, func):
        """ Wrap the user supplied view to accept object PK and pass the object itself to the view function.
        If the response is an HttpResponse, allow the view to return a response.
        Otherwise, redirct back to the object page with a success message.
        """
        @functools.wraps(func)
        def wrapped_function(request, obj_pk):
            obj = self.model.objects.get(pk=obj_pk)
            response = func(request, obj)

            if isinstance(response, http.HttpResponse):
                return response

            get_name = getattr(self, 'short_description', lambda: func.__name__)
            self.message_user(request, u'Executed object action: %s on %s' % (get_name(), obj), level='SUCCESS')
            return http.HttpResponseRedirect('../')
        return wrapped_function


    # def requires_confirmation(self, action_func):
    #     """ Check if this action requires a confirmation page
    #     """
    #     if getattr(self, 'suit_object_actions_require_confirmation'):
    #         return True
    #     if getattr(action_func, 'require_confirmation', None):
    #         return True
    #     return False
