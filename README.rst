toJiraTable
===========

Reads input from stdin and converts it to a JIRA table.


The first line it reads is used as the table header, and all subsequent lines are made into the body. Supports shell\-style splitting of fields (you can use quotes to "group" items with spaces into a single field).


By default, it will split by whitespace, so each word becomes an item. The entire table, by default, will grow to the longest row, and fill in blanks where needed.


If you need to split by an alternative thing, such as two\-spaces (if columns are seperated by two\-or\-more spaces, and contain characters with spaces between) there are various \-\-split\-by options available, see usage below. See usage and examples for more information.


**Usage:**


	Usage: toJiraTable

	Converts stdin to a JIRA table. If no arguments provided, it will use "shell\-style" splitting

		so quoting strings with spaces makes them a single column, otherwise spaces/tabs/whatever

		splits. The first line passed in becomes the header, the remainder become the body.


	By default, everything will be matched to the longest row. Any missing columns in a row will

		be filled by blank columns at the end. Use \-\-no\-stretch to disable this.


		Arguments:


			\-\-no\-stretch                \-  Do not stretch each row to the longest row. See above.

			\-\-split\-header\-by=X         \-  Instead of using shell\-style splitting, split by provided string for the header line

			\-\-split\-body\-by=X           \-  Instead of using shell\-style splitting, split by the provided string for body lines

			\-\-split\-by=X                \-  Split both header and body by the given string

			\-\-split\-keep\-empty          \-  By default, using the \-\-split\-by* will strip empty columns. The default behaviour is 

										 useful, in example: if a script outputs strings which are not quoted, but has at least two

										 spaces between each real column, using \-\-split\-body\-by='  '  will ensure that any place that 

										 is separated by two or more spaces becomes a column. This option disables that feature.



**Example Usage:**


*Simple split:*


	[myuser]$ ( echo 'Hostname "Free Space"'; cat hostnames.txt ) \| toJiraTable 

	\|\|Hostname\|\|Free Space\|\|

	\|host1\|500G\|

	\|wwwprod1\|120G\|

	\|wwwdev1\|11G\|


*More complicated split. In this case, we want the body to form columns any time there are at least two spaces:*


(dataset)


	[myuser]$ cat myData

	Name Size Comment

	George Jetson  500G    The man from the future

	Jeeves  200M           Everyone's favourite butlet


(convert to JIRA table)


	[myuser]$ cat myData \| ./toJiraTable \-\-split\-body\-by="  "

	\|\|Name\|\|Size\|\|Comment\|\|

	\|George Jetson\|500G\|The man from the future\|

	\|Jeeves\|200M\|Everyone's favourite butlet\|



*Tab\-deliminated split:*


(dataset):

	[myuser]$ python \-c "import sys; sys.stdout.write(repr(open('myData', 'rt').read()).replace('\\\\n', '\\n') + '\n');"

	"Name\tSize\tComment

	George Jetson\t500G\tThe man from the future

	Jeeves\t200M\tEveryone's favourite butlet

	"


(convert to JIRA table)

	[myuser]$ cat myData \| ./toJiraTable \-\-split\-by='\t'

	\|\|Name\|\|Size\|\|Comment\|\|

	\|George Jetson\|500G\|The man from the future\|

	\|Jeeves\|200M\|Everyone's favourite butlet\|


