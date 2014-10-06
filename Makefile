all:
	@echo "build a cloud based tools server (requires vagrant aws plugin)"
	@echo "usage: make devtools cmd=<vagrant command>"
	@echo "   eg: make devtools cmd=up"

.PHONY: devtools clean

Devtoolfile: Devtooltmpl
	@AWS_KEY=$$(grep :aws_access_key_id ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g'); \
	AWS_SECRET=$$(grep :aws_secret_access_key ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g');  \
	AWS_PAIR=$$(grep :aws_ssh_key_id ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g');  \
	PVT_KEY=$$(grep :identity_file ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g'); \
	AWS_AMI=$$(grep :image ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g'); \
	AWS_INSTANCE_TYPE=$$(grep :flavor ~/.chef/knife.rb | awk '{print $$NF}' | sed 's/"//g'); \
	cat Devtooltmpl | \
	sed "s/AWS_KEY/$$AWS_KEY/g" | \
	sed "s/AWS_SECRET/$$AWS_SECRET/g" | \
	sed "s/AWS_PAIR/$$AWS_PAIR/g" | \
	sed "s/AWS_AMI/$$AWS_AMI/g" | \
	sed "s/AWS_INSTANCE_TYPE/$$AWS_INSTANCE_TYPE/g" | \
	sed "s;PVT_KEY;$$PVT_KEY;g" > Devtoolfile

cmd?=status

ifeq ($(cmd),up)
	PROVIDER=--provider=aws
else
	PROVIDER=
endif

devtools: Devtoolfile
	VAGRANT_VAGRANTFILE=Devtoolfile vagrant $(cmd) $(PROVIDER)

clean:
	rm -f Devtoolfile
