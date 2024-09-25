from rest_framework import permissions


class GlobalPermissionClass(permissions.BasePermission):
    metodo_para_acao = {
        'GET': 'view',
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete',

    }
    
    
    def has_permission(self, request, view):

        codename = self.__get_codename(request, view)
        if codename:
            return request.user.has_perm(codename)
        
        return False
    
    def __get_codename(self, request, view):

        try:
            nome_do_model = view.queryset.model._meta.model_name
            etiqueta_do_label = view.queryset.model._meta.app_label
            metodo = self.__get_method(request)
            return f"{etiqueta_do_label}.{metodo}_{nome_do_model}"
        except:
            return None
    
    def __get_method(self, request):
        acao = self.metodo_para_acao.get(request.method)
        
        if acao:
            return acao
        return None
