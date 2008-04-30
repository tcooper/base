# $Id: __init__.py,v 1.7 2008/03/06 23:41:38 mjk Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		            version 5.0 (V)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: __init__.py,v $
# Revision 1.7  2008/03/06 23:41:38  mjk
# copyright storm on
#
# Revision 1.6  2007/07/04 01:47:38  mjk
# embrace the anger
#
# Revision 1.5  2007/06/28 19:45:44  bruno
# all the 'rocks list host' commands now have help
#
# Revision 1.4  2007/06/19 16:42:41  mjk
# - fix add host interface docstring xml
# - update copyright
#
# Revision 1.3  2007/05/31 19:35:42  bruno
# first pass at getting all the 'help' consistent on all the rocks commands
#
# Revision 1.2  2007/05/10 20:37:01  mjk
# - massive rocks-command changes
# -- list host is standardized
# -- usage simpler
# -- help is the docstring
# -- host groups and select statements
# - added viz commands
#
# Revision 1.1  2007/05/02 20:20:53  bruno
# added 'pxeaction' table -- allows for adding and removing pxeboot actions
#
#

import sys
import socket
import rocks.commands
import string

class Command(rocks.commands.list.host.command):
	"""
	Lists the set of PXE actions for hosts. Each PXE action is a label
	that points to a command string. The command string is placed into
	a host-specific pxelinux configuration file. Example labels are
	'install' and 'os' which point to command strings used to install
	and boot hosts respectively.

	<arg optional='1' type='string' name='host' repeat='1'>
	Zero, one or more host names. If no host names are supplied, info about
	all the known hosts is listed.
	</arg>

	<example cmd='list host pxeaction compute-0-0'>
	List the PXE actions available for compute-0-0.
	</example>

	<example cmd='list host pxeaction'>
	List the PXE actions available for all known hosts.
	</example>
	"""

	def run(self, params, args):

		self.beginOutput()

		# Using a dictionary read the default values for all nodes
		# and override the entries with the per-node values.
		
		for host in self.getHostnames(args):
			dict = {}
			self.db.execute("""select
				p.action, p.command, p.args from
				nodes n, pxeaction p where
				p.node=0 and n.name='%s'""" % host)

			for row in self.db.fetchall():
				dict[row[0]] = row

			self.db.execute("""select
				p.action, p.command, p.args from
				nodes n, pxeaction p where
				p.node=n.id and n.name='%s'""" % host)
			for row in self.db.fetchall():
				dict[row[0]] = row
			keys = dict.keys()
			keys.sort()
			for action in keys:
				self.addOutput(host, dict[action])

		self.endOutput(header=['host', 'action', 'command', 'args'])

