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

![Screenshot (555)](https://user-images.githubusercontent.com/97608893/172868674-7a7c3f1f-89dc-432a-ae1d-d971fac8742c.png)


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

![M Arya Nugraha_Hasil instalasi flow,ryu, dan minimet](https://user-images.githubusercontent.com/97608893/172869181-f7f06541-7950-424b-b339-8268ee284c26.png)

## BAB 2 Custom Mininet Topology

1. Jalankan Mininet dengan Custom Topology dengan command `$ sudo mn --controller=none --custom custom_topo_2sw2h.py --topo mytopo --mac --arp`
2. Selah itu buat flow agar h1 terhubung dengan h2 dengan command `mininet> sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=1,action=output:2"`,
   `mininet> sh ovs-ofctl add-flow s1 -O OpenFlow13 "in_port=2,action=output:1"`,
   `mininet> sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=1,action=output:2"`,
   `mininet> sh ovs-ofctl add-flow s2 -O OpenFlow13 "in_port=2,action=output:1“`
3. Uji koneksi h1 dengan h2 `mininet> h1 ping -c2 h2`
   
   Setelah itu kita mencoaba percobaan pada topology mininet 3 switch (loop) dengan 6 host dengan penerapan STP. Gunakan command `Kode program custom mininet topology.py`.
   Setelah itu kita dapat lihat hasilnya
   ![Screenshot (458)](https://user-images.githubusercontent.com/97608893/172869328-bb63de58-f8d1-45b3-86f6-8a9a524d4e55.png)
![Screenshot (459)](https://user-images.githubusercontent.com/97608893/172869349-49fdee2e-7f43-4678-a8b5-3225f2b8b1a9.png)

## BAB 3 Ryu Load Balancer

- Unduh kedua file berikut ke direktori Linux `topo_lb.py`, dan `rr_lb.py`
- Jalankan program rr_lb.py dengan `ryu-manager rr_lb.py` # pada terminal console 1
- Jalankan topo_lb.py dgn `sudo python3 topo_lb.py` # pada terminal console 2
- Pada mininet> console di terminal console 2 jalankan `h1 curl 10.0.0.100`
- Gunakan topologi standart `sudo mn --controller=remote --topo single,4 --mac`
- gunakan: mininet> h1 curl 10.0.0.100
- gunakan round-robin
- jalankan dengan perintah dalam console " mininet> h2 python3 -m http.server 80 & " hal yg sama untuk h3 dan h4



## BAB 4 Shortest Path Route

- Pertama kita jalankan Program Ryu - Dijkstra
clone repo berikut https://github.com/abazh/learn_sdn.git
`$ git clone https://github.com/abazh/learn_sdn.git`
- Setelah itu jalankan `$ cd learn_sdn/SPF`
- Buka 2 terminal
- Pada Terminal Console 1 jalankan: `$ ryu-manager --observe-links dijkstra_Ryu_controller.py`
- Pada Terminal Console 2 jalankan: `$ sudo python3 topo-spf_lab.py`
- Lanjutkan dengan cek semua konektivitas, misalnya `$ mininet> h1 ping -c 4 h4` , `$ mininet> h5 ping -c 4 h6`

![Screenshot (539)](https://user-images.githubusercontent.com/97608893/172881973-5d922830-c74e-41dc-a093-36a0a0874b16.png)
![Screenshot (540)](https://user-images.githubusercontent.com/97608893/172881989-2574c3d7-08b0-4901-8475-ebc05a4bb70f.png)
![Screenshot (541)](https://user-images.githubusercontent.com/97608893/172881997-7b9a6a06-148a-44b2-a2d2-ece1234dc2f9.png)
![Screenshot (538)](https://user-images.githubusercontent.com/97608893/172882005-529e5271-db43-4bdc-b5b8-ee765705ce29.png)

Hasil observasi yang dilakukan dapat disimpulkan Saat menjalankan perintah h1 ping -c 4 h4, paket yang dikirim sebanyak 4 dan diterima sebanyak
4. Selama melaksanakan perintah ini, sebanyak 4 kali ping dari h1 dan h4, diantaranya sebanya 2
kali h1 dan 2 kali h4, akan tetapi ketika saya coba ulang kembali terjadi duplikasi sebanyak 3 kali.
Saat menjalankan h5 ping –c 4 h6, terjadi loss paket sebesar 25%, dan ketika saya melakukan
percobaan ke 2 kalinya terjadi loss paket sebasar 50%. Hal ini disebabkan mungkin, program tidak
menemukan jalan untuk menuju h5 ke h6 atau sebaliknya. Atau tidak terlaksanakan program
dengan jelas.
