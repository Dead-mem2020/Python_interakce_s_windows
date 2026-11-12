from subprocess import Popen, PIPE

cmd = ['powershell.exe', '-ExecutionPolicy', 'Bypass', '-File', 'C:\\Users\\Stanislav.Roll\\Python_interakce_s_windows']

proc = Popen(cmd, stdout=PIPE, stderr=PIPE)

#while True:
