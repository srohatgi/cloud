#
# Cookbook Name:: tomcat
# Attributes:: default
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

default["tomcat"]["base_version"] = 7
default["tomcat"]["port"] = 8080
default["tomcat"]["proxy_port"] = nil
default["tomcat"]["ssl_port"] = 8443
default["tomcat"]["ssl_proxy_port"] = nil
default["tomcat"]["ajp_port"] = 8009
default["tomcat"]["catalina_options"] ="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=8999 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -Djava.rmi.server.hostname=localhost" 
default["tomcat"]["java_options"] = "-Xmx4G -Xms4G -Djava.awt.headless=true"
default["tomcat"]["use_security_manager"] = false
default["tomcat"]["authbind"] = "no"
default["tomcat"]["deploy_manager_apps"] = true
default["tomcat"]["ssl_max_threads"] = 150
default["tomcat"]["ssl_cert_file"] = "#{node.chef_environment}.crt"
default["tomcat"]["ssl_key_file"] = "#{node.chef_environment}.key"
default["tomcat"]["ssl_chain_files"] = ["startssl_inter_class1.pem","startssl_root.pem"]
default["tomcat"]["keystore_file"] = "keystore"
default["tomcat"]["keystore_type"] = "PKCS12"
default["tomcat"]["loglevel"] = "INFO"
default["tomcat"]["tomcat_auth"] = "true"

default["tomcat"]["user"] = "tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["group"] = "tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["home"] = "/usr/share/tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["base"] = "/var/lib/tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["config_dir"] = "/etc/tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["log_dir"] = "/var/log/tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["tmp_dir"] = "/tmp/tomcat#{node["tomcat"]["base_version"]}-tmp"
default["tomcat"]["work_dir"] = "/var/cache/tomcat#{node["tomcat"]["base_version"]}"
default["tomcat"]["context_dir"] = "#{node["tomcat"]["config_dir"]}/Catalina/localhost"
default["tomcat"]["webapp_dir"] = "/var/lib/tomcat#{node["tomcat"]["base_version"]}/webapps"
default["tomcat"]["keytool"] = "/usr/lib/jvm/default-java/bin/keytool"
default["tomcat"]["lib_dir"] = "#{node["tomcat"]["home"]}/lib"
default["tomcat"]["endorsed_dir"] = "#{node["tomcat"]["lib_dir"]}/endorsed"

default["tomcat"]["catalina_home"] = "/home/vagrant/downloads/other/apache-tomcat-7.0.26"
