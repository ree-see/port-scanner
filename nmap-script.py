import nmap
import tqdm

scanners = {
    0: 'sS',
    1: 'sU',
    2: 'sA',
    3: 'sW',
    4: 'sM'
}
scanr = nmap.PortScanner()

# uncomment line below for production
#ip_addr = input('Host ip addr >>> ')

ip_addr = '10.0.0.0/8'

for types in scanners:   

    type = scanners[types]
    print(f'{type}')
    scanr.scan(ip_addr, '1-1024', f'-v -{type}', True)
    print(scanr.scanstats())
