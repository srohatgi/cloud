#
# Cookbook Name:: tomcat
# Recipe:: default
#
# Copyright 2010, Opscode, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# required for the secure_password method from the openssl cookbook
::Chef::Recipe.send(:include, Opscode::OpenSSL::Password)

include_recipe "java"

tomcat_pkgs = ["tomcat#{node["tomcat"]["base_version"]}","tomcat#{node["tomcat"]["base_version"]}-admin"]

tomcat_pkgs.each do |pkg|
  package pkg do
    action :install
  end
end

warname = "api"
hostname = "localhost"
if !node['ulini']['user'].eql?("vagrant")
  app_props = Chef::EncryptedDataBagItem.load("pfm-app-props", node.chef_environment)
  warname = app_props["app_war_name"]
  hostname = app_props["host_name"]
end

directory node['tomcat']['endorsed_dir'] do
  mode "0755"
  recursive true
end

service "tomcat" do
  service_name "tomcat#{node["tomcat"]["base_version"]}"
  supports :restart => true, :reload => false, :status => true
  action [:enable, :start]
  retries 2
  retry_delay 10
end

template "/etc/default/tomcat#{node["tomcat"]["base_version"]}" do
  source "default_tomcat6.erb"
  owner "root"
  group "root"
  mode "0644"
  notifies :restart, "service[tomcat]"
end

if !node['ulini']['user'].eql?("vagrant")
  ssl_creds = Chef::EncryptedDataBagItem.load("ssl-creds", node.chef_environment)
  node.set['tomcat']['keystore_password'] = ssl_creds['keystore_password']
end

template "#{node["tomcat"]["config_dir"]}/server.xml" do
  source "server.xml.erb"
  owner "root"
  group "root"
  mode "0644"
  variables({
      :warname => warname,
      :hostname => hostname
  })
  notifies :restart, "service[tomcat]"
end

template "#{node["tomcat"]["config_dir"]}/logging.properties" do
  source "logging.properties.erb"
  owner "root"
  group "root"
  mode "0644"
  notifies :restart, "service[tomcat]"
end

if !node['ulini']['user'].eql?("vagrant")
  script "create_tomcat_keystore" do
    interpreter "bash"
    action :nothing
    user "root"
    cwd node['tomcat']['config_dir']
    code <<-EOH
      cat #{node['tomcat']['ssl_chain_files'].join(' ')} > cacerts.pem
      openssl pkcs12 -export \
       -inkey #{node['tomcat']['ssl_key_file']} \
       -in #{node['tomcat']['ssl_cert_file']} \
       -chain \
       -CAfile cacerts.pem \
       -password pass:#{node['tomcat']['keystore_password']} \
       -out #{node['tomcat']['keystore_file']}
      sudo chown root:tomcat7 /etc/tomcat7/keystore
      sudo chmod 774 /etc/tomcat7/keystore
    EOH
    notifies :restart, "service[tomcat]"
  end

  cookbook_file "#{node['tomcat']['config_dir']}/#{node['tomcat']['ssl_cert_file']}" do
    mode "0644"
    notifies :run, "script[create_tomcat_keystore]"
  end

  cookbook_file "#{node['tomcat']['config_dir']}/#{node['tomcat']['ssl_key_file']}" do
    mode "0644"
    notifies :run, "script[create_tomcat_keystore]"
  end

  node['tomcat']['ssl_chain_files'].each do |cert|
    cookbook_file "#{node['tomcat']['config_dir']}/#{cert}" do
      mode "0644"
      notifies :run, "script[create_tomcat_keystore]"
    end
  end

  script "include_certs_in_java_keystore" do
    interpreter "bash"
    cwd "/usr/lib/jvm/jdk1.7.0_51/jre/lib/security"
    code <<-EOH
    sudo keytool -import -trustcacerts -noprompt -alias startcom.ca -file /etc/tomcat7/startssl_inter_class1.pem -keystore cacerts -storepass changeit
    sudo keytool -import -trustcacerts -noprompt -alias startcom.ca.sub -file /etc/tomcat7/startssl_inter_class1.pem -keystore cacerts -storepass changeit
    sudo keytool -import -trustcacerts -noprompt -alias api.qa.sciul.com -file /etc/tomcat7/#{node.chef_environment}.crt -keystore cacerts -storepass changeit 
    EOH
    user "root"
    notifies :create, "ruby_block[created_certs_flag]", :immediately
    not_if { node.attribute?("created_certs") }
  end

  ruby_block "created_certs_flag" do
    block do
      node.set['created_certs'] = true
      node.save
    end
    action :nothing
  end
end
