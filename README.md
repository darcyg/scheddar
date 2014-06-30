API
command line
GUI

single shot
periodic

queue
priorities
run now

priorities
pause
abort

predefined tasks
predefined tasks with parameters
free style

parallel
sequential
tag parallel

threaded
green

inspect
what was running, its output, and result
what is running
what is scheduled (incl. periodic)

tags = tags
marks what the task does

conflicts = tags
postpone if the task conflicts with a running task which 
means it does something which should not run in parallel, i.e. two tag sets 
have a non-empty intersection

compatible = tags
run only if all tasks will have something in common


queues
completed
running
ready
scheduled


Running Queue
=============

create (add)
retrieve (list, detail)
update (pause)
delete (kill, terminate)

stdout, stderr
