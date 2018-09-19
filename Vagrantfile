# # -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "eduardojvr/raspberrypi2"
  # config.vm.box_url = "https://app.vagrantup.com/eduardojvr/boxes/raspberrypi2/versions/1.0/providers/virtualbox.box"
  config.vm.box_version = "1.0"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provision :shell, path: "setuprasp.sh"
  config.vm.hostname = "raspberry"
  config.ssh.username = "pi"
  config.ssh.password = "vagrant"
  config.ssh.insert_key=false
  #config.vm.synced_folder "troca", "/home/pi/Desktop/troca"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 1000
    vb.name = "raspberrypi-2"
    vb.gui = true

  end
  
end
