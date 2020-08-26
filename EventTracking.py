class Event:
    def __init__(self, date, type, machine, user):
        self.Date = date
        self.Type = type
        self.Machine = machine
        self.User = user
    def __str__(self):
        return "Login el dia: {} el usuario: {}".format(self.Date, self.User)


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

def get_event_date(event):
    return event.Date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.Machine not in machines:
            machines[event.Machine]  = set()
        if event.Type == "login":
            machines[event.Machine].add(event.User)
        elif event.Type == "logout":
            if(event.User in machines[event.Machine]):
                machines[event.Machine].remove(event.User)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine,user_list))

users = current_users(events)
generate_report(users)





