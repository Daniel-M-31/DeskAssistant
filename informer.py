import os, psutil, datetime, threading, time

class Info_CPU:
    def __init__(self):
        self.cpu_perf = []

    def info_cpu_time(self) -> dict:
        '''Retorna o tempo de inicialização do boot do pc'''

        cptime = psutil.boot_time()
        act_time = datetime.datetime.now()
        cptime = (time.time() - cptime)
        act_time = act_time - datetime.timedelta(seconds=cptime)
        act_time = act_time.strftime("%d/%m/%y horario do boot: %H:%M:%S")
        #retorna a data formatada e o tempo de execução em segundos
        return {'data_init': act_time, 'exe_time': cptime }

    def info_cpu_performance(self) -> dict:
        def check():
            cpperf_geral = psutil.cpu_percent(interval=1)
            cpperf_all = psutil.cpu_percent(interval=1, percpu=True)
            if not self.cpu_perf:
                self.cpu_perf.append({"cpu_performance_geral": cpperf_geral, "cpu_performance_all": cpperf_all})
            else:
                self.cpu_perf[0] = {"cpu_performance_geral": cpperf_geral, "cpu_performance_all": cpperf_all}
        check_cpu = threading.Thread(target=check, daemon=True)
        check_cpu.start()

if __name__ == '__main__':
    info = Info_CPU()
    cpu = info.cpu_perf
    info.info_cpu_performance()
    time.sleep(3)
    print(cpu)