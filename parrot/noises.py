from talon import Module, Context, cron, actions
import time

mod = Module()
state = {}
cron_jobs = {}
callbacks = {}
shush_start: float = 0

ctx = Context()
ctx.matches = r"""
mode: command
mode: dictation
"""

@ctx.action_class("user")
class UserActions:
    def noise_pop():
        actions.user.mouse_on_pop()

    def noise_cluck():
        if not last_command_is_sleep():
            actions.core.repeat_phrase()

    def noise_shush_start():
        actions.mouse_scroll(-3, by_lines=True)
        
    def noise_shush_stop():
        actions.mouse_scroll(0, by_lines=True)

    def noise_hiss_start():
        actions.mouse_scroll(3, by_lines=True)

    def noise_hiss_stop():
        print("mouse_scroll_stop")
        actions.mouse_scroll(0, by_lines=True)



@mod.action_class
class Actions:
    def noise_debounce(name: str, active: bool):
        """Start or stop continuous noise using debounce"""
        if active:
            state[name] = time.time()
            callbacks[name](active)
        
        cron_jobs[name] = cron.after("30ms", lambda: check_stop_condition(name))
        

    def noise_pop():
        """Noise pop"""

    def noise_cluck():
        """Noise cluck"""

    def noise_shush_start():
        """Noise shush started"""

    def noise_shush_stop():
        """Noise shush stopped"""

    def noise_hiss_start():
        """Noise hiss started"""

    def noise_hiss_stop():
        """Noise hiss stopped"""


def last_command_is_sleep():
    cmd, _ = actions.core.last_command()
    return cmd.script.code.startswith("user.talon_sleep()")


def check_stop_condition(name: str):
    time_since_start = time.time() - state[name]
    if time_since_start > 0.1:
        callbacks[name](False)
        cron_jobs[name] = None
    else:
        cron_jobs[name] = cron.after("30ms", lambda: check_stop_condition(name))


def on_shush(active: bool):
    if active:
        # actions.user.debug("shush:start")
        print("shush:start")
        actions.user.noise_shush_start()
    else:
        
        # actions.user.debug("shush:stop")
        print("shush:stop")
        actions.user.noise_shush_stop()


def on_hiss(active: bool):
    if active:
        # actions.user.debug("hiss:start")
        print("hiss:start")
        actions.user.noise_hiss_start()

    else:
        # actions.user.debug("hiss:stop")
        print("hiss:stop")
        actions.user.noise_hiss_stop()


callbacks["shush"] = on_shush
callbacks["hiss"] = on_hiss
