Vagrant.configure("2") do |config|
  config.vm.box = "eduardojvr/rasperrypi2"
  config.vm.box_url = ""
  config.vm.box_version = "1.0"
  
  config.vm.provider "virtualbox" do |machine|
    	machine.memory = 1000
    	machine.name = "pi2-ambiente"
      machine.cpus = 2
  end

  config.vm.provision :shell, path: "setup.sh"

end