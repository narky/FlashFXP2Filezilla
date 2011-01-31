#!/usr/bin/env python
# -*- coding: UTF-8  -*-

# =====================================
# FlashFxp To FileZilla Sites Converter
# File: Core.py
# Class: SiteParse
# =====================================

__author__ = 'narky'
__date__ = '11-1-19'
__version__ = '1.0'

from xml2dict.xml2dict import XML2Dict
from Temlpate import fileTemplate,serverTemplate,folderTemplate
from Lang import _L

def writeFilezillaXmlFile(dict, filename='Filezilla.xml'):
	try:
		sites=dict.SITES.SITE
	except KeyError:
		return

	_servers,_params,_groups = [],[],[]
	groups = {}
	for site in sites:
		if site.has_key('GROUP'):
			group = trimSlashes(site['GROUP']['value'])
		else:
			group = _L["no_group"]
		if groups.has_key(group)==False:
			groups[group]=[]
		
		_params = (
			#Host
			site['ADDRESS']['value'],
			#Port
			site['PORT']['value'],
			#Protocol
			site['PROTOCOL']['value'],
			#Type
			'0',
			#User
			site['USERNAME']['value'],
			#Pass
			site['PASSWORD']['value'],
			#Logontype
			'1',
			#TimezoneOffset
			'0',
			#PasvMode
			parsePassive(site['PASSIVE']['value']),
			#MaximumMultipleConnections
			'0',
			#EncodingType
			'Auto',
			#BypassProxy
			'0',
			#Name
			site['NAME']['value'],
			#Comments
			(site.has_key('NOTES') and [site['NOTES']['value']] or [''])[0],
			#LocalDir
			(site.has_key('LOCALPATH') and [site['LOCALPATH']['value']] or [''])[0],
			#RemoteDir
			(site.has_key('REMOTEPATH') and [parseRemotePath(site['REMOTEPATH']['value'])] or [''])[0],
			#SyncBrowsing
			'0',
			site['NAME']['value'],
		)
		groups.has_key(group) and groups[group].append(_params)
	for group in groups:
		_servers = []
		for server in groups[group]:
			_servers.append(serverTemplate % server)
		_groups.append(folderTemplate % (group,"".join(_servers)))

	fileContent=fileTemplate % ("".join(_groups)).encode('UTF-8')
	return writeFile(filename,fileContent)

def parseRemotePath(remotePath, char='/'):
	li = remotePath.split(char)
	fl = remotePath[0]
	if fl=='/':
		return "1 0 %s" % "".join([(lambda s: " ".join(["%s" % len(s),s]))(item)+" " for item in li][1:])
	if fl=='\\':
		return "8 0 %s %s" % (("%s" % len(remotePath[1:])),remotePath[1:])

def parsePassive(passive):
	return "MODE_%s" % {'DEFAULT':'DEFAULT','ON':'PASSIVE','OFF':'ACTIVE'}[passive]

def trimSlashes(str):
	return str.replace("\\","")

def writeFile(fileName, fileContent):
	try:
		f = open(fileName,'w')
		f.write(fileContent)
		f.close()
		return True
	except IOError:
		return False

def main():
	r = XML2Dict().parse('flashfxp_sites.xml')
	writeFilezillaXmlFile(r)

if __name__ == '__main__':
	main()