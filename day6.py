import subprocess
import time
intf = "Беспроводное сетевое соединение "
cmd = "ping -n 1 8.8.8.8"
#cmd = "ping -n 1 192.168.8.8" # 'Ответ от 192.168.8.100: Заданный узел недоступен.'
count = 0
wifiisup = True
while True:
    try:
        sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
        rt = sp.wait()
        out, err = sp.communicate()
        out = out.strip().decode("cp866").split('\r\n')
        #print(out, err)
        tm = out[1].split('=')[2].split(' ')[0]
        print(int(tm.replace('мс', '').replace('ms', '')))
        count = 0

    except:

        if count > 2 and wifiisup:
            cmdw = 'netsh interface set interface name="' + intf + '" admin = '
            sp = subprocess.Popen(cmdw + 'DISABLED', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rt = sp.wait()
            print("disabled interface")
            wifiisup = False
            print("WiFi is down!")
            time.sleep(2)
        else:
            count += 1
            print("error response " + str(count))

        if not wifiisup:
            sp = subprocess.Popen(cmdw + 'ENABLED', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            rt = sp.wait()
            #print(cmd)
            wifiisup = True
            count = 0
            print("WiFi is up!")
            time.sleep(12)
    time.sleep(2)