import commands

(status, output) = commands.getstatusoutput(
    'ps -ef|grep XXX.py|grep -v grep|wc -l')
execute_process_cnt = int(output.strip())
if execute_process_cnt > 2:
    print "XXX.py executing..."
    exit()