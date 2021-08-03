_disco-cli v0.0.1_

### To install **disco-cli**, run:

```
pip install git+https://github.com/grayatom/disco-CLI.git
```

Disco CLI provide the following commands :

1. whoami
2. list
3. describe
4. status
5. log

### 1. The **whoami** command

-This command prints the email id of the user.

```
disco whoami
```

![whoami](./static/whoami.png)

### 2. The **list** command

-This command helps user to list all the jobs he/she ever submitted to disco.

```
disco list
```

![list](./static/list.png)
-This command offers the functionality to filter jobs as per user's need, using the `--filter` option.

```
disco list --filter name=testjob1
```

_the accepted format is **--filter key=value**_

![filter_one](./static/filter_one.png)

-Users can also apply multiple filters.

```
disco list --filter name=testjob2 --filter status=scheduled
```

![filter_multiple](./static/filter_multiple.png)

-This command also offers users to select the fields (columns) they want to see using the `--attributes` command.

```
disco list --attributes name,status,scheduled_on
```

_the valid format is **--attributes attr1,attr2,attr3,attr4** (comma separated without any space)_

![attribute](./static/attr.png)
