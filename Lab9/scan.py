from scapy.all import *
import ScanResult

def TCP_SYN_scan(**args):
    dport = args['dport']
    sport = RandShort()
    dest_ip = args['dest_ip']
    timeout = args['timeout']
    if 'sport' in args:
        sport = args['sport']
    ss_res = IP(dst=dest_ip) /TCP(sport=sport,dport=(0,dport),flags="S")
    ss_res.getlayer(TCP).display()
    ss_res=sr1(ss_res,timeout=timeout)
    if(str(type(ss_res))=="<type 'NoneType'>"):
        return ScanResult.Filtered
    elif(ss_res.haslayer(TCP)):
        if(ss_res.getlayer(TCP).flags == 0x12):
            i = send(IP(dst=dest_ip)/TCP(sport=sport,dport=dport,flags="RA"))
            ss_res[0].show()
            return ScanResult.Open
        elif (ss_res.getlayer(TCP).flags == 0x14):
            return ScanResult.Closed
    elif(ss_res.haslayer(ICMP)):
        if(int(ss_res.getlayer(ICMP).type)==3 and int(ss_res.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            return ScanResult.Filtered
    return ScanResult.Unknown

def launch_scans(config):
    port_results = []
    for port in config['dports']:
        port_results.append(TCP_SYN_scan(dport=port, dest_ip=config['dest_ip'], timeout=config['timeout']))

    return port_results

def print_results(config, port_results):
    for i in range(len(port_results)):
        report_str = "port " + str(config['dports'][i])
        report_str += " : [" + ScanResult.get_result_str(port_results[i]) + "]." 
        print report_str
    print "Scan done."
