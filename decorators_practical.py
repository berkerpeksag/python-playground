# Examples are taken from the following link but slightly modified.
#
# https://github.com/hchasestevens/posts/blob/master/notebooks/the-decorators-they-wont-tell-you-about.ipynb


def process_list(list_):
    def decorator(function):
        return function(list_)
    return decorator

unprocessed_list = [0, 1, 2, 3]


@process_list(unprocessed_list)
def processed_list(items):
    return [item for item in items if item > 1]

print(processed_list)


# -----------------


def invoke(func):
    return func()


@list
@str.upper
@invoke
def name():
    return 'berker'

print(name)


# -----------------


def registered(fn):
    registered.registry.append(fn)
    return fn

registered.registry = []


@registered
def step_1():
    print('Hello')


@registered
def step_2():
    print('world!')


def run_all():
    for function in registered.registry:
        function()

run_all()
