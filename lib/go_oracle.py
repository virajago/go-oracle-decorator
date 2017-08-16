# go-oracle-decorator
#
# Copyright (c) 2017-Present Pivotal Software, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import sys
import json
import urllib2
import base64
import ssl
import time

urlargs = {}
try:
	ctx = ssl.create_default_context()
	urlargs['context'] = ctx
except:
	ctx = None

def main():
	get_vcap_config()
	if skip_ssl_validation and ctx is not None:
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE
	appinfo = get_application_info()

def decorate():
	appinfo = get_application_info()
	#service = find_eureka_service(appinfo)
	#if service == None:
		#sys.exit(1)
	print 'go-oracle'

vcap_config = None
log_level = 1
skip_ssl_validation = False

def get_vcap_config():
	global vcap_config
	global log_level
	global skip_ssl_validation
	vcap_config = json.loads(os.getenv('VCAPX_CONFIG', '{}'))
	log_level = vcap_config.get('loglevel', 1)
	skip_ssl_validation = vcap_config.get('skip_ssl_validation', False)

# Get Application Info
#
# Collect the information about this application instance
#
def get_application_info():
	appinfo = {}
	vcap_application = json.loads(os.getenv('VCAP_APPLICATION', '{}'))
	appinfo['name'] = vcap_application.get('application_name')
	if appinfo['name'] == None:
		print >> sys.stderr, "VCAP_APPLICATION must specify application_name"
		sys.exit(1)
	appinfo['instance'] = os.getenv('CF_INSTANCE_INDEX')
	appinfo['hostname'] = vcap_application.get('application_uris')[0]
	appinfo['ipaddress'] = os.getenv('CF_INSTANCE_IP')
	appinfo['port'] = os.getenv('CF_INSTANCE_PORT')
	return appinfo

if __name__ == "__main__":
	main()
