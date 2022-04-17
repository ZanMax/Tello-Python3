def print_log(response):
    for stat in response:
        stat.print_stats()
        print(stat.return_stats())


def banner(title):
    print("--------------------------------")
    print("| {}".format(title))
    print("| Type 'help' for a list of commands")
    print("--------------------------------")
