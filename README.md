# Tugas-Akhir
Tugas Akhir Arsitektur Jaringan Terkini

## BAB 1 Menginstall MiniNet, Openflow, dan Ryu

Buat EC2 Instance di AWS Academy
- Name and tags: Tugas Akhir
- OS Images: Ubuntu Server 22.04 LTS 64 bit
- Instance type: t2.medium
- Key pair: vockey
- Edit Network settings: allow SSH, allow HTTP, allow HTTPS, allow TCP port 8080, allow TCP port 8081
- Configure storage: 30 GiB, gp3

1. Installasi Mininet
   - Command `git clone git://github.com/mininet/mininet`
   - Command `cd mininet`
   - Command `git checkout -b mininet-2.3.0 2.3.0 # or whatever version you wish to install`
   - Command `cd`
   - Installasi mininet `mininet/util/install.sh -nfv`
 
2. Installasi Ryu
   - Command `git clone git://github.com/osrg/ryu.git`
   - Command `cd ryu; pip install`
   - Command `cd`

3. Installasi Openflow
   - Command `git clone https://github.com/martimy/flowmanager`
   - Command `cd`

Selesai sudah untuk installasi Mininet, Ryu, dan Openflownya

## B
   

