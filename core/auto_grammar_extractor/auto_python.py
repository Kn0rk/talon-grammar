from talon import Context, Module, actions
ctx = Context()
ctx.matches = '\napp: jetbrains\n'
mod = Module()
python_keywords = {'false': 'False', 'none': 'None', 'true': 'True', 'and': 'and', 'as': 'as', 'assert': 'assert', 'async': 'async', 'await': 'await', 'break': 'break', 'class': 'class', 'continue': 'continue', 'define': 'def', 'elif': 'elif', 'else': 'else', 'except': 'except', 'finally': 'finally', 'for': 'for', 'from': 'from', 'global': 'global', 'if': 'if', 'import': 'import', 'in': 'in', 'is': 'is', 'lambda': 'lambda', 'nonlocal': 'nonlocal', 'not': 'not', 'or': 'or', 'pass': 'pass', 'raise': 'raise', 'return': 'return', 'try': 'try', 'while': 'while', 'with': 'with', 'yield': 'yield', 'telephone': 'THIS IS TEST'}
mod.list('vocabulary', desc='additional vocabulary words')
automatically_generated_mapping = {'django': 'django', 'import': 'import', 'views': '.views', 'bloglistview': 'BlogListView', 'blogdetailview': 'BlogDetailView', 'blogcreateview': 'BlogCreateView', 'blogupdateview': 'BlogUpdateView', 'blogdeleteview': 'BlogDeleteView', 'urlpatterns': 'urlpatterns', 'as view': '.as_view', 'as': 'as'}
mod.list('python_keywords', desc='Automatically extracted key words from python files')
ctx.lists['self.python_keywords'] = dict(automatically_generated_mapping, **python_keywords)
ctx.lists['user.vocabulary'] = dict(automatically_generated_mapping, **python_keywords)

@mod.capture(rule='{self.python_keywords}+')
def python_keywords(m) -> str:
    return ''.join(m.python_keywords_list)