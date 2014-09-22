# -*- mode: ruby -*-
# vi: set ft=ruby :

$setup_script = <<SCRIPT

# install our supported chef
sudo dpkg -i /home/vagrant/downloads/debs/chef_11.8.2-1.ubuntu.12.04_amd64.deb

SCRIPT

$test_script = <<SCRIPT
echo "----------TESTING ALL COMPONENTS--------\n\n----------- JAVA VERSION -------------- \n"
java -version
exit 0
SCRIPT

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "precise64"

  # The url from where the 'config.vm.box' box will be fetched if it
  # doesn't already exist on the user's system.
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network :forwarded_port, guest: 8080, host: 18080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network :private_network, ip: "192.168.33.30"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "../data", "/home/vagrant/downloads"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider :virtualbox do |vb|
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "4096"]
  end

  config.vm.provider :vmware_fusion do |v, override|
    override.vm.box_url = "http://files.vagrantup.com/precise64_vmware.box"
 
    v.vmx["memsize"] = "4096"
  end
  #
  # View the documentation for the provider you're using for more
  # information on available options.

  # Enable provisioning with chef solo, specifying a cookbooks path, roles
  # path, and data_bags path (all relative to this Vagrantfile), and adding
  # some recipes and/or roles.
  #
  
  config.vm.provision :shell, inline: $setup_script
  
  config.vm.provision :chef_solo do |chef|
    chef.cookbooks_path = "chef/cookbooks"
    #chef.add_recipe "java"
    
    # You may also specify custom JSON attributes:
    chef.json = {
      :ip_address => '192.168.33.30',
      :chef_environment => "QA",
      :platform => "ubuntu",
      :platform_family => "debian",
      :java => { "jdk" => { "7" => { "x86_64" => { "url" => "file://\/home/vagrant/downloads/other/jdk-7u51-linux-x64.tar.gz" }}},
                 :install_flavor => "oracle" },
      :ulini => { :user => "vagrant" },
      :tomcat => { :java_options => "-Xmx1G -Xms1G -Djava.awt.headless=true" } 
    }
    chef.log_level = :debug
  end
  
  config.vm.provision :shell, inline: $test_script
end
