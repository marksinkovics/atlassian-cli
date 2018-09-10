# jira-cli commands

* `config`  
	* `user` Manage user configurations
		* `set` Add or Update user
		* `remove` Remove user from the list
		* `set-default` Use this this for requests
		* `list` List all available users
* `myself` Show information about the logged in user (myself)
* `issue <ISSUE_ID>` Show a detailed information about the given issue
* `boards` List all available bosrds
* `board <BOARD_ID>` Show a detailed information about the given board
* `sprints <BOARD_ID>` List all available sprints for the the given board
* `sprint <SPRINT_ID>` Show a detailed information about the given sprint
* `sprint <SPRINT_ID> issues` Show a list of Issues for the given sprint
* `epics <BOARD_ID>` List all available epics for the the given board
* `epic <EPIC_ID>` Show a detailed information about the given epic
* `epic <SPRINT_ID> issues` Show a list of Issues for the given epic
* `jql "<JQL_STRING>"` Search for issues by Jira Query Language

