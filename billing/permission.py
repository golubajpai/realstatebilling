from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponseRedirect 
from django.urls import reverse



class IsMapperMixin(AccessMixin):
    """ if user is not administrator, decline permission """

    def dispatch(self, request, *args, **kwargs):
        """
        if user is authenticated and administrator
            we are good. otherwise permission denied
        """
        if request.user.is_authenticated and \
                request.user.is_mapper == \
                True:
                if len(request.user.image.all())==0:

                    return HttpResponseRedirect(reverse('admin:index'))

                else:
                    return super().dispatch(request, *args, **kwargs)

        return HttpResponseRedirect(reverse('admin:index'))  # decline permission


class IsAutnticated(AccessMixin):
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)

        else:
            raise PermissionDenied('no permision')