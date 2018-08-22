# atlassian-cli 
> the "missing" command-line interface for Atlassian products :rocket:

## **Important notice** :construction:

This project is in development phase which means some breaking change is unavoidable in the future.

## Goals

The main purpose of this project is to create a command-line interface for Atlassian products (mainly Jira, Bitbucket and Confluence) in order to make possible other scripts (bash, python, etc) to easily communicate and modify those products.

This project is separated into 2 parts. The first is a reusable pip package which could be used other python scripts. While the second part is a the actual terminal interface.

## Development

More information about development can be found [here](docs/development.md)

## Command-line interfaces

There are 2 main commands `jira-cli` and `bitbucket-cli`. Both have help menu which can give more information about the available options.

The first level of commands is the following:

* Jira `jira-cli`

	```
	usage: jira-cli [-h] [--version]
	                {config,myself,issue,boards,board,sprints,sprint,jql} ...
	
	positional arguments:
	  {config,myself,issue,boards,board,sprints,sprint,jql}
	                        commands
	    config              Config
	    myself              Show information about current user (myself)
	    issue               Show issue by id
	    boards              Show available boards
	    board               Show a specific board by id
	    sprints             Show sprints for a specific board
	    sprint              Show details of a specific sprint
	    jql                 Jira Query Language
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --version             show program's version number and exit
	```

* Bitbucket `bitbucket-cli`

	```
	usage: bitbucket-cli [-h] [--version]
	                     {config,projects,project,my-pull-requests,my-pull-requests-count}
	                     ...
	
	positional arguments:
	  {config,projects,project,my-pull-requests,my-pull-requests-count}
	                        commands
	    config              Config
	    projects            projects
	    project             project
	    my-pull-requests    my-pull-requests
	    my-pull-requests-count
	                        my-pull-requests-count
	
	optional arguments:
	  -h, --help            show this help message and exit
	  --version             show program's version number and exit
	```

## TODO

### Common service handling

- [x] use requests
- [x] use authenticators
- [x] store credentials
- [ ] handle env variables
- [ ] give path by env variables too

### Bitbucket service

- [ ] pull-requests
- [ ] list of pull-requests
- [ ] show diff (by commit) at pull-requests

### Jira service

- [ ] show current sprint
- [ ] show tickets

### Confluence

- [ ] search pages
- [ ] create, edit pages
