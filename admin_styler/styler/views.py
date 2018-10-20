import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

def opts_dict_to_sass(opts_dict):
    out = "";
    for k in opts_dict:
        out += "$%s : %s;" % (k, opts_dict[k])
    return out



base_theme = {

    'body-color' : "#333", # #333

    'header-background' : '#000',

    'breadcrumbs-background' : '#222', # #79aec8
    'breadcrumbs-color ' : '#fff', # #c4dce8
    'breadcrumbs-a-color ' : '#ccc', # #fff

    #forms
    'form-label-required' : "#333", # #333

}
    
def compile_file(scss, opts={}):

    scss_path = os.path.join(settings.BASE_DIR, "styler_theme/static/admin/scss", scss)

    #vars_scss_path = os.path.join(settings.BASE_DIR, "styler_theme/static/admin/scss", "vars.scss")

    opts_dict = {}
    opts_dict.update(base_theme)
    opts_dict.update(opts)
    scss_user = opts_dict_to_sass(opts_dict)

    with open(scss_path) as scss_file:
        scss_text = scss_file.read()

    #with open(vars_scss_path) as vars_file:
    #    vars_text = vars_file.read()
    
    full_scss = scss_user + scss_text

    from scss import Scss
    css = Scss()
    out = css.compile(full_scss)

    return out



def compile_view(request, path=None):
    out = compile_file(path)
    return HttpResponse(out, content_type='text/css')

