# qf = query fragment
# MAP is for mapping user's input to the query fragment to be used in api to get jobs
MAP = {
    'id': {
        'qf': '_id',
        'rank': 0,
        'is_timestamp': False
    },
    'name': {
        'qf': 'Name',
        'rank': 1,
        'is_timestamp': False
    },
    'status': {
        'qf': 'State.Status',
        'rank': 2,
        'is_timestamp': False
    },
    'submitted': {
        'qf': 'Events.Submitted.Time',
        'rank': 3,
        'is_timestamp': True
    },
    'scheduled': {
        'qf': 'Events.Scheduled.Time',
        'rank': 4,
        'is_timestamp': True
    },
    'started': {
        'qf': 'Events.Started.Time',
        'rank': 5,
        'is_timestamp': True
    },
    'exited': {
        'qf': 'Events.Exited.Time',
        'rank': 6,
        'is_timestamp': True
    },
    'last_modified': {
        'qf': 'LastModified',
        'rank': 7,
        'is_timestamp': False
    },
    'scheduled_on': {
        'qf': 'Events.Scheduled.On',
        'rank': 8,
        'is_timestamp': False
    },
    'exit_code': {
        'qf': 'Events.Exited.ExitCode',
        'rank': 9,
        'is_timestamp': False
    },
    'user_arn': {
        'qf': 'UserDetails.ARN',
        'rank': 10,
        'is_timestamp': False
    },
    'user_email': {
        'qf': 'UserDetails.Email',
        'rank': 11,
        'is_timestamp': False
    },
    'exec_script': {
        'qf': 'Config.ExecScript',
        'rank': 12,
        'is_timestamp': False
    },
    'gpus': {
        'qf': 'Config.NumberOfGPUsRequested',
        'rank': 13,
        'is_timestamp': False
    },
    'python_version': {
        'qf': 'Config.PythonVersion',
        'rank': 14,
        'is_timestamp': False
    },
    'cuda_version': {
        'qf': 'Config.CudaVersion',
        'rank': 15,
        'is_timestamp': False
    },
    'shm': {
        'qf': 'Config.SharedMemorySize',
        'rank': 16,
        'is_timestamp': False
    },
    'package_bucket': {
        'qf': 'PackageLocation.BucketName',
        'rank': 17,
        'is_timestamp': False
    },
    'package_key': {
        'qf': 'PackageLocation.Key',
        'rank': 18,
        'is_timestamp': False
    },
    'package_src': {
        'qf': 'PackageLocation.Source',
        'rank': 19,
        'is_timestamp': False
    },
    'data_node': {
        'qf': 'data_node_name',
        'rank': 20,
        'is_timestamp': False
    },
    'data_path': {
        'qf': 'data_path',
        'rank': 21,
        'is_timestamp': False
    },
}