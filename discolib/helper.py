from prettytable import PrettyTable
import websockets 
import datetime
from .Map import MAP


def get_pretty_dt_time(date_time_str):
    if date_time_str is not None:
        utc_dt_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        utc_now = datetime.datetime.utcnow()
        diff = utc_now - utc_dt_time_obj

        days = diff.days

        weeks, _days = divmod(days, 7)

        if weeks > 0:
            if _days == 0:
                return f'{weeks}w ago'.ljust(14)
            return f'{weeks}w {_days}d ago'.ljust(14)

        seconds = diff.total_seconds()
        hours = int(seconds / 3600)

        if days > 0:
            _hours = hours - 24 * days
            if _hours == 0:
                return f'{days}d ago'.ljust(14)
            return f'{days}d {_hours}hr ago'.ljust(14)

        else:
            minutes = int(divmod(seconds, 60)[0] % 60)
            if hours == 0:
                return f'{minutes}min ago'.ljust(14)
            else:
                return f'{hours}hr {minutes}min ago'.ljust(14)


def get_val(job, col):
    levels = MAP[col]['qf'].split('.')
    curr = job
    for level in levels:
        _next = curr.get(level)
        if _next is None:
            curr = None
            break
        curr = _next
    if curr is not None and MAP[col]['is_timestamp']:
        curr = get_pretty_dt_time(curr)
    return '--' if curr is None else curr


def get_table_row(job, cols):
    # return list containing the fields in the cols ['ad', None, 'ada', 'date']
    row = []
    for col in cols:
        row.append(get_val(job, col))
    return row


def generate_table(jobs, attrs):
    table = PrettyTable(border=False, header=True)
    cols = list()
    if attrs is None:
        #print default table (id, name, status, submitted_at, scheduled_at, started_at, exited_at, scheduled_on)
        cols = ['id', 'name', 'status', 'submitted', 'scheduled',\
        'started', 'exited', 'scheduled_on']
    else:
        # print user custom table
        cols = ['id']
        items = attrs.split(',')
        for item in items:
            if item != 'id':
                cols.append(item)
    cols.sort(key=lambda item: MAP[item]['rank'])
    COLS = list(map(lambda item: item.upper(), cols))
    table.field_names = COLS
    for job in jobs:
        row = get_table_row(job, cols)
        table.add_row(row)
    return table


def print_timeline(job):
    cols = ['submitted', 'scheduled', 'started', 'exited', 'scheduled_on', 'exit_code']
    info = get_table_row(job, cols)
    *timestamps, scheduled_on, exit_code = info

    if timestamps[1] == '--':
        print(f'''
    O--------------(waiting)
    |                  
    |                 
    Submitted          
    {timestamps[0]}                
    ''')

    elif timestamps[2] == '--':
        print(f'''
    O----------------------O--------------(waiting)
    |                      |                                                           
    |                      |                                          
    Submitted              Scheduled                          
    {timestamps[0]}         {timestamps[1]}                 
                           (on {scheduled_on})
    ''')

    elif timestamps[3] == '--':
        print(f'''
    O----------------------O----------------------O--------------(running)
    |                      |                      |                                    
    |                      |                      |                      
    Submitted              Scheduled              Started              
    {timestamps[0]}         {timestamps[1]}         {timestamps[1]}        
                           (on {scheduled_on})
    ''')

    else:
        print(f'''
    O----------------------O----------------------O----------------------O----------------------O
    |                      |                      |                      |                      Done
    |                      |                      |                      |
    Submitted              Scheduled              Started                Exited ({exit_code})
    {timestamps[0]}         {timestamps[1]}         {timestamps[2]}         {timestamps[3]}        
                           (on {scheduled_on})
    ''')


async def viewlog(job_id, tail):
    try:
        async with websockets.connect(uri='ws://localhost:34543/joblogs?job_id='\
            f'{job_id}&tail={tail}') as websocket:
            while True:
                message = await websocket.recv()
                if message == "ping":
                    await websocket.send("pong")
                else:
                    print(f"< {message}")
    except websockets.exceptions.ConnectionClosedError as e:
        print("Uh oh! Connection Closed: {}".format(e))
    except websockets.exceptions.InvalidMessage as e:
        print(f"Something went wrong - {e.__class__.__name__}: {e}")
    except websockets.exceptions.ConnectionClosedOK as e:
        print(f"{e.__class__.__name__}: {e}")
