from talon import Module, Context

basic_module= None
basic_context = None
def getBasicModule():
    global basic_module
    if basic_module:
        return basic_module
    else:
        basic_module = Module()
        return basic_module

def getBasicContext():
    global basic_context
    if basic_context:
        return basic_context
    else:
        basic_context = Context()
        return basic_context